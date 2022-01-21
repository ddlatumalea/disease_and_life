"""
Codes for sexes:
1 -> male
2 -> female
3 -> male and female
9 -> unspecified
"""

from abc import ABC, abstractmethod
from typing import Callable
import pandas as pd


class Cleaner(ABC):

    def __init__(self, file: object) -> None:
        self.file = file

    @abstractmethod
    def has_missing_values(self) -> bool:
        pass

    @abstractmethod
    def handle_missing_values(self, func: Callable) -> None:
        pass


class DataFrameCleaner(Cleaner):

    def __init__(self, file: pd.DataFrame):
        if not isinstance(file, pd.DataFrame):
            raise ValueError('Expects a pandas DataFrame.')

        super().__init__(file)

        self.column_lower()

    def __str__(self) -> str:
        return self.file.head().to_string()

    def column_lower(self) -> None:
        self.file.columns = self.file.columns.str.lower()

    def keep_columns(self, to_keep: list) -> None:
        self.file = self.file[to_keep]

    def rename_columns(self, mapping: dict) -> None:
        self.file = self.file.rename(columns=mapping)

    def assign_dtypes(self, mapping: dict) -> None:
        try:
            self.file = self.file.astype(mapping)
        except KeyError:
            print('Some error occurred.')
        except Exception as e:
            print('Some error occurred', e)

    def convert_values(self, mapping, column) -> None:

        def convert(x):
            return mapping[x]

        self.file[column] = self.file[column].apply(convert)

    def has_missing_values(self) -> bool:
        return self.file.isna().sum().sum() != 0

    def get_data(self) -> pd.DataFrame:
        return self.file

    def handle_missing_values(self, func: Callable) -> None:
        """Expects a function as input that outputs the file while replacing missing values."""
        self.file = func(self.file)


def clean_life_expectancy(df: pd.DataFrame) -> pd.DataFrame:
    cleaner = DataFrameCleaner(df)

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

    if cleaner.has_missing_values():
        print('Has missing values!')
        # cleaners.handle_missing_values(())

    cleaner.rename_columns(cols_names)
    cleaner.assign_dtypes(dtypes_mapping)
    cleaner.convert_values(mapping_sex, 'sex')

    return cleaner.get_data()


def clean_country_codes(df: pd.DataFrame) -> pd.DataFrame:
    cleaner = DataFrameCleaner(df)

    cols_names = {
        'country': 'country code',
        'name': 'country'
    }
    dtypes_mapping = {
        'country code': 'int',
        'country': 'str'
    }

    if cleaner.has_missing_values():
        print('Has missing values!')
        # cleaners.handle_missing_values(())

    cleaner.rename_columns(cols_names)
    cleaner.assign_dtypes(dtypes_mapping)

    return cleaner.get_data()


def clean_population(df: pd.DataFrame) -> pd.DataFrame:
    cleaner = DataFrameCleaner(df)

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
        9: 9
    }

    cleaner.keep_columns(cols_to_keep)

    if cleaner.has_missing_values():
        print('Has missing values!')
        # cleaners.handle_missing_values(())

    cleaner.rename_columns(cols_names)
    cleaner.assign_dtypes(dtypes_mapping)
    cleaner.convert_values(mapping_sex, 'sex')

    return cleaner.get_data()


def clean_mortality(df: pd.DataFrame) -> pd.DataFrame:
    cleaner = DataFrameCleaner(df)

    def handle_nan(_df):
        return _df.dropna(subset=['sex'], how='all')

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
        9: 9
    }

    cleaner.keep_columns(cols_to_keep)

    if cleaner.has_missing_values():
        cleaner.handle_missing_values(func=handle_nan)

    cleaner.rename_columns(cols_names)
    cleaner.assign_dtypes(dtypes_mapping)
    cleaner.convert_values(mapping_sex, 'sex')

    return cleaner.get_data()
