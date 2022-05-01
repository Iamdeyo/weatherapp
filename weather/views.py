from django.shortcuts import redirect, render
import json
# import urllib.request
import requests
# Create your views here.
def index(req):
    if req.method == "POST":
        # api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e2cd184d298ab123b8327d8e8c3c2c0b'


        city = req.POST['city']

        # data from openweather API in JSON
        # api_data = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e2cd184d298ab123b8327d8e8c3c2c0b').read()
        api_data = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e2cd184d298ab123b8327d8e8c3c2c0b')


        # converting JSON to py dictionary
        # json_data = json.loads(api_data)
        json_data = api_data.json()
        # print(json_data)

        if json_data['cod'] == 200:
            pass
        else:
            # print(json_data['message'])
            return redirect('index')

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
        }


        # wdata = json_data
        wdata = weather_data
        # return redirect('index')
    else:
        wdata = ''

    return render(req, 'weather/index.html', {'data': wdata})