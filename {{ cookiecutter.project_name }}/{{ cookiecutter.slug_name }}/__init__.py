# coding=utf-8
"""{{ cookiecutter.slug_name }} documentation

.. versionadded:: {{ cookiecutter.version }}
   Initial version.

"""

from {{ cookiecutter.slug_name }}.utils._log import create_logger
from {{ cookiecutter.slug_name }}.utils._dotenv import DOTENV_LOCATION
from {{ cookiecutter.slug_name }} import settings

S = settings.init_settings()
logger = create_logger(S.LOG_LEVEL, S.LOG_MODE)  # pylint: disable=invalid-name

logger.info("Using variables from `%s`", DOTENV_LOCATION)
logger.debug("Full config :\n`%s`", S.to_str(compact=False, indent=2))
