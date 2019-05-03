# -*- coding: utf-8 -*-
"""Base stuff for settings - do not get in the way"""

import os
from typing import Type, TypeVar
from pprint import pformat

import json
import jsonschema

from {{ cookiecutter.slug_name }}.utils.io import nth_parent

SCHEMA_FILE = nth_parent(__file__, 3).joinpath("settings-schema.json")

Config = TypeVar("Config", bound="BaseConfig")


class Transformer:  # pylint: disable=invalid-name,
    """Several string_to_native variable converters using jsonschema"""

    _TRUE = {"true"}
    _FALSE = {"false"}

    def __init__(self):

        mapper_dct = {
            "boolean": self.as_bool,
            "array": self.as_list,
            "integer": int,
            "string": str,
            "number": float,
        }

        with open(SCHEMA_FILE, "r") as json_schema_file:
            schema_props = json.load(json_schema_file)["properties"]

        self._mapper = (
            lambda name, value: mapper_dct[schema_props[name]["type"]](value)
            if name in schema_props
            else value
        )

    @classmethod
    def as_bool(cls, var: str) -> bool:
        """Cast to bool form bash-style string env

        Args:
            var (str): Value of the variable

        Returns:
            bool: The python-native boolean
        """
        if var in cls._TRUE:
            return True

        if var in cls._FALSE:
            return False
        raise ValueError("Variable must be `true` or `false`. " + f"Received: `{var}`")

    @classmethod
    def as_list(cls, var: str) -> list:
        """Cast to list form bash-style string env"""

        if not (var[1] == "(" and var[-1] == ")"):
            raise ValueError("variable {} not in bash array format.")

        return [part for part in var[1:-1].split(" ")]

    def autocast(self, name, value):
        """Infers value type and casts if it corresponds"""
        return self._mapper(name, value)


TRANSFORMER = Transformer()


class BaseConfig:
    """Boilerplate for config loading and dotenv handling"""

    _excluded_keys = {"__doc__", "__module__", "from_env", "to_dict", "to_str"}

    @property
    def ENV(self):  # pylint: disable=invalid-name
        """The environment to work in: dev/test/prod"""
        raise NotImplementedError

    @classmethod
    def __getattribute__(cls, name: str):
        try:
            return TRANSFORMER.autocast(name, os.environ[name])
        except KeyError:
            return type.__getattribute__(cls, name)  # Default behaviour
        except AttributeError:
            raise NotImplementedError(f"Attribute {name} not found in class {cls}")

    @classmethod
    def from_env(cls: Type[Config], env: str, validate: bool = False) -> Config:
        """Allows instantiation from a single variable"""

        config_cls: Type[Config] = {
            str(child.ENV): child for child in cls.__subclasses__()
        }[env]

        config = config_cls()

        if validate:
            schema = json.load(open(SCHEMA_FILE, "r"))
            jsonschema.validate(config.to_dict(), schema)

        return config

    @classmethod
    def to_dict(cls):
        """Create dictionary representation of the class"""
        return {
            attr: cls.__getattribute__(attr)
            for attr in dir(cls)
            if attr not in cls._excluded_keys and not attr.startswith("_")
        }

    @classmethod
    def to_str(cls, **dumps_kw) -> str:
        """Formats the dictionary version as a string

        Args:
            dumps_kw : optional kwargs forwarded to `pprint.pformat`.

        Returns:
            str: The formatted string version of the class as a
            dictionary.
        """
        return pformat(cls.to_dict(), **dumps_kw)
