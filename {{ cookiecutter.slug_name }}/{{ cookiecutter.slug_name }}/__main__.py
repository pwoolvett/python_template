#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Expose scripts"""

import fire

from {{ cookiecutter.slug_name }}.scripts import *  # noqa: E123

fire.Fire()
