#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Entrypoints for {{ cookiecutter.slug_name }}"""
import sys as _sys

from fire import Fire as _Fire_

from {{ cookiecutter.slug_name }}.scripts import *  # pylint: disable=wildcard-import, unused-wildcard-import

if __name__ == "__main__":
    _Fire_()
else:
    def _Fire():  # pylint: disable=invalid-name
        return _Fire_(_sys.modules[__name__])
