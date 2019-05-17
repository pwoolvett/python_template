# -*- coding: utf-8 -*-
"""Text preprocessing utilities"""

import re

import unidecode


CLEANER = re.compile(r"[\W]+")
JOINER = re.compile(r"\s+")


def clean_str(dirty: str) -> str:
    """Cleans a string to utf8 with only alphanumeric

    Args:
        dirty (str): A dirty string

    Returns:
        str: The bleached version
    """
    english = unidecode.unidecode(dirty)
    lowered = english.lower().strip()
    single = lowered.replace(" ", "_")
    alphanumeric = CLEANER.sub("", single)

    return alphanumeric
