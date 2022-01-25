from functools import partial, reduce
from typing import List

import pandas as pd
import numpy as np


def convert_format(series: pd.Series, n: int = 3) -> pd.Series:
    """Keeps the first n characters of the series."""
    return series.apply(lambda x: x[:n])


def find_elements(target: list, elements: list) -> list:
    """ Returns the found elements. Checks if the target elements can be found in a list of elements.

    Keyword arguments:
        target -- target values to check
        elements -- elements to compare to
    """
    mask = np.isin(target, elements)
    found = np.where(mask, target, '')
    valid = [c for c in found if c != '']

    return valid


def groupby_sum(df: pd.DataFrame, index_cols: list, column: str) -> pd.DataFrame:
    """Groups the dataframe by the index columns, and sums the target column and
    returns the result as a dataframe."""

    grouped = df.groupby(index_cols, as_index=False)[column].sum()

    return grouped


def generate_ICD_codes(lower: int, upper: int, symbol: str) -> np.ndarray:
    """Generates ICD-10 codes with a detail of 3 characters.

    Keyword arguments:
        lower -- lowest code
        upper -- highest code
        symbol -- prefix symbol

    Usage:
        C_codes = generate_ICD_codes(0, 97, 'C')

        It will return generated ICD-10 codes that are classified as Cxx.
        These can be compared with the ac
    """
    codes = []
    for i in range(lower, upper + 1, 1):
        if i < 10:
            codes.append(f'{symbol}0{i}')
        else:
            codes.append(f'{symbol}{i}')

    return np.array(codes)


def multi_merge(dfs: List[pd.DataFrame], on: List[str]) -> pd.DataFrame:
    """Returns a single DataFrame that consists of merged DataFrames."""
    merge = partial(pd.merge, on=on, how='outer')
    dataset = reduce(merge, dfs)

    return dataset
