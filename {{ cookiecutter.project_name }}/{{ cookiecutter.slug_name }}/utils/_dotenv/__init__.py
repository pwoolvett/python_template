# coding=utf-8
"""Loads `.env` & equip os.environ with `get_int` and similar methods"""
import os
from pathlib import Path
from dotenv import load_dotenv

from {{ cookiecutter.slug_name }}.utils import _parent_rec


def init_dotenv():
    dotenv_location = os.getenv(
        "DOTENV_LOCATION", _parent_rec(__file__, 4).joinpath(".env")
    )

    if not os.path.isfile(dotenv_location):
        raise FileNotFoundError(
            f"`.env` file does not exist in {dotenv_location}"
        )

    load_dotenv(dotenv_location)

    return dotenv_location


DOTENV_LOCATION = init_dotenv()
