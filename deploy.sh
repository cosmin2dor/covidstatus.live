#!/bin/bash

docker build -t covid-django webapp/

docker stop covid-django
docker run --rm -d -v /var/www/covid-status/static:/static -v /home/ubuntu/covidstatus.live/webapp/data.json:/django/data.json,shared --network=django-redis -p 8000:8000 --name covid-django covid-django

pkill -f updater.sh
nohup bash fetch/updater.sh &