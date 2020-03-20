from django.shortcuts import render, redirect
import requests
import json
from django.core.cache import cache
from .forms import SubscribeForm
from .models import Subscription


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

    country_code = data['country_code']

    cache.set(ip, country_code, timeout=None)

    return country_code


# def generate_locations(data):
#     result = {}
#
#     print(data['countires'])
#
#     for country, value in data['countires'].items():
#         if int(value['total_cases']) > 0:
#             location = geolocate(country=country)
#             try:
#                 result[country] = {
#                     'lat': location[0],
#                     'lon': location[1],
#                 }
#             except TypeError:
#                 continue
#
#     return result


def index_view(request):
    country_code = locate_user(request)

    print(country_code)

    with open('data.json') as json_file:
        data = json.load(json_file)
        try:
            my_country = data['countires'][country_code]
        except KeyError:
            my_country = data['countires']['US']

        active_cases = int(data['global_cases']) - int(data['global_recovered']) - int(data['gloabl_deaths'])
        my_country_rate = "{0:.2f}%".format(float(my_country['total_deaths']) / int(my_country['total_cases']) * 100)

        my_country_data = {
            "country_name": my_country['country_name'],
            "cases": my_country['total_cases'],
            "new_cases": my_country['new_cases'],
            "deaths": my_country['total_deaths'],
            "new_deaths": my_country['new_deaths'],
            "death_rate": my_country_rate,
        }

        global_data = {
            "cases": data['global_cases'],
            "deaths": data['gloabl_deaths'],
            "recovered": data['global_recovered'],
            "active": active_cases,
        }

        return render(request, 'index.html', {
            'global_data': global_data,
            'my_country_name': country_code,
            'my_country_data': my_country_data,
            'countires': data['countires'],
        })


def subscribe_view(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            country_name = form.cleaned_data['country_name']

            s = Subscription(email=email, country_name= country_name)
            s.save()

        return redirect('/?subscribed')
