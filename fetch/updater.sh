#!/bin/bash

while [ True ]
do
	scrapy crawl bot -a filename=data
	docker cp /home/ubuntu/covidstatus.live/webapp/data.json covid-django:/django/
	sleep 60m
done
