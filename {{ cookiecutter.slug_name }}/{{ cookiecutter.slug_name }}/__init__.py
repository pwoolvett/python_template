# coding=utf-8
"""{{ cookiecutter.slug_name }} documentation

.. versionadded:: {{ cookiecutter.version }}
   Initial version.

"""

from {{ cookiecutter.slug_name }}._meta import DOTENV_LOCATION, create_logger, Metadata
from {{ cookiecutter.slug_name }}.settings import init_settings

S = init_settings()
__meta__ = Metadata()
logger = create_logger(  # pylint: disable=invalid-name
    S.LOG_LEVEL, S.LOG_MODE, logs_folder=S.LOG_STORAGE
)

logger.info("Using variables from `%s`", DOTENV_LOCATION)
logger.debug("Full config :\n`%s`", S.to_str(compact=False, indent=2))
