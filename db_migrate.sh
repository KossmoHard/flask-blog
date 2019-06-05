#!/bin/bash
source .venv/bin/activate
python app/manage.py db init
python app/manage.py db migrate
python app/manage.py db upgrade
