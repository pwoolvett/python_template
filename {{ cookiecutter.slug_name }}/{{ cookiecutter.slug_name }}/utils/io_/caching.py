# -*- coding: utf-8 -*-
"""Caching functions."""

import pickle  # nosec
from functools import wraps
from typing import Callable

from pathlib import Path

from {{ cookiecutter.slug_name }} import LOGGER

PICKLE_EXTENSIONS = {".pickle", ".pkl"}


def define_save_load(location):
    """Save and load are noops if location is not pickle."""

    if any(location.endswith(ext) for ext in PICKLE_EXTENSIONS):

        def save(location_, result_):
            with open(location_, "wb") as pkl:
                pickle.dump(result_, pkl)
            LOGGER.info("%s Saved", location)

        def load(location_,):
            with open(location_, "rb") as pkl:
                result = pickle.load(pkl)  # nosec
            LOGGER.info("%s Loaded", location_)
            return result

    else:

        def save(location_, result_):  # pylint: disable=unused-argument,
            LOGGER.info(
                "%s without pickle extension. Skipping Saving", location_
            )

        def load(location_):
            LOGGER.info(
                "%s Already exists without pickle ext. Skipping Loading",
                location_,
            )

    return save, load


def cached_output(location: str, force: bool = False) -> Callable:
    """Decorate a function to store its result as a pickle.

    Appends two additional dunder kwargs: `__location__` & `__force__`.

    Args:
        location (str): Where to store the cached result.
        force (bool, optional): Whether to call the function even if a
        cached result already exists. Defaults to False.

    Returns:
        Callable: The original function, with two extra arguments
    """

    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, __location__=location, __force__=force, **kwargs,):

            save, load = define_save_load(__location__)

            if __force__ or not Path(__location__).exists():
                result = function(*args, **kwargs)
                save(__location__, result)
            else:
                try:
                    result = load(__location__)

                except (EOFError, pickle.UnpicklingError) as error:
                    LOGGER.error(
                        "Error %s in %s. Calling again ...",
                        type(error),
                        __location__,
                    )

                    result = function(*args, **kwargs)
                    save(__location__, result)
            return result

        return wrapper

    return real_decorator
