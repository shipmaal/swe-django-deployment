#!/usr/bin/env bash
set -o errexit


pip install pipenv
pipenv install

cd student_planner

pipenv run python manage.py migrate
pipenv run python manage.py csci
pipenv run python manage.py math
pipenv run python manage.py createsu