# -*- coding: utf-8 -*-
"""Decorator for measuring execution time"""
from functools import wraps
from typing import Callable
import time

from {{ cookiecutter.slug_name }} import logger


def timed_call() -> Callable:
    """Decorate a function measure execution time.

    Returns:
        Callable: The original function with logging
    """

    def real_decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            start = time.time()

            result = function(*args, **kwargs)

            end = time.time()

            logger.debug("%s exec time: %s.", function, end-start)

            return result

        return wrapper

    return real_decorator
