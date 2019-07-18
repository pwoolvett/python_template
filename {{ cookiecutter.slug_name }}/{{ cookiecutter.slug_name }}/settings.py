# coding=utf-8
"""Set any and all {{ cookiecutter.project_name }} variables here.

If you have two version of the project running, they should differ only
in variables set in this file.

Optionally, secret stuff is located in the a .env file, to be loaded
here.

"""

from petri import BaseSettings as PetriBaseSettings, LogMode, LogLevel


class BaseSettings(PetriBaseSettings):
    """Define project settings for {{ cookiecutter.slug_name }}.

    Use pydantic style. Already included in `PetriBaseSettings`: ENV,
    APP, BASEPATH, PKG_PATH, DATA, LOG_LEVEL, LOG_MODE, LOG_STORAGE

    Of these, the following have defaults: APP, BASEPATH, PKG_PATH,
    DATA, LOG_STORAGE,

    This means `ENV` must be set in an env. var, and both LOG_LEVEL and
    LOG_MODE do not have defaults.

    """


class ProdSettings(BaseSettings):  # pylint: disable=missing-docstring
    ENV = "production"
    LOG_LEVEL = LogLevel.TRACE
    LOG_MODE = LogMode.ERROR_FILE


class DevSettings(BaseSettings):  # pylint: disable=missing-docstring
    ENV = "development"
    LOG_LEVEL = LogLevel.INFO
    LOG_MODE = LogMode.CONSOLE | LogMode.ERROR_FILE


class TestSettings(BaseSettings):  # pylint: disable=missing-docstring
    ENV = "testing"
    LOG_LEVEL = LogLevel.ERROR
    LOG_MODE = LogMode.CONSOLE
