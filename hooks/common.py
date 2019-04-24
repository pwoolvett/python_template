#!/usr/bin/env python
"""Common stuff for cookiecutter hooks
"""
import subprocess  # nosec
import os
import sys

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

YES = {"y", "Y", "yes", "Yes", "YES", "yep", "Yep", "YEP"}
NO = {"n", "N", "no", "No", "NO", "nope", "Nope", "NOPE", ""}
BOOL_OPTS = {*YES, *NO}

AUTHOR_NAME = "{{ cookiecutter.author_name }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
DEFAULT_ENV = "{{ cookiecutter.default_env }}"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"
VERSION = "{{ cookiecutter.version }}"
RELEASE = "{{ cookiecutter.release }}"
DESCRIPTION = "{{ cookiecutter.description }}"
MAX_LINE_LENGTH = "{{ cookiecutter.max_line_length }}"
LICENSE = "{{ cookiecutter.license }}"
ADDITIONAL_LIBS = "{{ cookiecutter.additional_libs }}"
TIMEZONE = "{{ cookiecutter.timezone }}"
FORMATTER = "{{ cookiecutter.formatter }}"
LINTER = "{{ cookiecutter.linter }}"
DOCKER = "{{ cookiecutter.docker }}"
TESTING = "{{ cookiecutter.testing }}"
DOCS = "{{ cookiecutter.docs }}"
GIT = "{{ cookiecutter.git }}"
GITHUB_USERNAME = "{{ cookiecutter.github_username }}"
REPO = "{{ cookiecutter.repo }}"
URL = "{{ cookiecutter.url }}"
DEFAULT_ENV = "{{ cookiecutter.default_env }}"
COPYRIGHT = "{{ cookiecutter.copyright }}"
APP_NAME = "{{ cookiecutter.app_name }}"
SLUG_NAME = "{{ cookiecutter.slug_name }}"
PROJECT_SHORT_DESCRIPTION = "{{ cookiecutter.project_short_description }}"
AUTHOR_NAME = "{{ cookiecutter.author_name }}"
AUTHOR_MAIL = "{{ cookiecutter.author_mail }}"
AUTHOR = "{{ cookiecutter.author }}"
AUTHORS = "{{ cookiecutter.authors }}"
MAINTAINER = "{{ cookiecutter.maintainer }}"


def ass_ert(variable, string):
    """Assert with print and sysexit"""
    if not variable:
        print(WARNING + string + TERMINATOR)
        sys.exit(1)


def _exec(string):
    """Send a string to subprocess.call, splitting by spaces

    Note:
        Spaces inside text should be replaced by `___` to avoid extra
        splitting
    """
    cmd_arg = [x.replace("___", " ") for x in string.split(" ")]
    exit_code = subprocess.call(cmd_arg)  # nosec
    if exit_code != 0:
        sys.exit(exit_code)
    return exit_code


def _delete_or_raise(paths_iter):

    if isinstance(paths_iter, str):
        paths_iter = [paths_iter]

    for path in paths_iter:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.rmdir(path)
        else:
            print(WARNING + f"Can't find path: {path}")
