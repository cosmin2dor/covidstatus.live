docker run --rm -d -v /var/www/covid-status/static:/static -v /root/covidstatus.live/webapp/data.json:/django/data.json,shared -p 8000:8000 --name covid-django cosmin2dor/covid-django:stable
docker cp /root/covidstatus.live/webapp/data.json.backup covid-django:/django/
