"""Settings

Set any and all project variables here.

If you have two version of the project running, they should differ only in
variables set in this file.

Optionally, secret stuff is located in the a .env file, to be loaded here.
"""

from dotenv import load_dotenv
import os


DOTENV_LOCATION = os.getenv("DOTENV_LOCATION", ".env")
"""Location of the environment variales file

By default, a :code:`.env` file is expected in the project's root.
"""
load_dotenv(DOTENV_LOCATION)
