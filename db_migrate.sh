#!/bin/bash
source .venv/bin/activate
cd app
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
cd ..
