from django.shortcuts import render
import requests
import json


def get_client_ip(request):
    return "188.26.27.31"
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def locate_user(request):
    ip = get_client_ip(request)
    api_key = "6fd4e0d631f6fb7fce324c7e928a3ddd"
    endpoint = "http://api.ipstack.com/{}?access_key={}".format(ip, api_key)

    r = requests.get(endpoint)
    data = r.json()

    return data['country_name'], data['location']['country_flag']


def index_view(request):
    country, flag = locate_user(request)

    my_country = None

    with open('data.json') as json_file:
        data = json.load(json_file)
        try:
            my_country = data['countires'][country]
        except KeyError:
            pass

        active_cases = int(data['global_cases'].replace(',', '')) - int(data['global_recovered'].replace(',', '')) - int(data['gloabl_deaths'].replace(',', ''))

        return render(request, 'index.html', {'location': country,
                                              'flag': flag,
                                              'global_cases': data['global_cases'],
                                              'global_deaths': data['gloabl_deaths'],
                                              'global_recovered': data['global_recovered'],
                                              'global_active': active_cases,
                                              'my_country_total_cases': my_country['total_cases'],
                                              'my_country_new_cases': my_country['new_cases'],
                                              'my_country_new_deaths': my_country['new_deaths'],
                                              'my_country_total_deaths': my_country['total_deaths'],
                                              'countires': data['countires']})