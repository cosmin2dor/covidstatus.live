#!/bin/bash

scrapy crawl bot -a filename=$1
docker cp /home/ubuntu/covidstatus.live/webapp/$1.json covid-django:/django/
