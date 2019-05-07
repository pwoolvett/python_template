#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Entrypoints for {{ cookiecutter.slug_name }}"""

from fire import Fire as _Fire_

from {{ cookiecutter.slug_name }} import scripts


def main(): # pylint: disable=missing-docstring
    _Fire_(scripts)

if __name__ == "__main__":
    main()
