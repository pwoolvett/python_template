FROM python:{{ cookiecutter.python_version }}-alpine

MAINTAINER {{ cookiecutter.author }}

# Install system dependencies here
RUN "curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python"

# Update system deps
RUN "poetry self:update --preview"

# avoid virtualenvs in production, see https://github.com/sdispater/poetry/issues/218
RUN "poetry config settings.virtualenvs.create false"

# Add poetry.lock before rest of repo for caching, see https://www.aptible.com/documentation/enclave/tutorials/faq/dockerfile-caching/pip-dockerfile-caching.html
ADD poetry.lock /app/
ADD pyproject.toml /app/

WORKDIR /app
RUN "poetry install --no-dev -vvv"

ADD . /app

CMD {{ cookiecutter.slug_name }}
