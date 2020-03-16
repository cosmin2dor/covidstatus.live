#!/bin/bash

while [ True ]
do
	scrapy crawl bot
	docker cp /root/covidstatus.live/webapp/data.json covid-django:/django/
	sleep 1m
done
