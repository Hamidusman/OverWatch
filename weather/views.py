from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
  city = ''
  data = {}
  error_message = None

  if request.method == 'POST':
    try:
      city = request.POST['city']
      url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=83c5fe972e2774e1d0ce9250eec48664'
      res = urllib.request.urlopen(url).read()
      json_data = json.loads(res)
      data = {
          'country_code': str(json_data['sys']['country']),
          'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
          'temp': str(json_data['main']['temp'] - 273.15) + ' C',
          'pressure': str(json_data['main']['pressure']),
          'humidity': str(json_data['main']['humidity'])
      }
    except (urllib.error.URLError, json.JSONDecodeError) as e:
      error_message = f"Error retrieving weather data: {e}"

  return render(request, 'index.html', {'data': data, 'city': city, 'error_message': error_message})



'''  Hello, World!



For the passed few days, I got involved on a handful of projects, ranging from web development, web scraping and automation. Most which will be showcased in the future. 



But for now, I present to you OverWatch, essentially, a weather application. (Please, don't mind my subpar web design skills)



This webapp makes use of the OpenWeather API to fetch accurate data on the temperature from all known locations. I also implemented an exception method, should the searched location be unreachable or nonexistent. (with Django btw)



I worked on this project some time ago, when I initially learned about public APIs. Just made a few changes to it recently. This is the GitHub repository: https://github.com/Hamidusman/OverWatch (feel free to check out my way cooler projects 👀).



There are tons of APIs out there. If there is a cool API you know of, I would be happy to know about it and possibly work with it.



Danke :)'''