from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class Cleaner(ABC):

    def __init__(self, file):
        self.file = file

    @abstractmethod
    def has_missing_values(self):
        pass

    @abstractmethod
    def handle_missing_values(self):
        pass


class DataFrameCleaner(Cleaner):

    def __init__(self, file):
        if not isinstance(file, pd.DataFrame):
            raise ValueError('Expects a pandas DataFrame.')

        super().__init__(file)

        self.column_lower()

    def __str__(self):
        return self.file.head().to_string()

    def column_lower(self):
        self.file.columns = self.file.columns.str.lower()

    def keep_columns(self, to_keep: list):
        self.file = self.file[to_keep]

    def rename_columns(self, mapping: dict):
        self.file = self.file.rename(columns=mapping)

    def assign_dtypes(self, mapping: dict):
        try:
            self.file = self.file.astype(mapping)
        except KeyError:
            print('Some error occurred.')
        except:
            print('Some error occurred')

    def convert_values(self, mapping, column):

        def convert(x):
            return mapping[x]

        self.file[column] = self.file[column].apply(convert)

    def has_missing_values(self):
        return self.file.isna().sum().sum() != 0

    def get_data(self):
        return self.file

    def handle_missing_values(self):
        """Expects a function as input that outputs the file while replacing missing values."""
        pass


def clean_life_expectancy(df):
    cleaner = DataFrameCleaner(df)

    if cleaner.has_missing_values():
        print('Has missing values!')
        # cleaners.handle_missing_values(())

    cols_to_keep = ['year', 'country', 'sex', 'value']
    cols_names = {
        'value': 'life expectancy [age]'
    }
    dtypes_mapping = {
        'year': 'int',
        'country': 'str',
        'sex': 'str',
        'life expectancy [age]': 'float'
    }
    mapping_sex = {
        'Male': 1,
        'Female': 2,
        'Both sexes': 3
    }

    cleaner.keep_columns(cols_to_keep)
    cleaner.rename_columns(cols_names)
    cleaner.assign_dtypes(dtypes_mapping)
    cleaner.convert_values(mapping_sex, 'sex')

    return cleaner.get_data()


def clean_country_codes(df):
    cleaner = DataFrameCleaner(df)

    if cleaner.has_missing_values():
        print('Has missing values!')
        # cleaners.handle_missing_values(())

    cols_names = {
        'country': 'country code',
        'name': 'country'
    }
    dtypes_mapping = {
        'country code': 'int',
        'country': 'str'
    }

    cleaner.rename_columns(cols_names)
    cleaner.assign_dtypes(dtypes_mapping)

    return cleaner.get_data()


def clean_population(df):
    cleaner = DataFrameCleaner(df)

    if cleaner.has_missing_values():
        print('Has missing values!')
        # cleaners.handle_missing_values(())

    cols_to_keep = ['country', 'year', 'sex', 'pop1']
    cols_names = {
        'country': 'country code',
        'pop1': 'population'
    }
    dtypes_mapping = {
        'country code': 'int',
        'year': 'int',
        'sex': 'int',
        'population': 'float'
    }
    mapping_sex = {
        1: 1,
        2: 2,
        9: 'unspecified'
    }

    cleaner.keep_columns(cols_to_keep)
    cleaner.rename_columns(cols_names)
    cleaner.assign_dtypes(dtypes_mapping)
    cleaner.convert_values(mapping_sex, 'sex')

    return cleaner.get_data()


def clean_mortality(df):
    cleaner = DataFrameCleaner(df)

    if cleaner.has_missing_values():
        print('Has missing values!')
        # cleaners.handle_missing_values(())

    cols_to_keep = ['country', 'year', 'list', 'cause', 'sex', 'deaths1']
    cols_names = {
        'country': 'country code',
        'deaths1': 'deaths'
    }
    dtypes_mapping = {
        'country code': 'int',
        'year': 'int',
        'list': 'str',
        'cause': 'str',
        'sex': 'int',
        'deaths': 'int'
    }
    mapping_sex = {
        1: 1,
        2: 2,
        9: 'unspecified'
    }

    cleaner.keep_columns(cols_to_keep)
    cleaner.rename_columns(cols_names)
    cleaner.assign_dtypes(dtypes_mapping)
    # cleaner.convert_values(mapping_sex, 'sex')

    return cleaner.get_data()
