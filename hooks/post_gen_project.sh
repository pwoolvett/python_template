

# create dotenv file
cp .env.dist .env
echo -e "FILE_CREATED_BY=python_template\n">> .env


# initialize git repo
git init
git remote add origin {{ cookiecutter.repo }}
git add .
git commit -m "initial commit"
git push --set-upstream origin master


# install virtualenv into ./.venv/ and run poetry install
tox -e venv

