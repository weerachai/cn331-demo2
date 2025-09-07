#!/usr/bin/env bash
# Exit on error
set -o errexit

cd $(dirname $(find . | grep manage.py$))
gunicorn $(dirname $(find . | grep wsgi.py$) | sed "s/\.\///g").wsgi