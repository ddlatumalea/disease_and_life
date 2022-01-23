from pathlib import Path
import yaml

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

CODE_TO_NAME_MAP = {
    'C': 'cancer [deaths]',
    'I': 'cardiovascular disease [deaths]',
    'E': 'diabetes mellitus [deaths]',
    'J': 'chronic respiratory diseases [deaths]',
    'K': 'diseases of digestive system [deaths]'
}

MIN_YEARS = 1996
MAX_YEARS = 2018

if __name__ == '__main__':
    df_life_exp = pd.read_csv(Path(DATA_CLEANED_DIR, LIFE_EXPECTANCY_FILE))
    df_mortality = pd.read_csv(Path(DATA_CLEANED_DIR, MORTALITY_FILE))
    df_population = pd.read_csv(Path(DATA_CLEANED_DIR, POPULATION_FILE))

    nl_life_exp = df_life_exp[['year', 'sex', 'life expectancy [age]']]
    nl_mortality = df_mortality[df_mortality['country code'] == NL_CODE]
    nl_population = df_population[df_population['country code'] == NL_CODE]

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
    nl_mortality.loc[:, 'cause'] = nl_causes

    nl_unique_causes = nl_causes.unique()

    # select the correct mortality data
    nl_mortality = nl_mortality[(nl_mortality['year'] >= MIN_YEARS) & (nl_mortality['year'] <= MAX_YEARS)]
    mortality_selector = DataFrameSelector(nl_mortality)
    mortality_selector.split_dataframe('cause', labels, codes)
    mortality_selector.rename_selection('deaths', CODE_TO_NAME_MAP)
    mortality_sets = mortality_selector.get_selection()

    # create aggregates
    for k, df in mortality_sets.items():
        aggr = Aggregator(df)
        aggr.calc_aggr(by=['year', 'sex'], on=CODE_TO_NAME_MAP[k])
        aggr.calc_aggr(by=['year'], on=CODE_TO_NAME_MAP[k], column='sex', value=3)

        mortality_sets[k] = aggr.get_aggregation(sort_by='year')

    # select the correct population data
    nl_population = nl_population[(nl_population['year'] >= MIN_YEARS) & (nl_population['year'] <= MAX_YEARS)]

    aggr = Aggregator(nl_population)
    aggr.calc_aggr(by=['year', 'sex'], on='population')
    aggr.calc_aggr(by=['year'], on='population', column='sex', value=3)
    nl_pop_agg = aggr.get_aggregation(sort_by='year')

    # combine all data
    nl_life_exp = nl_life_exp[(nl_life_exp['year'] >= MIN_YEARS) & (nl_life_exp['year'] <= MAX_YEARS)]

    dfs = [df for df in mortality_sets.values()]
    dfs.append(nl_pop_agg)
    dfs.append(nl_life_exp)

    dataset = multi_merge(dfs, on=['year', 'sex']).sort_values('year')

    dataset['non-communicable chronic disease [deaths]'] = 0
    for disease in CODE_TO_NAME_MAP.values():
        dataset['non-communicable chronic disease [deaths]'] += dataset[disease]

    # save to csv
    file_name = 'merged_data.csv'
    dataset.to_csv(Path(DATA_PREPARED_DIR, file_name), index=False)