from django.http import HttpResponse
from django.shortcuts import redirect, render
import json
from .models import cityModel
# import urllib.request
import requests
# Create your views here.
def index(req):

    savedCities = cityModel.objects.all()

    data2 = []

    for acity in savedCities:

        city = str(acity)
        print(city)
        theapi = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e2cd184d298ab123b8327d8e8c3c2c0b')
        json_data = theapi.json()

        # covert the temp(K) to C
        tempK = float(json_data['main']['temp'])
        temp = str(round((tempK - 273.15), 2))

        weather_dataS = {
        'city':  str(json_data['name']),
        'countryCode': str(json_data['sys']['country']),
        'temperture': str(temp + '°C'),
        'cloudsDescription': str(json_data['weather'][0]['description']),
        'icon': str(json_data['weather'][0]['icon']),
        'pressure': str(json_data['main']['pressure']),
        'humdity': str(json_data['main']['humidity']),
        'cod' :  json_data['cod'], 
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
        # print(json_data)

        if json_data['cod'] == 200:

            # covert the temp(K) to C
            tempK = float(json_data['main']['temp'])
            temp = str(round((tempK - 273.15), 2))

            weather_data = {
           'city':  str(json_data['name']),
           'countryCode': str(json_data['sys']['country']),
           'temperture': str(temp + '°C'),
           'cloudsDescription': str(json_data['weather'][0]['description']),
           'icon': str(json_data['weather'][0]['icon']),
           'pressure': str(json_data['main']['pressure']),
           'humdity': str(json_data['main']['humidity']),
           'cod' :  json_data['cod'], 
            }

        else:

            weather_data = {
                'cod' :  json_data['cod'], 
                'message' : json_data['message'],
            }
            # print(json_data)
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
            # print('allreadyyyyyyyyyyyyyyyyyyyyy')
            pass
        else:
            cityModel.objects.create(
            city = req.POST['cityname']
            )
            print(req.POST['cityname'])

            

    return redirect('index')
    # return HttpResponse('good')