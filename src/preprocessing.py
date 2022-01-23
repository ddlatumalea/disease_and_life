import yaml
from pathlib import Path

import pandas as pd

from models.cleaners import clean_population, clean_country_codes, clean_life_expectancy, clean_mortality


def get_data_path():
    with open('config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

    return config['data_dir']


def get_cleaned_data_path():
    with open('config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

    return config['data_cleaned_dir']


DATA_DIR = get_data_path()
DATA_CLEANED_DIR = get_cleaned_data_path()

LIFE_EXPECTANCY_FILE = 'life_expectancy_at_birth.xlsx'
COUNTRY_CODES_FILE = 'country_codes'
POPULATION_FILE = 'pop'
MORTALITY_FILE = 'Morticd10_part'  # append 1 till 5 and concatenate the 5 files together

LIFE_EXPECTANCY_PATH = Path(DATA_DIR, LIFE_EXPECTANCY_FILE)
COUNTRY_CODES_PATH = Path(DATA_DIR, COUNTRY_CODES_FILE)
POPULATION_PATH = Path(DATA_DIR, POPULATION_FILE)
MORTALITY_PATH = Path(DATA_DIR, MORTALITY_FILE)

if __name__ == '__main__':
    # Load datasets
    mortality_datasets = [Path(DATA_DIR, f"{MORTALITY_FILE}{str(i + 1)}") for i in range(0, 5)]
    mortality_datasets = [pd.read_csv(data_path) for data_path in mortality_datasets]

    df_life_exp = pd.read_excel(LIFE_EXPECTANCY_PATH)
    df_country_codes = pd.read_csv(COUNTRY_CODES_PATH)
    df_population = pd.read_csv(POPULATION_PATH)
    df_mortality = pd.concat(mortality_datasets)

    # call cleaners
    df_life_exp = clean_life_expectancy(df_life_exp)
    df_country_codes = clean_country_codes(df_country_codes)
    df_population = clean_population(df_population)
    df_mortality = clean_mortality(df_mortality)

    # save files
    df_life_exp.to_csv(Path(DATA_CLEANED_DIR, 'life_expectancy.csv'), index=False)
    df_country_codes.to_csv(Path(DATA_CLEANED_DIR, 'country_codes.csv'), index=False)
    df_population.to_csv(Path(DATA_CLEANED_DIR, 'population.csv'), index=False)
    df_mortality.to_csv(Path(DATA_CLEANED_DIR, 'mortality.csv'), index=False)
