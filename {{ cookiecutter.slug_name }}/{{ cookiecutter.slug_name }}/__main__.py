#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Expose scripts"""

from fire import Fire as _Fire

from {{ cookiecutter.slug_name }}.scripts import *  # noqa: E123

_Fire()
