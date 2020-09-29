from django.shortcuts import render
import requests
from .models import *


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1f3cda3b32790247c37903ac750221cb'
    city = 'California'  # request.GET.get('city_name')
    

    cities = Country.objects.all()
    weather_data = []

    for city in cities:   # cities is list each time iteration will produce a jason data that we will store in weather_data list
        r = requests.get(url.format(city)).json()  # passing city into format{} of url
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],  # 'main': {'temp':111,....}
            'description': r['weather'][0]['description'], # 'weather': [{'id':800, 'description':'clear sky',....}]
            'icon': r['weather'][0]['icon'],
        } 

        weather_data.append(city_weather)

    return render(request, 'weather_app/index.html', {'weather_data':weather_data})



def specific(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1f3cda3b32790247c37903ac750221cb'
    city = request.GET.get('city_name')
    r = requests.get(url.format(city)).json()
    city_weather = {
        'city':city,
        'temprature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    return render(request, 'weather_app/specific.html', {'city_weather':city_weather})

