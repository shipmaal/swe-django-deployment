#!/usr/bin/env bash
set -o errexit

pip install pipenv
pipenv install

pipenv run python manage.py collectstatic --no-input
pipenv run python manage.py migrate