"""Pandas shortcuts"""

from typing import Callable
from pathlib import Path

from autologging import traced
import pandas as pd

from {{ cookiecutter.slug_name }} import LOGGER


def tsv_reader(*args, **kwargs) -> Callable:
    """wrapper for pd.read_csv used for tab-separated files.

    Returns:
        Callable: pd.read_csv with sep='t'
    """

    return pd.read_csv(*args, sep="\t", **kwargs)


@traced(LOGGER)
def get_reader(file_path: str) -> Callable:
    """Selects a pandas excel/csv reader depending on file extension

    Args:
        file_path (str): The file to Read

    Raises:
        NotImplementedError: If the file is neither a csv nor excel

    Returns:
        callable: The function pandas.read_xx (eg: csv, excel, etc)
    """
    ext = Path(file_path).suffix

    if ext == ".csv":
        reader = pd.read_csv
    elif ext == ".tsv":
        reader = tsv_reader
    elif ext in [".xls", ".xlsx"]:
        reader = pd.read_excel
    else:
        raise NotImplementedError(
            f"file: {file_path} format not supported. ext={ext}"
        )

    return reader


def read(file_path, *args, **kwargs):
    """Load a DataFrame from excel, csv, etc"""

    nrows = kwargs.pop("nrows", 10)

    dataframe = get_reader(file_path)(file_path, *args, nrows=nrows, **kwargs)

    return dataframe
