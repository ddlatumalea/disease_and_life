from pathlib import Path

import pandas as pd

from models.utils import generate_ICD_codes, convert_format, multi_merge
from models.utils.paths import get_prepared_data_path, get_cleaned_data_path
from models.selectors import DataFrameSelector
from models.aggregators import Aggregator

DATA_PREPARED_DIR = Path(get_prepared_data_path())
DATA_CLEANED_DIR = Path(get_cleaned_data_path())
LIFE_EXPECTANCY_FILE = 'life_expectancy.csv'
MORTALITY_FILE = 'mortality.csv'
POPULATION_FILE = 'population.csv'

NL_CODE = 4210
JP_CODE = 3160
CA_CODE = 2090

CODE_TO_NAME_MAP = {
    'C': 'cancer [deaths]',
    'I': 'cardiovascular disease [deaths]',
    'E': 'diabetes mellitus [deaths]',
    'J': 'chronic respiratory diseases [deaths]',
    'K': 'diseases of digestive system [deaths]'
}

NAME_TO_CODE_MAP = {
    'cancer [deaths]': 'C',
    'cardiovascular disease [deaths]': 'I',
    'diabetes mellitus [deaths]': 'E',
    'chronic respiratory diseases [deaths]': 'J',
    'diseases of digestive system [deaths]': 'K',
}

MIN_YEARS = 1996
MAX_YEARS = 2018



