#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Expose scripts"""
import sys as _sys

from fire import Fire as _Fire_

from {{ cookiecutter.slug_name }}.scripts import *  # noqa: E123

if __name__ == "__main__":
    _Fire_(_sys.modules[__name__])
else:
    def _Fire(*a, **kw):
        return _Fire_(_sys.modules[__name__])

