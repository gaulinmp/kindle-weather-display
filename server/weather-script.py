
# coding: utf-8

# In[6]:

import re
import os
import json
import codecs
import datetime as dt
from dateutil.parser import parse
from dateutil.tz import tzlocal
try:
    # Python 3
    from urllib.request import urlopen
except ImportError:
    # Python 2
    from urllib2 import urlopen


# In[2]:

#
# Geographic location: Houston
#
latitude = 29.76
longitude = -95.37

one_day = dt.timedelta(days=1)


# In[3]:

def get_icon_lookup_dict(filename = None):
    """
    Reads the ID tags from an SVG, and returns a dictionary in the form:
    {'forecast.io name': 'svg ID value'}
    """
    if not filename:
        filename = 'weather-script-preprocess.svg'
    with open(filename) as fh:
        txt = fh.read()
        icon_dict = {x:[x] for x in re.findall(r'(?<=id=")[^"]*(?=")', txt) if x not in ('divider')}
    # Icon names from forecast.io: 
    # clear-day, clear-night, rain, snow, sleet, wind, 
    # fog, cloudy, partly-cloudy-day, partly-cloudy-night
    icon_dict['sun'].extend(['clear-day','clear-night'])
    icon_dict['overcast'].extend(['cloudy'])
    icon_dict['clouds-medium'].extend(['partly-cloudy-day','partly-cloudy-night'])
    icon_dict['rain-freezing'].extend(['sleet'])

    return {v:k for k,vs in icon_dict.items() for v in vs }


# In[4]:

#
# Download and parse weather data. Must have API key at ~/.forecastio.key
#
try:
    API_KEY = str(open(os.path.expanduser('~/.forecastio.key')).read().strip())
except FileNotFoundError:
    print("No API key existed")
    exit()
url_raw = "https://api.forecast.io/forecast/{key}/{lat},{lon}?exclude=hourly,alerts,flags"
# Todays weather
url_weather = url_raw.format(key=API_KEY, lat=latitude, lon=longitude)
weather_data = urlopen(url_weather).read().decode("utf-8")
weather_json = json.loads(weather_data)
#weather_json.keys()


# In[7]:

# Assemble first day data (0 day)
icon_dict = get_icon_lookup_dict()


# In[8]:

#
# Preprocess SVG
#
info_dict = {'date' : dt.datetime.now()}

# Add data: date, day#, icon#, rain#, high#, low#
for i in range(0,4):  # 4 day forcast
    info_dict['day{}'.format(i)] = info_dict['date'] + i*one_day
    info_dict['high{}'.format(i)] = weather_json['daily']['data'][i]['apparentTemperatureMax']
    info_dict['low{}'.format(i)] = weather_json['daily']['data'][i]['apparentTemperatureMin']
    info_dict['icon{}'.format(i)] = icon_dict.get(weather_json['daily']['data'][i]['icon'], 'sun')
    info_dict['rain{}'.format(i)] = ("{:2d}%".format(int(weather_json['daily']['data'][i]['precipProbability']*100)) 
                                     if weather_json['daily']['data'][i]['precipProbability']>0 else '')

info_dict['temp'] = weather_json['currently']['apparentTemperature']

# Open SVG to process
output = codecs.open('weather-script-preprocess.svg', 'r',  encoding='utf-8').read()

# Write output
codecs.open('weather-script-output.svg', 'w',
             encoding='utf-8').write(output.format(**info_dict))

