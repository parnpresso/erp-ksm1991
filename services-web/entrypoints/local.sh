#!/usr/bin/env sh

while ! nc -z db 5432; do sleep 1; done

python3 erp/manage.py migrate --settings=erp.settings.local
python3 erp/manage.py runserver 0.0.0.0:8000 --settings=erp.settings.local
