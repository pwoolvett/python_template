.. image:: https://circleci.com/gh/pwoolvett/python_template.svg?style=shield
    :target: https://circleci.com/gh/pwoolvett/python_template
    :alt: Build Status

.. image:: https://api.codeclimate.com/v1/badges/f0f976249fae332a0bab/test_coverage
   :target: https://codeclimate.com/github/pwoolvett/python_template/test_coverage
   :alt: Test Coverage


.. image:: https://api.codeclimate.com/v1/badges/f0f976249fae332a0bab/maintainability
   :target: https://codeclimate.com/github/pwoolvett/python_template/maintainability
   :alt: Maintainability

Requirements
---

* cookiecutter
* poetry (must be in PATH)
* tox (must be in PATH)
* python>=3.6

Usage:
---

1. `cookiecutter https://github.com/pwoolvett/python_template`
2. Answer questions properly
3. enjoy!



for dev:
  :code:`tox -e env` creates virtualenv located at .venv

testing:

- unit / developer-required tests with pytest
- integration testing with docker-compose+pytest
- user stories testing with docker-compose+behave
