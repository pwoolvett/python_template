#!/usr/bin/env python
"""Execute conditional processes depending con cookiecutter variables
"""
import os
import sys
from shutil import copy2 as copy
import subprocess  # nosec

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

YES = {"y", "Y", "yes", "Yes", "YES", "yep", "Yep", "YEP"}
NO = {
    "n",
    "N",
    "no",
    "No",
    "NO",
    "nope",
    "Nope",
    "NOPE",
    "none",
    "None",
    "NONE",
    "",
}
BOOL_OPTS = {*YES, *NO}

AUTHOR_NAME = "{{ cookiecutter.author_name }}"
DEFAULT_ENV = "{{ cookiecutter.default_env }}"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"
VERSION = "{{ cookiecutter.version }}"
RELEASE = "{{ cookiecutter.release }}"
DESCRIPTION = "{{ cookiecutter.description }}"
MAX_LINE_LENGTH = "{{ cookiecutter.max_line_length }}"
LICENSE = "{{ cookiecutter.license }}"
ADDITIONAL_LIBS = "{{ cookiecutter.additional_libs }}"
TIMEZONE = "{{ cookiecutter.timezone }}"
FORMATTER = "{{ cookiecutter.formatter }}"
LINTER = "{{ cookiecutter.linter }}"
DOCKER = "{{ cookiecutter.docker }}"
TESTING = "{{ cookiecutter.testing }}"
DOCS = "{{ cookiecutter.docs }}"
GIT = "{{ cookiecutter.git }}"
GITHUB_USERNAME = "{{ cookiecutter.github_username }}"
REPO = "{{ cookiecutter.repo }}"
URL = "{{ cookiecutter.url }}"
DEFAULT_ENV = "{{ cookiecutter.default_env }}"
COPYRIGHT = "{{ cookiecutter.copyright }}"
APP_NAME = "{{ cookiecutter.app_name }}"
SLUG_NAME = "{{ cookiecutter.slug_name }}"
PROJECT_SHORT_DESCRIPTION = "{{ cookiecutter.project_short_description }}"
AUTHOR_NAME = "{{ cookiecutter.author_name }}"
AUTHOR_MAIL = "{{ cookiecutter.author_mail }}"
AUTHOR = "{{ cookiecutter.author }}"
AUTHORS = "{{ cookiecutter.authors }}"
MAINTAINER = "{{ cookiecutter.maintainer }}"


def ass_ert(variable, string):
    """Assert with print and sysexit"""
    if not variable:
        print(WARNING + string + TERMINATOR)
        sys.exit(1)


def _exec(string):
    """Send a string to subprocess.call, splitting by spaces

    Note:
        Spaces inside text should be replaced by `___` to avoid extra
        splitting
    """
    cmd_arg = [x.replace("___", " ") for x in string.split(" ")]
    exit_code = subprocess.call(cmd_arg)  # nosec
    if exit_code != 0:
        sys.exit(exit_code)
    return exit_code


def _delete_or_raise(paths_iter):

    if isinstance(paths_iter, str):
        paths_iter = [paths_iter]

    for path in paths_iter:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.rmdir(path)
        else:
            print(WARNING + f"Can't find path: {path}")


def create_dotenv():
    """Create dotenv file.

    Uses .env.dist as a base, and sets `ENV=cookiecutter.default_env`
    """
    copy(".env.dist", ".env")

    with open(".env", "a+") as dotenv:
        dotenv.write(f"ENV={DEFAULT_ENV}\n")


def config_license():
    """May delete license-related files"""

    file_names = []

    if "GPLv3" not in LICENSE:
        file_names.append("COPYING")

    if not LICENSE:
        file_names.extend(("CONTRIBUTORS.txt", "LICENSE"))
        _delete_or_raise(file_names)
        return


def config_docker():
    """Sets up docker and docker-compose, if required"""

    if DOCKER not in NO:
        # TODO: Additional configuration here
        return

    file_names = []
    if "dockerfile" not in DOCKER:
        file_names.append("Dockerfile")

    if "docker-compose" not in DOCKER:
        file_names.append("docker-compose.yml")

    _delete_or_raise(file_names)


def config_tests():
    """Sets up testing: pytest, behave, hypothesis, etc, if required"""

    if TESTING in NO:
        _delete_or_raise("tests")
        return

    file_names, dir_names = [], []
    hyp_files = (
        os.path.join("tests", "features", "gherkin_hypothesis.feature"),
        os.path.join("tests", "features", "steps", "gherkin_hypothesis.py"),
        os.path.join("tests", "unit", "test_002_hypothesis.py"),
    )

    beh_folders = (os.path.join("tests", "features"),)

    if "hypothesis" not in TESTING:
        file_names.extend(hyp_files)

    if "behave" not in TESTING:
        dir_names.extend(beh_folders)

    to_delete = (*file_names, *dir_names)
    _delete_or_raise(to_delete)


def config_docs():
    """Sets up docs and sphinx, if required"""

    if DOCS in NO:
        _delete_or_raise("docs")


def configure_git():
    """Configures or deletes git+github stuff"""

    if GIT in NO:
        return

    commands = []
    if "git" in GIT:
        commands.extend(
            ["git init", "git add .", 'git commit -m "initial___commit"']
        )
    if "github" in GIT:
        commands.extend(
            [
                f"git remote add origin {REPO}",
                "git push --set-upstream origin master",
            ]
        )

    for command in commands:
        _exec(command)


def create_virtualenv():
    """install virtualenv into ./.venv/ and run poetry install"""
    _exec("tox -e venv")


def main():
    """Runs all checks, removes useless files, initializes project"""
    create_dotenv()
    config_license()
    config_docker()
    config_tests()
    config_docs()
    configure_git()
    # create_virtualenv()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
