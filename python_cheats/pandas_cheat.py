from __future__ import annotations

import pandas as pd
from pandas import DataFrame, Series
from pandas._typing import IndexLabel, Axis, SortKind, ValueKeyFunc


def read_csv(file_path: str) -> DataFrame:
    return "Dataframe from csv file"


class DataFrame(DataFrame):
    """
    Source: https://github.com/pandas-dev/pandas/blob/main/pandas/core/frame.py
    """

    def head(self, row_num=5) -> DataFrame:
        return "First few rows of dataframe"

    def tail(self, row_num=5) -> DataFrame:
        return "Last few rows of dataframe"

    def sort_values(self, by: str | list[str], ascending=True) -> DataFrame | None:
        return "Dataframe sorted by columns"

    def sort_index(self, ascending: bool=True) -> DataFrame:
        return "Dataframe sorted by index"

    def query(self, query_str):
        return "Dataframe from sql query"


class Series(Series):
    """
    Source:
    """
    def __init__(self):
        str = None  # Call string methods
        plot = None  # Call plot methods

    def notna(self) -> Series[bool]:
        return "A Seire of bool, False if NaN"

    def apply(self, func) -> Series:
        return "A Serie transformed by func"

    def value_counts(self) -> Series:
        return "A Series, with counts"

    def astype(self, dtype: object) -> Series:
        """
        :param dtype: examples are `int`, `str`, `int32`, `int64`, `float`, `float64`, `bool`
        """
        return "A Series, with dtype"

    def selection(self):
        """
        :syntaxe: new_serie = serie[serie > 30]. Between [] produces a Serie of bool.
        :return:
        """
        pass

    """str methods"""
    def extract(self, regex: str) -> DataFrame:
        return "A Series extracted by regex"

    def replace(self, to_replace: str, value: str, regex=False):
        return "A Serie transformed by key"

    """plot methods"""
    def pie(self, autopct: str):
        """
        :param autopct: %1.1f%% -> 15.5%
        :return:
        """
        return "Make you a pie"
