===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.description }}

Sample Usage
------------

Show available scripts::

  $ python {{ cookiecutter.project_name }}

Requirements
------------

- User requirements

   + python>={{ cookiecutter.python_version }}
   + poetry (recommended)

- Development requirements

   + tox
   + docker >=18.09
   + docker-compose >= 1.22


Installation
------------

- User:

   + Install {{ cookiecutter.app_name }} by running::

      $ poetry install --no-dev -v

   + Alternatively, create a virtualenv and manually install all the requirements
     listed in `./pyproject.toml` -> `tool.poetry.dependencies`

- Development:

   + Create virtualenv and install install {{ cookiecutter.app_name }} (with
     development libs) by running::

      $ tox -e venv # internally this runs `poetry install -v`

   + Alternatively, create a virtualenv and manually install all the requirements
     listed in `./pyproject.toml` -> `tool.poetry.dependencies` and
     `tool.poetry.dev-dependencies`.


Testing
-------

Without virtualenv activated (!), run `tox` in the project root. This runs the following:

+ Unit tests and developer-designed tests:

   - located in tests/unit
   - run with pytest

+ Integration testing:

   - located in tests/integration
   - might use docker-compose
   - run with pytest

+ User stories testing with behave and docker-compose:

   - located in tests/features
   - might use docker-compose
   - run with behave

Contribute
----------

- Issue Tracker: {{ cookiecutter.repo }}/issues
- Source Code: {{ cookiecutter.repo }}

Support
-------

If you are having issues, please let us know.
Contact us at: {{ cookiecutter.project_name }}

License
-------

{{ cookiecutter.license }}
