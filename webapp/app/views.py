from django.shortcuts import render, redirect
import requests
import json
from django.core.cache import cache
from .forms import SubscribeForm
from .models import Subscription
from .geolocations import geolocate, d


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def locate_user(request):
    ip = get_client_ip(request)

    cache.set(ip, "China", timeout=None)

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


def generate_locations(data):
    result = {}

    print(data['countires'])

    for country, value in data['countires'].items():
        if int(value['total_cases']) > 0:
            location = geolocate(country=country)
            try:
                result[country] = {
                    'lat': location[0],
                    'lon': location[1],
                }
            except TypeError:
                continue

    return result


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
        # active_cases = data['global_cases'] - data['global_recovered'] - data['gloabl_deaths']
        my_country_rate = "{0:.2f}%".format(float(my_country['total_deaths']) / int(my_country['total_cases']) * 100)



        return render(request, 'index.html', {'location': country,
                                              'global_cases': data['global_cases'],
                                              'global_deaths': data['gloabl_deaths'],
                                              'global_recovered': data['global_recovered'],
                                              'global_active': active_cases,
                                              'my_country_total_cases': my_country['total_cases'],
                                              'my_country_new_cases': my_country['new_cases'],
                                              'my_country_new_deaths': my_country['new_deaths'],
                                              'my_country_total_deaths': my_country['total_deaths'],
                                              'countires': data['countires'],
                                              'my_country_rate': my_country_rate,
                                              'map_locations': d})


def subscribe_view(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            country_name = form.cleaned_data['country_name']

            s = Subscription(email=email, country_name= country_name)
            s.save()

        return redirect('/?subscribed')
