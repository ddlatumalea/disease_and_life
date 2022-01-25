"""This module contains the aggregator to calculate the sum of specific columns."""

import pandas as pd

from models.utils import groupby_sum


class Aggregator:
    """ Aggregates data together based on indices.

    Keyword arguments:
        df -- a dataset as a pandas DataFrame
    """

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.aggregation = None

    def __handler(self, df) -> None:
        """ Handles data aggregation in such a way that the functions can be called sequentially.

        Keyword argument:
            df -- a pandas DataFrame
        """
        if self.aggregation is None:
            self.aggregation = df
        else:
            self.aggregation = self.aggregation.append(df)

    def calc_aggr(self, by, on, column='', value=None) -> None:
        """ Calculates the aggregate by indices and calculates the sum.

        Keyword arguments:
            by -- the index indices to use to group the DataFrame
            on -- the column that will be summed
            column -- a column to add to the dataframe
            value -- the value to add to the 'column'
        """
        # calculate aggregate and append it to the original
        if not column and not value:
            self.__handler(groupby_sum(self.df, by, on))
            return

        aggr = groupby_sum(self.df, by, on)
        aggr[column] = value

        self.__handler(aggr)

    def get_aggregation(self, sort_by: str) -> pd.DataFrame:
        """Returns the aggregation.

        Keyword arguments:
            sort_by -- the index to sort the values by
        """
        return self.aggregation.sort_values(sort_by).reset_index(drop=True)
