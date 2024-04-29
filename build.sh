#!/usr/bin/env bash
set -o errexit


pip install pipenv
pipenv install

cd student_planner

pipenv run python manage.py migrate