1. clone
2. refactor "package" folder
3. enjoy!

reqs:
  pipenv
  tox
  python>=3.6

optionally set env:
PIPENV_VENV_IN_PROJECT=true

for dev:
  :code:`tox -e env` creates virtualenv located at .venv
  (see PIPENV_VENV_IN_PROJECT)

testing:

- unit / developer-required tests with pytest
- integration testing with docker-compose+pytest
- user stories testing with docker-compose+behave
