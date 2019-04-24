"""Settings

Set any and all project variables here.

If you have two version of the project running, they should differ only in
variables set in this file.

Optionally, secret stuff is located in the a .env file, to be loaded here.
"""
import os

BASEPATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PKG_PATH = os.path.join(BASEPATH, "{{ cookiecutter.slug_name }}")
DATA = os.path.join(BASEPATH, "data")
