#!/bin/sh
python manage.py collectstatic --no-input
python manage.py makemigrations core escola
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
#gunicorn django_setup.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile='-'
exec "$@"