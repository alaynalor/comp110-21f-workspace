"""Utility functions."""
from csv import DictReader
__author__ = "730411361"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Product of list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into a columb-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Return table with first 'n' rows of data."""
    result: dict[str, list[str]] = {}
    if n > len(column_table):
        n = len(column_table)
    for column in column_table:
        n_values: list[str] = []
        i: int = 0
        while i < n:
            n_values.append(column_table[column][i])
            i += 1
        result[column] = n_values
    return result


def select(column_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Return table with indicated columns only."""
    result: dict[str, list[str]] = {}
    for key in columns:
        result[key] = column_table[key]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Return a table of two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in table_one:
        result[key] = table_one[key]
    for key in table_two:
        if key in result:
            i: int = 0
            while i < len(table_two[key]):
                result[key].append(table_two[key][i])
                i += 1
        else:
            result[key] = table_two[key]
    return result


def count(given_values: list[str]) -> dict[str, int]:
    """Return dict with counts of values in input list."""
    result: dict[str, int] = {}
    for item in given_values:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 0
    return result