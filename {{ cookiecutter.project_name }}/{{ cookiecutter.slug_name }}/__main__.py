#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Entrypoints for {{ cookiecutter.slug_name }}"""

from fire import Fire as _Fire_

from {{ cookiecutter.slug_name }} import scripts

if __name__ == "__main__":
    _Fire_(scripts)
else:
    def _Fire():  # pylint: disable=invalid-name
        return _Fire_(scripts)
