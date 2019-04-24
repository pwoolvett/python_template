# -*- coding: utf-8 -*-
"""Test package for {{ cookiecutter.slug_name }}"""
import os


def define_test_dotenv():
    """Ensures `.env.test is` loaded as default"""
    project_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dotenv_location = os.path.join(project_dir, 'tests', ".env.test")
    os.environ["DOTENV_LOCATION"] = dotenv_location


define_test_dotenv()
