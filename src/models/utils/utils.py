from functools import partial, reduce

import pandas as pd
import numpy as np


def convert_format(series, n=3):
    """Only keep the n first characters of the column"""
    return series.apply(lambda x: x[:n])


def filter_column(df: pd.DataFrame, column: str, elements):
    """


    :param df:
    :param column:
    :param elements:
    :return:
    """
    target = df[column].unique()
    found_elements = find_elements(target, elements)
    dataset = df[df[column].isin(found_elements)]

    return dataset


def find_elements(target, elements):
    """
    Checks if the targets can be found in an arbitrary list of elements.

    :param elements:
    :param target:
    :return:
    """
    mask = np.isin(target, elements)
    found = np.where(mask, target, '')
    valid = [c for c in found if c != '']

    return valid


def groupby_sum(df, index_cols, column):
    """Groups the dataframe by the index columns, and sums the target column and
    returns the result as a dataframe."""

    grouped = df.groupby(index_cols, as_index=False)[column].sum()

    return grouped


def generate_ICD_codes(lower, upper, symbol):
    codes = []
    for i in range(lower, upper + 1, 1):
        if i < 10:
            codes.append(f'{symbol}0{i}')
        else:
            codes.append(f'{symbol}{i}')

    return np.array(codes)


def multi_merge(dfs, on):
    merge = partial(pd.merge, on=on, how='outer')
    dataset = reduce(merge, dfs)

    return dataset