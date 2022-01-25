from pathlib import Path
from typing import List, Dict
from abc import ABC, abstractmethod

import pandas as pd
import numpy as np

from models.utils import find_elements


class Selector(ABC):

    def __init__(self, file) -> None:
        self.file = file

    @abstractmethod
    def get_selection(self):
        pass


class DataFrameSelector(Selector):

    def __init__(self, df: pd.DataFrame) -> None:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('Expects a pandas DataFrame.')
        super().__init__(df)

        self.selection = {}

    def filter_column(self, column: str, elements: np.ndarray):
        """ Filters a column based on given elements.
        It searches if the unique values of a column are in a list of elements.

        Keyword arguments:
            column -- the column to filter
            elements -- the elements to check the values of the column against
        """
        target = self.file[column].unique()
        found_elements = find_elements(target, elements)
        dataset = self.file[self.file[column].isin(found_elements)]

        return dataset

    def split_dataframe(self, column: str, labels: List[str], selection: List[np.ndarray]):
        """Expects labels as keys and the selection to be the string to select the dataframe on.

        if unique elements are given then it searches for elements found in the selection and the unique list
        """

        for label, selector in zip(labels, selection):
            dataset = self.filter_column(column, selector)
            self.selection[label] = dataset

    def rename_selection(self, column: str, mapping: dict) -> None:
        """Renames the dataframes found in the selection.

        Keyword arguments:
            column -- column to rename
            mapping -- a dictionary with mappings of the name
        """
        if len(self.selection) < 1:
            raise KeyError('Selection is still empty. Add values to the selection by splitting the dataframe.')

        for k, df in self.selection.items():
            self.selection[k] = df.rename(columns={column: mapping[k]})

    def get_selection(self) -> Dict[str, pd.DataFrame]:
        return self.selection
