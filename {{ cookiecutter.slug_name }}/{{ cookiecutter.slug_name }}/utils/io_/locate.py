"""Default module locations decorator"""

from typing import Callable
from pathlib import Path
from functools import wraps

from {{ cookiecutter.slug_name }} import logger


def get_file_path(func_name, locations, **kwargs):
    """defines a default file location"""
    if "file_path" in kwargs:
        logger.debug("file_path %s in kwargs", kwargs["file_path"])
    else:

        for default_location in locations:
            logger.info(
                "Added `file_path=%s` to kwargs in `%s` call",
                default_location,
                func_name,
            )
            kwargs["file_path"] = default_location
            break

    file_path = kwargs["file_path"]

    if not Path(file_path).exists:
        raise FileNotFoundError(file_path)

    return kwargs


def requires_file(locations: tuple) -> Callable:
    """Decorate a function to add `locations` with default values.

    Appends an additional dunder kwarg: `locations`.

    Args:
        locations (tuple): Where to look for the files.

    Returns:
        Callable: The original function, with two extra arguments.
    """

    def real_decorator(function):
        @wraps(function)
        def wrapper(
            *args, __locations__=locations, **kwargs
        ):

            kwargs.update(
                **get_file_path(
                    function.__name__, __locations__, **kwargs
                )
            )

            result = function(*args, **kwargs)

            return result

        return wrapper

    return real_decorator
