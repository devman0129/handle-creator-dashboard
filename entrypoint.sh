#!/bin/sh

set -e

python manage.py collectstatic --noinput
python manage.py migrate

exec gunicorn --bind :8000 --workers 2 -t 60 handlechat.wsgi