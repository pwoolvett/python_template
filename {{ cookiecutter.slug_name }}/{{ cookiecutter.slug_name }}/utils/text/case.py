# -*- coding: utf-8 -*-
"""String case conversion"""

import re


class Pascal2Snake:
    """PascalCase to snake_case converter."""

    def __init__(self):
        self.first_cap_re = re.compile("(.)([A-Z][a-z]+)")
        self.all_cap_re = re.compile("([a-z0-9])([A-Z])")

    def convert(self, name):  # pylint: disable=missing-docstring
        splat = self.first_cap_re.sub(r"\1_\2", name)
        return self.all_cap_re.sub(r"\1_\2", splat).lower()


class Snake2Pascal:
    """snake_case to PascalCase converter."""

    def __init__(self, first_letter=False):
        txt = r"(?:^|_)(\w)" if first_letter else r"_([a-z])"
        self.reg = re.compile(txt)

    def _upfirst(self, match):
        return match.group(1).upper()

    def convert(self, words):  # pylint: disable=missing-docstring
        return self.reg.sub(self._upfirst, words)
