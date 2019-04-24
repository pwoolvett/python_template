===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.description }}

Sample Usage
------------

Show available scripts::

  $ python {{ cookiecutter.slug_name }}

Requirements
------------

- User requirements

   + python>={{ cookiecutter.python_version }}
   + poetry (recommended)

- Development requirements

   + tox
   {%- if cookiecutter.use_docker|lower == "n" -%}
   + docker >=18.09
   + docker-compose >= 1.22
   {%- endif -%}


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

+ Coverage reports:

   - located in `coverage.unit.xml` and `coverage.integration.xml`

+ Documentation:

   - Builds using sphinx
   - Source located at `docs/source`
   - Output located at `docs/build`

Contribute
----------

- Development
   For tests design, you can use use ´@pytest.mark.incremental´ and  ´@pytest.mark.slow´. See "{{ cookiecutter.project_name }}/tests/conftest.py"
{%- if cookiecutter.use_github|lower == "y" -%}
- Issue Tracker: {{ cookiecutter.repo }}/issues
- Source Code: {{ cookiecutter.repo }}
{%- endif -%}


Support
-------

If you are having issues, please let us know.
Contact us at: {{ cookiecutter.project_name }} {{ cookiecutter.maintainer }}

{%- if cookiecutter.license|trim() != "" -%}
License
-------

{{ cookiecutter.license }}
{%- endif -%}

{%- if cookiecutter.copyright|trim() != "" -%}
Copyright
-------

{{ cookiecutter.copyright }}
{%- endif -%}
