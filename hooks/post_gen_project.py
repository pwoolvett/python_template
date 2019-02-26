#!/usr/bin/env python

from shutil import copy2 as copy
import subprocess

def _exec(string):
    return subprocess.call(list(string.split()))

# create dotenv file
copy('.env.dist','.env')

with open('.env','a+') as dotenv:
    dotenv.write('FILE_CREATED_BY=python_template\n')

# initialize git repo
commands = [
    "git init",
    "git remote add origin {{ cookiecutter.repo }}",
    "git add .",
    'git commit -m "initial commit"',
    "git push --set-upstream origin master",
]
for command in commands:
    _exec(command)

# install virtualenv into ./.venv/ and run poetry install
_exec('tox -e venv')

