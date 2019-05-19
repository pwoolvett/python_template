# coding=utf-8
"""Loads `.env` & equip os.environ with `get_int` and similar methods"""
import os
from pathlib import Path

from dotenv import load_dotenv


DEFAULT_DOTENV_LOCATION: str = Path(__file__).parent.parent.parent.joinpath(
    ".env"
).as_posix()
PRESET_LOCATION: str = os.getenv("DOTENV_LOCATION", DEFAULT_DOTENV_LOCATION)


def init_dotenv(dotenv_location: str = None) -> str:
    """Loc n' load dotenv file

    Sets the location for a dotenv file containig envvars loads its
    contents.

    Args:
        dotenv_location (str, optional): Location of the dotenv file.
        If not set, it will look for `DOTENV_LOCATION` envvar.
        If the envvar does not exist, it will default to ´.env´, located
        in the project's root.
        Defaults to None.

    Raises:
        FileNotFoundError: When the selected location does not
        correspond to a file.

    Returns:
        str: Location of the dotenv file.
    """

    location: str = dotenv_location or PRESET_LOCATION

    if not os.path.isfile(location):
        raise FileNotFoundError(f"`.env` file does not exist in {location}")

    load_dotenv(location)

    return location
