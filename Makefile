PROJECT_NAME=MINI-PROJECT
PROJECT_MAIN_MODULE=
PYTHON_VERSION=3.8

#Variable needed to create the virutal env in subsidiaries called .venv
export PIPENV_VENV_IN_PROJECT=1

dep:
	@python3 -m pip install -U pip
	@python3 -m pip install pipenv
	@python3 -m pip install pre-commit

.create_env:
	@echo "PIPENV_VENV_IN_PROJECT=1" > .env

.precommit:
	@pipenv pre-commit install

welcome: dep .create_env .precommit

lint:
	@flake8 ... --count --max-complexity=10 --max-line-length=127 --statistics
