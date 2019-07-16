# !/usr/bin/env python
"""Execute conditional processes depending con cookiecutter variables
"""
import os
import sys
from shutil import copy2 as copy, rmtree
import subprocess  # nosec
from functools import wraps

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
SLUG_NAME = "{{ cookiecutter.slug_name }}"
PROJECT_SHORT_DESCRIPTION = "{{ cookiecutter.project_short_description }}"
AUTHOR_NAME = "{{ cookiecutter.author_name }}"
AUTHOR_MAIL = "{{ cookiecutter.author_mail }}"
AUTHOR = "{{ cookiecutter.author }}"
MAINTAINER = "{{ cookiecutter.maintainer }}"


def can_fail(function) -> callable:
    """Decorator to report exceptions instead of raising

    Args:
        function (callable): the function to decorate.
    
    Returns:
        callable: The decorated function.
    """

    @wraps(function)
    def wrapped(*a, **kw):
        try:
            return function(*a, **kw)
        except BaseException as err:
            print(WARNING + str(err) + TERMINATOR)
            return 1

    return wrapped


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
            rmtree(path)
        else:
            print(WARNING + f"Can't find path: {path}")


def create_dotenv():
    """Create dotenv file.

    Uses .env.dist as a base, and sets `ENV=cookiecutter.default_env`
    """

    print(INFO + "Creating and configuring `.env` file" + TERMINATOR)
    copy(".env.dist", ".env")

    with open(".env", "a+") as dotenv:
        dotenv.write(f"ENV={DEFAULT_ENV}\n")

    print(SUCCESS + "`.env` file created and cofigured" + TERMINATOR)


def config_license():
    """May delete license-related files"""

    print(INFO + "Configuring project license" + TERMINATOR)

    file_names = []
    if "GPLv3" not in LICENSE:
        file_names.append("COPYING")

    if LICENSE in NO:
        file_names.extend(("CONTRIBUTORS.txt", "LICENSE"))

    _delete_or_raise(file_names)

    print(SUCCESS + "Project license configured" + TERMINATOR)


def config_docker():
    """Sets up docker and docker-compose, if required"""

    print(INFO + "Configuring docker" + TERMINATOR)

    if DOCKER not in NO:
        # TODO: Additional configuration here
        pass
    else:
        file_names = []
        if "dockerfile" not in DOCKER:
            file_names.append("Dockerfile")

        if "docker-compose" not in DOCKER:
            file_names.append("docker-compose.yml")

        _delete_or_raise(file_names)

    print(SUCCESS + "Docker configured" + TERMINATOR)


def config_tests():
    """Sets up testing: pytest, behave, hypothesis, etc, if required"""

    print(INFO + "Setting up testing" + TERMINATOR)

    if TESTING in NO:
        _delete_or_raise("tests")
    else:
        file_names, dir_names = [], []
        hyp_files = (
            os.path.join("tests", "features", "gherkin_hypothesis.feature"),
            os.path.join(
                "tests", "features", "steps", "gherkin_hypothesis.py"
            ),
            os.path.join("tests", "unit", "test_002_hypothesis.py"),
        )

        beh_folders = (os.path.join("tests", "features"),)

        if "hypothesis" not in TESTING:
            file_names.extend(hyp_files)

        if "behave" not in TESTING:
            dir_names.extend(beh_folders)

        to_delete = (*file_names, *dir_names)
        _delete_or_raise(to_delete)

    print(SUCCESS + "Testing setup completed" + TERMINATOR)


def config_docs():
    """Sets up docs and sphinx, if required"""

    print(INFO + "Setting up documentation" + TERMINATOR)

    if DOCS in NO:
        _delete_or_raise("docs")

    print(SUCCESS + "Documentation setup completed" + TERMINATOR)


def configure_git():
    """Configures or deletes git+github stuff"""

    print(INFO + "Setting up GIT" + TERMINATOR)

    if GIT in NO:
        # TODO: Additional configuration here
        pass
    else:
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

    print(SUCCESS + "GIT setup completed" + TERMINATOR)


@can_fail
def create_virtualenv():
    """install virtualenv into ./.venv/ and run poetry install"""

    print(
        INFO
        + "Configuring virtual environment and installing libraries"
        + TERMINATOR
    )
    _exec("tox -e venv")
    print(
        INFO
        + "Virtual environment configured and libraries installed"
        + TERMINATOR
    )


@can_fail
def update_dependencies():
    """Update dependencies defined in `pyproject.toml` and `poetry.lock`"""

    print(INFO + "Updating dependencies" + TERMINATOR)
    _exec("poetry update --no-interaction")
    print(INFO + "Done updating dependencies" + TERMINATOR)


@can_fail
def run_tests():
    """Run all tests as defined in `tox.ini`"""

    print(INFO + "Running tox tests" + TERMINATOR)
    _exec("tox -- --runslow")
    print(INFO + "tox tests ran and passed!" + TERMINATOR)


def main():
    """Runs all checks, removes useless files, initializes project"""
    create_dotenv()
    config_license()
    config_docker()
    config_tests()
    config_docs()
    configure_git()
    create_virtualenv()
    update_dependencies()
    run_tests()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)

    import this  # noqa


if __name__ == "__main__":
    main()
