# -*- coding: utf-8 -*-
"""Base stuff for settings - do not get in the way"""

from typing import Type
from pprint import pformat

from pydantic import BaseSettings, ValidationError


class BaseConfig(BaseSettings):
    """Boilerplate for config loading and dotenv handling"""

    class Config:  # pylint: disable=missing-docstring,
        env_prefix = ""

    @classmethod
    def from_env(
        cls: Type["BaseConfig"], env: str, **cls_data
    ) -> "BaseConfig":
        """Allows instantiation from a single variable"""

        config_cls: Type["BaseConfig"] = {
            child.__fields__["ENV"].default: child
            for child in cls.__subclasses__()
        }[env]

        try:
            config = config_cls(**cls_data)
        except ValidationError as err:
            print(err.json())
            raise err

        return config

    def to_str(self, dict_kw=None, **dumps_kw) -> str:
        """Formats the dictionary version as a string

        Args:
            dict_kw ([dict], optional): kwargs for `BaseModel.dict`.
                Defaults to `{}`}.
            dumps_kw : optional kwargs forwarded to `pprint.pformat`.

        Returns:
            str: The formatted string version of the class as a
                dictionary.
        """

        dict_kw = dict_kw or {}

        return pformat(self.dict(**dict_kw), **dumps_kw)
