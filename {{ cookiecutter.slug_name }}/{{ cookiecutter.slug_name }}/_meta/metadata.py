# -*- coding: utf-8 -*-
"""Meta-info for the project, as read from`pyproject.toml`"""
import toml

from {{ cookiecutter.slug_name }}.utils.io import nth_parent


class Metadata:  # pylint: disable=too-few-public-methods,
    """Lazy-loader for attributes found in `[tool.poetry]`"""

    def __init__(self):
        self.pyproject_file = nth_parent(__file__, 3).joinpath("pyproject.toml")
        if not self.pyproject_file.exists():
            raise FileNotFoundError(self.pyproject_file)  # pragma: no cover

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pyproj_toml = toml.load(self.pyproject_file)["tool"]["poetry"]
            self.__dict__.update({k: v for k, v in pyproj_toml.items()})

            if name not in self.__dict__:
                raise AttributeError(f"{name} not in {self.pyproject_file}")

            return self.__getattribute__(name)
