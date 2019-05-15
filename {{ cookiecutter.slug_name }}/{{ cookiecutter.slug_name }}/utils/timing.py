# -*- coding: utf-8 -*-
"""Decorator for measuring execution time"""
from functools import wraps


def timed_call(
    logger: logging.Logger
) -> Callable:
    """Decorate a function measure execution time.

    Args:
        logger (logging.Logger): Logger to report.

    Returns:
        Callable: The original function with logging
    """

    def real_decorator(function):

        @wraps(function)
        def wrapper(*args, __logger__=logger, **kwargs):

            ts = time.time()

            result = function(*args, **kwargs)

            te = time.time()

            __logger__.info("%s exec time: %s.", function, te)

            return result

        return wrapper

    return real_decorator


def timeit(method):

    @wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print '%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000)
        return result

    return timed
