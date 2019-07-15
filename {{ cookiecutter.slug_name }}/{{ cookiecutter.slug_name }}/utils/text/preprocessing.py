# -*- coding: utf-8 -*-
"""Text preprocessing utilities"""

import re

import unidecode

from ..extensions import Singleton
from .case import Pascal2Snake, Snake2Pascal

CLEANER = re.compile(r"[\W]+")
SPACER = re.compile(r"\s+")


class Cleaner(metaclass=Singleton):
    """Clean text"""

    def __init__(self, first_letter=False):
        self._pascaler = None
        self._snaker = None
        self.first_letter = first_letter

    @property
    def pascaler(self):  # pylint: disable=missing-docstring
        if not self._pascaler:
            self._pascaler = Pascal2Snake()

    @property
    def snaker(self):  # pylint: disable=missing-docstring
        if not self._snaker:
            self._snaker = Snake2Pascal(first_letter=self.first_letter)

    def _clean_str(
        self,
        dirty: str,
        lower=True,
        strip=True,
        formatter="snake"
    ) -> str:
        """Cleans a string to utf8 with only alphanumeric

        Args:
            dirty: A dirty string
            lower: Wheter to lowercase.
            strip: Wheter to strip leading & trailing spaces.
            format: Final formatting option .

        Returns:
            The processed version
        """
        english = unidecode.unidecode(dirty)

        lowered = english.lower() if lower else english
        stripped = lowered.strip() if strip else lowered

        if formatter == "snake":
            formatted = self.snaker.convert(stripped)
        elif formatter == "pascal":
            formatted = self.pascaler.convert(stripped)

        alphanumeric = CLEANER.sub("", formatted)
        return alphanumeric

    @classmethod
    def clean_str(cls, dirty:str):
        cleaner = cls()


clean_str = Cleaner.clean_str  # pylint: disable=invalid-name
