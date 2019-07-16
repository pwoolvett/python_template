# -*- coding: utf-8 -*-
"""Custom Python extensions and classes"""


class Singleton(type):
    """"A metaclass to equip singleton-like behavior."""

    _storage = {}
    """singleton classes global storage"""

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._storage[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._storage[cls]
