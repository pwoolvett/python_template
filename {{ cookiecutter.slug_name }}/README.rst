.. image:: https://circleci.com/gh/pwoolvett/python_template.svg?style=shield
    :target: https://circleci.com/gh/pwoolvett/python_template
    :alt: Build Status

.. image:: https://api.codeclimate.com/v1/badges/f0f976249fae332a0bab/test_coverage
   :target: https://codeclimate.com/github/pwoolvett/python_template/test_coverage
   :alt: Test Coverage


.. image:: https://api.codeclimate.com/v1/badges/f0f976249fae332a0bab/maintainability
   :target: https://codeclimate.com/github/pwoolvett/python_template/maintainability
   :alt: Maintainability

Development requirements:
  poetry
  tox
  python>={{ cookiecutter.python_version }}

note:
  :code:`tox -e venv` creates virtualenv located at .venv


testing:

- just run tox in project root
- unit / developer-required tests with pytest
- integration testing with docker-compose+pytest
- user stories testing with docker-compose+behave
