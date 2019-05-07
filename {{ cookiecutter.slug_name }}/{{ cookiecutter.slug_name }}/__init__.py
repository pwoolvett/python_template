# coding=utf-8
"""{{ cookiecutter.slug_name }} documentation

.. versionadded:: {{ cookiecutter.version }}
   Initial version.

"""

from {{ cookiecutter.slug_name }}._meta.log import create_logger
from {{ cookiecutter.slug_name }}._meta.dotenv_ import DOTENV_LOCATION
from {{ cookiecutter.slug_name }}._meta.metadata import Metadata
from {{ cookiecutter.slug_name }} import settings

S = settings.init_settings()
__meta__ = Metadata()
logger = create_logger(  # pylint: disable=invalid-name
    S.LOG_LEVEL, S.LOG_MODE, logs_folder=S.LOG_STORAGE
)

logger.info("Using variables from `%s`", DOTENV_LOCATION)
logger.debug("Full config :\n`%s`", S.to_str(compact=False, indent=2))
