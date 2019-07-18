# coding=utf-8
"""{{ cookiecutter.project_name }} documentation.

.. versionadded:: {{ cookiecutter.version }}

   Initial version.

"""

from petri import BaseSettings, initialize, LogMode, LogLevel

from . import settings

__meta__, DOTENV_LOCATION, SETTINGS, LOGGER, _ = initialize(
    __file__, "{{ cookiecutter.slug_name }}"
)

LOGGER.info("Using variables from `%s`", DOTENV_LOCATION)
LOGGER.debug("Full config :\n`%s`", SETTINGS.to_str(compact=False, indent=2))
