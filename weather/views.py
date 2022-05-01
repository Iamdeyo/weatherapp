from django.shortcuts import redirect, render
import json
import urllib.request
# Create your views here.
def index(req):


    if req.method == "POST":
        city = req.POST['city']

        # data from openweather API in JSON
        api_data = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e2cd184d298ab123b8327d8e8c3c2c0b').read()
        # converting JSON to py dictionary
        json_data = json.loads(api_data)
        # covert the temp(K) to C

        weather_data = {
           'city':  str(json_data['name']),
           'countryCode': str(json_data['sys']['country']),
           'temperture': str(json_data['main']['temp']),
           'cloudsDescription': str(json_data['weather'][0]['description']),
           'pressure': str(json_data['main']['pressure']),
           'humdity': str(json_data['main']['humidity']),
        }

        # print(json_data['weather'][0])
        # wdata = json_data
        wdata = weather_data
        # return redirect('index')
    else:
        wdata = ''

    return render(req, 'weather/index.html', {'data': wdata})