if __name__ == '__main__':
    df_life_exp = pd.read_csv(Path(DATA_CLEANED_DIR, LIFE_EXPECTANCY_FILE))
    df_mortality = pd.read_csv(Path(DATA_CLEANED_DIR, MORTALITY_FILE))
    df_population = pd.read_csv(Path(DATA_CLEANED_DIR, POPULATION_FILE))

    nl_life_exp = df_life_exp[(df_life_exp['country'] == 'Netherlands')]
    jp_life_exp = df_life_exp[(df_life_exp['country'] == 'Japan')]
    ca_life_exp = df_life_exp[(df_life_exp['country'] == 'Canada')]

    nl_mortality = df_mortality[(df_mortality['country code'] == NL_CODE)]
    jp_mortality = df_mortality[(df_mortality['country code'] == JP_CODE)]
    ca_mortality = df_mortality[(df_mortality['country code'] == CA_CODE)]

    nl_population = df_population[(df_population['country code'] == NL_CODE)]
    jp_population = df_population[(df_population['country code'] == JP_CODE)]
    ca_population = df_population[(df_population['country code'] == CA_CODE)]

    # drop sex 9 as this is not usesful
    ca_mortality = ca_mortality[~ca_mortality['sex'].isin([9])]
    ca_population = ca_population[~ca_population['sex'].isin([9])]

    life_exp_set = [nl_life_exp, jp_life_exp, ca_life_exp]
    mort_set = [nl_mortality, jp_mortality, ca_mortality]
    pop_set = [nl_population, jp_population, ca_population]

    # generate ICD-10 codes
    C_codes = generate_ICD_codes(0, 97, 'C')
    I_codes = generate_ICD_codes(5, 99, 'I')
    E_codes = generate_ICD_codes(10, 13, 'E')
    J_codes = generate_ICD_codes(40, 47, 'J')
    K_codes = generate_ICD_codes(0, 93, 'K')

    codes = [C_codes, I_codes, E_codes, J_codes, K_codes]
    labels = ['C', 'I', 'E', 'J', 'K']

    # get causes of mortality
    nl_causes = convert_format(nl_mortality['cause'], 3)
    jp_causes = convert_format(jp_mortality['cause'], 3)
    ca_causes = convert_format(ca_mortality['cause'], 3)

    nl_unique_causes = nl_causes.unique()
    jp_unique_causes = jp_causes.unique()
    ca_unique_causes = ca_causes.unique()

    nl_mortality.loc[:, 'cause'] = nl_causes
    jp_mortality.loc[:, 'cause'] = jp_causes
    ca_mortality.loc[:, 'cause'] = ca_causes


    # select the correct mortality data
    nl_mortality_selector = DataFrameSelector(nl_mortality)
    nl_mortality_selector.split_dataframe('cause', labels, codes)
    nl_mortality_selector.rename_selection('deaths', CODE_TO_NAME_MAP)
    nl_mortality_sets = nl_mortality_selector.get_selection()

    jp_mortality_selector = DataFrameSelector(jp_mortality)
    jp_mortality_selector.split_dataframe('cause', labels, codes)
    jp_mortality_selector.rename_selection('deaths', CODE_TO_NAME_MAP)
    jp_mortality_sets = jp_mortality_selector.get_selection()

    ca_mortality_selector = DataFrameSelector(ca_mortality)
    ca_mortality_selector.split_dataframe('cause', labels, codes)
    ca_mortality_selector.rename_selection('deaths', CODE_TO_NAME_MAP)
    ca_mortality_sets = ca_mortality_selector.get_selection()

    # create aggregates
    for k, df in nl_mortality_sets.items():
        aggr = Aggregator(df)
        aggr.calc_aggr(by=['year', 'sex'], on=CODE_TO_NAME_MAP[k])
        aggr.calc_aggr(by=['year'], on=CODE_TO_NAME_MAP[k], column='sex', value=3)

        data = aggr.get_aggregation(sort_by='year')
        data['country'] = 'Netherlands'

        nl_mortality_sets[k] = data

    for k, df in jp_mortality_sets.items():
        aggr = Aggregator(df)
        aggr.calc_aggr(by=['year', 'sex'], on=CODE_TO_NAME_MAP[k])
        aggr.calc_aggr(by=['year'], on=CODE_TO_NAME_MAP[k], column='sex', value=3)

        data = aggr.get_aggregation(sort_by='year')
        data['country'] = 'Japan'

        jp_mortality_sets[k] = data

    for k, df in ca_mortality_sets.items():
        aggr = Aggregator(df)
        aggr.calc_aggr(by=['year', 'sex'], on=CODE_TO_NAME_MAP[k])
        aggr.calc_aggr(by=['year'], on=CODE_TO_NAME_MAP[k], column='sex', value=3)

        data = aggr.get_aggregation(sort_by='year')
        data['country'] = 'Canada'

        ca_mortality_sets[k] = data

    # select the correct population data
    aggr = Aggregator(nl_population)
    aggr.calc_aggr(by=['year', 'sex'], on='population')
    aggr.calc_aggr(by=['year'], on='population', column='sex', value=3)
    data = aggr.get_aggregation(sort_by='year')
    data['country'] = 'Netherlands'

    nl_pop_agg = data

    aggr = Aggregator(jp_population)
    aggr.calc_aggr(by=['year', 'sex'], on='population')
    aggr.calc_aggr(by=['year'], on='population', column='sex', value=3)
    data = aggr.get_aggregation(sort_by='year')
    data['country'] = 'Japan'

    jp_pop_agg = data

    aggr = Aggregator(ca_population)
    aggr.calc_aggr(by=['year', 'sex'], on='population')
    aggr.calc_aggr(by=['year'], on='population', column='sex', value=3)
    data = aggr.get_aggregation(sort_by='year')
    data['country'] = 'Canada'

    ca_pop_agg = data

    # combine all data
    nl_dfs = []
    jp_dfs = []
    ca_dfs = []

    nl_dfs.extend([df for df in nl_mortality_sets.values()])
    jp_dfs.extend([df for df in jp_mortality_sets.values()])
    ca_dfs.extend([df for df in ca_mortality_sets.values()])

    nl_dfs.append(nl_pop_agg)
    nl_dfs.append(nl_life_exp)
    jp_dfs.append(jp_pop_agg)
    jp_dfs.append(jp_life_exp)
    ca_dfs.append(ca_pop_agg)
    ca_dfs.append(ca_life_exp)

    nl_dataset = multi_merge(nl_dfs, on=['year', 'sex', 'country']).sort_values('year')
    nl_dataset = nl_dataset[(nl_dataset['year'] > 1995) & (nl_dataset['year'] < 2019)]
    nl_dataset['non-communicable chronic disease [deaths]'] = 0
    for disease in NAME_TO_CODE_MAP.keys():
        nl_dataset['non-communicable chronic disease [deaths]'] += nl_dataset[disease]
    nl_dataset = nl_dataset.sort_values(['year', 'sex']).reset_index(drop=True)

    jp_dataset = multi_merge(jp_dfs, on=['year', 'sex', 'country']).sort_values('year')
    jp_dataset = jp_dataset[(jp_dataset['year'] > 1995) & (jp_dataset['year'] < 2019)]
    jp_dataset['non-communicable chronic disease [deaths]'] = 0
    for disease in NAME_TO_CODE_MAP.keys():
        jp_dataset['non-communicable chronic disease [deaths]'] += jp_dataset[disease]
    jp_dataset = jp_dataset.sort_values(['year', 'sex']).reset_index(drop=True)

    ca_dataset = multi_merge(ca_dfs, on=['year', 'sex', 'country']).sort_values('year')
    ca_dataset = ca_dataset[(ca_dataset['year'] > 1995) & (ca_dataset['year'] < 2019)]
    ca_dataset['non-communicable chronic disease [deaths]'] = 0
    for disease in NAME_TO_CODE_MAP.keys():
        ca_dataset['non-communicable chronic disease [deaths]'] += ca_dataset[disease]
    ca_dataset = ca_dataset.sort_values(['year', 'sex']).reset_index(drop=True)

    # concatenate the sets and save
    full_dataset = pd.concat([nl_dataset, jp_dataset, ca_dataset]).reset_index(drop=True)
    full_dataset.to_csv(Path(DATA_PREPARED_DIR, 'full_dataset.csv'), index=False)

    # standardized set
    cols = ['cancer [deaths]',
            'cardiovascular disease [deaths]', 'diabetes mellitus [deaths]',
            'chronic respiratory diseases [deaths]',
            'diseases of digestive system [deaths]',
            'non-communicable chronic disease [deaths]']
    full_dataset_standardized = full_dataset
    full_dataset_standardized[cols] = full_dataset[cols].divide(full_dataset['population'], axis=0) * 100000

    full_dataset_standardized.to_csv(Path(DATA_PREPARED_DIR, 'full_dataset_standardized.csv'), index=False)