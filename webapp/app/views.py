from django.shortcuts import render
import requests
import json
from django.core.cache import cache


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def locate_user(request):
    ip = get_client_ip(request)

    cached = cache.get(ip)

    if cached is not None:
        return cached

    api_key = "7fc2d6059a4287dfa817005787c2f7cc"
    endpoint = "http://api.ipstack.com/{}?access_key={}".format(ip, api_key)

    r = requests.get(endpoint)
    data = r.json()

    country_name = data['country_name']

    if country_name == "United States":
        country_name = "USA"
    elif country_name == "United Kingdom":
        country_name = "UK"

    cache.set(ip, country_name, timeout=None)

    return country_name


def index_view(request):
    country = locate_user(request)

    my_country = None

    with open('data.json') as json_file:
        data = json.load(json_file)
        try:
            my_country = data['countires'][country]
        except KeyError:
            pass

        active_cases = int(data['global_cases'].replace(',', '')) - int(data['global_recovered'].replace(',', '')) - int(data['gloabl_deaths'].replace(',', ''))

        return render(request, 'index.html', {'location': country,
                                              'global_cases': data['global_cases'],
                                              'global_deaths': data['gloabl_deaths'],
                                              'global_recovered': data['global_recovered'],
                                              'global_active': active_cases,
                                              'my_country_total_cases': my_country['total_cases'],
                                              'my_country_new_cases': my_country['new_cases'],
                                              'my_country_new_deaths': my_country['new_deaths'],
                                              'my_country_total_deaths': my_country['total_deaths'],
                                              'countires': data['countires']})