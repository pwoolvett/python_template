#!/usr/bin/env python
"""Execute conditional processes depending con cookiecutter variables
"""
import os
from shutil import copy2 as copy

from .common import (
    _exec,
    _delete_or_raise,
    NO,
    SUCCESS,
    TERMINATOR,
    DEFAULT_ENV,
    LICENSE,
    DOCKER,
    TESTING,
    DOCS,
    GIT,
    REPO,
)


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
    create_virtualenv()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
