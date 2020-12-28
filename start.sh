#!/bin/bash

docker pull cosmin2dor/covid-django
docker stop covid-django
docker run --rm -d -v /var/www/covid-status/static:/static -v /home/ubuntu/covidstatus.live/webapp/data.json:/django/data.json,shared --network=django-redis -p 8000:8000 --name covid-django cosmin2dor/covid-django
docker cp /home/ubuntu/covidstatus.live/webapp/data.json covid-django:/django/
