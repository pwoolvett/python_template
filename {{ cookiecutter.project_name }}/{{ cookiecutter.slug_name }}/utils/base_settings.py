# -*- coding: utf-8 -*-
"""Base stuff for settings - do not get in the way"""

import os
from typing import Type, TypeVar
from pprint import pformat

import json
import jsonschema

from {{ cookiecutter.slug_name }}.utils import _parent_rec

SCHEMA_FILE = _parent_rec(__file__, 3).joinpath("settings-schema.json")

Config = TypeVar("Config", bound="BaseConfig")


class Transformer:  # pylint: disable=invalid-name,
    """Equips with string to native variable converters"""

    _TRUE = {"true"}
    _FALSE = {"false"}

    def __init__(self):

        mapper_dct = {
            "string": str,
            "integer": int,
            "object": dict,
            "array": list,
            "boolean": self.as_bool,
        }

        with open(SCHEMA_FILE, "r") as json_schema_file:
            schema_props = json.load(json_schema_file)["properties"]

        self._mapper = (
            lambda name, value: mapper_dct[schema_props[name]["type"]](value)
            if name in schema_props
            else value
        )

    # @staticmethod
    # def _list_format(string: str) -> bool:
    #     return (
    #         True
    #         if string.startswith("(")
    #         and string.endswith(")")
    #         else False
    #     )

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
        elif var in cls._FALSE:
            return False
        else:
            raise ValueError(
                f"Variable must be `true` or `false`. Received: `{var}`"
            )

    # @staticmethod
    # def as_int(key: str, default: int = -1) -> int:
    #     """Cast to int form bash-style string env"""
    #     return int(os.environ.get(key, default))

    # @staticmethod
    # def as_float(key: str, default: float = -1) -> float:
    #     """Cast to float form bash-style string env"""
    #     return float(os.environ.get(key, default))

    # @staticmethod
    # def as_bytes(key: str, default: bytes = b"") -> bytes:
    #     """Cast to bytes form bash-style string env"""
    #     return bytes(os.environ.get(key, ""), encoding="utf8") or default

    # @classmethod
    # def as_list(cls, key: str, default: list = None) -> list:
    #     """Cast to list form bash-style string env"""
    #     value = os.environ.get(key)
    #     if (not value) or (not cls._list_format(value)):
    #         return default or []

    #     return [part for part in value[1:-1].split(" ")]

    def autocast(self, name, value):
        """Infers value type and casts if it corresponds"""
        return self._mapper(name, value)


TRANSFORMER = Transformer()


class BaseConfig:
    """Boilerplate for config loading and dotenv handling"""

    _excluded_keys = {"__doc__", "__module__"}

    @classmethod
    def __getattribute__(cls, name: str):
        try:
            return TRANSFORMER.autocast(name, os.environ[name])
        except KeyError:
            return type.__getattribute__(cls, name)  # Default behaviour
        except AttributeError:
            raise NotImplementedError(
                f"Attribute {name} not found in class {cls}"
            )

    @classmethod
    def _from_env(  # pylint: disable=invalid-name
        cls: Type[Config],
        env: str,
        DevCls: Type[Config],
        ProdCls: Type[Config],
        TestCls: Type[Config],
        validate: bool = False,
    ) -> Config:
        """Allows instantiation from a single variable"""

        config: Config

        if env == "development":
            config = DevCls()
        elif env == "production":
            config = ProdCls()
        elif env == "testing":
            config = TestCls()
        else:
            raise NotImplementedError(
                "env must be one of ({}).".format(
                    ", ".join(
                        f"´{mode}´"
                        for mode in ("development", "testing", "production")
                    )
                )
                + f" env= {env}"
            )

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
