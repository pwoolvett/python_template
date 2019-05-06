# coding=utf-8
"""Settings

Set any and all project variables here.

If you have two version of the project running, they should differ only in
variables set in this file.

Optionally, secret stuff is located in the a .env file, to be loaded here.
"""
import os
from pathlib import Path

from {{ cookiecutter.slug_name }}.utils.io import nth_parent
from {{ cookiecutter.slug_name }}._meta.log import LogLevel, LogMode
from {{ cookiecutter.slug_name }}._meta.base_settings import BaseConfig


class Config(BaseConfig):
    """All common values are defined here"""

    BASEPATH: str = nth_parent(__file__, 2).as_posix()
    """Absolute path to the project directory"""

    PKG_PATH: str = Path(BASEPATH).joinpath("project_sample").as_posix()
    """Absolute path to the package directory"""

    DATA: str = Path(BASEPATH).joinpath("data").as_posix()
    """Absolute path to the package directory"""

    ENV: str = os.environ["ENV"]
    """Execution mode of the project

    Must be one of: `production`, `development`, `testing`
    """

    DEBUG: bool = True
    """Set to True to enable debugging"""

    TESTING: bool = False
    """Set to True to enable testing mode"""

    LOG_LEVEL: LogLevel = LogLevel.INFO
    """Defines the logging level of the Application"""

    LOG_MODE: LogMode = LogMode.CONSOLE | LogMode.ERROR_FILE
    """Define allowed destinations for logs"""


class ProductionConfig(Config):
    """Production-specific values are defined here"""

    ENV = "production"
    DEBUG = False
    TESTING = False

    LOG_LEVEL = LogLevel.TRACE
    LOG_MODE = LogMode.ERROR_FILE | LogMode.TRACE_FILE


class DevelopmentConfig(Config):
    """Development-specific values are defined here"""

    ENV = "development"
    DEBUG = True
    TESTING = False

    LOG_LEVEL = LogLevel.TRACE
    LOG_MODE = LogMode.CONSOLE | LogMode.ERROR_FILE


class TestingConfig(Config):
    """Testing-specific values are defined here"""

    ENV = "testing"
    DEBUG = True
    TESTING = True

    LOG_LEVEL = LogLevel.TRACE
    LOG_MODE = LogMode.CONSOLE


def init_settings() -> 'BaseConfig':
    """Initializes configuration from envvar ´ENV´

    Returns:
        BaseConfig: A schema-validated configuration
    """

    env = os.environ["ENV"]

    config = Config.from_env(env)

    return config
