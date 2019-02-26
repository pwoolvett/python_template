
# initialize git repo
git init
git remote add origin {{ cookiecutter.repo }}
git add .
git commit -m "initial commit"
git push --set-upstream origin master


# install virtualenv into ./.venv/ and run poetry install
tox -e venv

