#!/usr/bin/env bash
set -o errexit

echo "Current working directory:"
ls -al

pip install pipenv
pipenv install

cd /student_planner/

pipenv run python manage.py migrate