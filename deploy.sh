#!/bin/bash

docker build -t covid-django webapp/
docker tag covid-django cosmin2dor/covid-django
docker push cosmin2dor/covid-django