# -*- coding: utf-8 -*-
"""Boilerplate used for easy acces to files"""
from .dotenv_ import init_dotenv
from .log import create_logger, LogLevel, LogMode
from .base_settings import BaseConfig
from .metadata import Metadata

DOTENV_LOCATION = init_dotenv()


__all__ = [
    "DOTENV_LOCATION",
    "create_logger",
    "Metadata",
    "LogLevel",
    "LogMode",
    "BaseConfig",
]
