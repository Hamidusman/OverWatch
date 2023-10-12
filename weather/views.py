from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res =urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=83c5fe972e2774e1d0ce9250eec48664').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + '' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp'] - 273.15) + ' C',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity'])
        }
    else:
        city = 'NIL'
        data = 'NIL'
    return render(request, 'index.html', {'data': data, 'city': city})