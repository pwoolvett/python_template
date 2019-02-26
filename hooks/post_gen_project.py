#!/usr/bin/env python

import sys
from shutil import copy2 as copy
import subprocess

def _exec(string):
    cmd_arg = [x.replace('___', ' ') for x in string.split(' ')]
    r = subprocess.call(cmd_arg)
    if r !=0:
        sys.exit(r)
    return r

# create dotenv file
copy('.env.dist','.env')

with open('.env','a+') as dotenv:
    dotenv.write('FILE_CREATED_BY=python_template\n')

# initialize git repo
commands = [
    "git init",
    "git remote add origin {{ cookiecutter.repo }}",
    "git add .",
    'git commit -m "initial___commit"',
    "git push --set-upstream origin master",
]
for command in commands:
    r = _exec(command)

# install virtualenv into ./.venv/ and run poetry install
_exec('tox -e venv')

