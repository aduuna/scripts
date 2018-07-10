from pyowm import OWM

owm = OWM("cea41d88ba0edacdf321dc839d631d1b")
observation = owm.weather_at_place('Accra, gh')
w = observation.get_weather()

print(w.get_wind())
print(w.get_humidity())

from pprint import pprint
from requests import request
import json
res = request('GET', 'http://api.openweathermap.org/data/2.5/weather?q=Accra&APPID=cea41d88ba0edacdf321dc839d631d1b')

js = json.loads(res.text)
print(js,end='\n\n\n')

pprint(res.json())
