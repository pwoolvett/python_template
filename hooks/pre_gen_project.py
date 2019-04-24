#!/usr/bin/env python
"""Executed before cookiecutter to validate inputs"""
from .common import (
    ass_ert,
    TERMINATOR,
    SUCCESS,
    AUTHOR_NAME,
    PROJECT_SLUG,
)

ass_ert(
    PROJECT_SLUG.isidentifier(),
    f"'{PROJECT_SLUG}' project slug is not a valid Python identifier.",
)

ass_ert("\\" not in AUTHOR_NAME, "Don't include backslashes in author name.")


# TODO: Add missing asserts for cookiecutter config
# For example, if github is enabled, also require github username
# <pwoolvett 2019-04-24T14:59:34>

print(SUCCESS + "pre-gen hook complete" + TERMINATOR)
