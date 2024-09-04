#!/bin/bash

set -e

NAME="revitalle"
NUM_WORKERS=2
PORT=80
TIMEOUT=120
LOGFILE=/app/log/revitalle.log
DJANGO_WSGI_MODULE=revitalle.wsgi

cd /app/revitalle

python manage.py migrate

if [ ${DEBUG:-True} = "True" ]; then
    python manage.py runserver_plus 0:8000 --print-sql
else
    gunicorn ${DJANGO_WSGI_MODULE}:application \
        --name ${NAME} \
        --workers ${NUM_WORKERS} \
        --bind=localhost:${PORT} \
        --log-level=${LOGLEVEL} \
        --timeout=${TIMEOUT} \
        --log-file=${LOGFILE}
fi
