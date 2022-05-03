from django.http import HttpResponse
from django.shortcuts import redirect, render
import json
from .models import cityModel
# import urllib.request
import requests
import math
from django.contrib import messages
# Create your views here.
def index(req):

    savedCities = cityModel.objects.all()

    data2 = []
 

    for acity in savedCities:

        city = str(acity)


        theapi = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e2cd184d298ab123b8327d8e8c3c2c0b')
        json_data = theapi.json()

        # covert the temp(K) to C
        tempK = float(json_data['main']['temp'])
        temp = str(math.floor(tempK - 273.15))
        # temp = str(round((tempK - 273.15), 2))

        feelsLikeK = float(json_data['main']['feels_like'])
        feelsLike = str(math.floor(feelsLikeK - 273.15))

        weather_dataS = {
        'city':  str(json_data['name']),
        'countryCode': str(json_data['sys']['country']),
        'temperture': str(temp + '°C'),
        'feelsLike' :  str(feelsLike + '°C'),
        'cloudsDescription': str(json_data['weather'][0]['description']),
        'icon': str(json_data['weather'][0]['icon']),
        'pressure': str(json_data['main']['pressure']),
        'humdity': str(json_data['main']['humidity']),
        'cod' :  json_data['cod'],
        'visibility' :  json_data['visibility'],
        'wind' :  json_data['wind']['speed'],
        }
        data2.append(weather_dataS)


    # acity = str(cityModel.objects.get(id=1))
    # print(acity)

    if req.method == "POST":
        city = req.POST['city']

        # data from openweather API in JSON
        # api_data = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e2cd184d298ab123b8327d8e8c3c2c0b').read()
        api_data = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e2cd184d298ab123b8327d8e8c3c2c0b')


        # converting JSON to py dictionary
        # json_data = json.loads(api_data)
        json_data = api_data.json()
        print(json_data)

        if json_data['cod'] == 200:

            # covert the temp(K) to C
            tempK = float(json_data['main']['temp'])
            temp = str(math.floor(tempK - 273.15))

            feelsLikeK = float(json_data['main']['feels_like'])
            feelsLike = str(math.floor(feelsLikeK - 273.15))

            weather_data = {
            'city':  str(json_data['name']),
            'countryCode': str(json_data['sys']['country']),
            'temperture': str(temp + '°C'),
            'feelsLike' :  str(feelsLike + '°C'),
            'cloudsDescription': str(json_data['weather'][0]['description']),
            'icon': str(json_data['weather'][0]['icon']),
            'pressure': str(json_data['main']['pressure']),
            'humdity': str(json_data['main']['humidity']),
            'cod' :  json_data['cod'],
            'visibility' :  json_data['visibility'],
            'wind' :  json_data['wind']['speed'],
            }

        else:

            weather_data = {
                'cod' :  json_data['cod'], 
                'message' : json_data['message'],
            }
            print(json_data)
            # return redirect('index')

        # wdata = json_data
        wdata = weather_data
        # return redirect('index')
    else:
        wdata = ''

    return render(req, 'weather/index.html', {'data': wdata, 'data2': data2})

def addCity(req):

    if req.method == "POST":

        newCity = req.POST['cityname']

        if cityModel.objects.filter(city = newCity):
            pass
        else:
            cityModel.objects.create(
            city = req.POST['cityname']
            )

            

    return redirect('index')
    # return HttpResponse('good')

def delCity(req, cn):
    # cn is cityname

    # print(cn)
    # print(type(cn))

    delcity = cityModel.objects.get(city= cn)
    delcity.delete()

    # non-case sensitive query
    # delcity = cityModel.objects.filter(city__iexact=cn)
    # for city in delcity:
    #     print(city)
    #     city.delete()


    return redirect('index')

