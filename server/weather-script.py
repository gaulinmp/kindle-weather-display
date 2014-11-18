#!/usr/bin/python2

# Kindle Weather Display
# Matthew Petroff (http://mpetroff.net/)
# September 2012

from xml.dom import minidom
import datetime
import codecs
from dateutil.parser import parse
from dateutil.tz import tzlocal
try:
    # Python 3
    from urllib.request import urlopen
except ImportError:
    # Python 2
    from urllib2 import urlopen

#
# Geographic location
#

latitude = 29.74
longitude = -95.40



#
# Download and parse weather data
#

# Fetch data (change lat and lon to desired location)
url_encoded = 'http://graphical.weather.gov/xml/SOAP_server/ndfdSOAPclientByDay.php?whichClient=NDFDgenByDay&lat={}&lon={}&format=24+hourly&numDays=4&Unit=e'.format(latitude, longitude)
weather_xml = urlopen(url_encoded).read()
dom = minidom.parseString(weather_xml)

# Parse temperatures
xml_temperatures = dom.getElementsByTagName('temperature')
highs = [None]*4
lows = [None]*4
for item in xml_temperatures:
    if item.getAttribute('type') == 'maximum':
        values = item.getElementsByTagName('value')
        for i in range(len(values)):
            highs[i] = int(values[i].firstChild.nodeValue)
    if item.getAttribute('type') == 'minimum':
        values = item.getElementsByTagName('value')
        for i in range(len(values)):
            lows[i] = int(values[i].firstChild.nodeValue)

# Parse icons
xml_icons = dom.getElementsByTagName('icon-link')
icons = [None]*4
for i in range(len(xml_icons)):
    icons[i] = xml_icons[i].firstChild.nodeValue.split('/')[-1].split('.')[0].rstrip('0123456789')

# Parse dates
xml_day_one = dom.getElementsByTagName('start-valid-time')[0].firstChild.nodeValue
day_one = parse(xml_day_one)
full_day_one = dom.getElementsByTagName('creation-date')[0].firstChild.nodeValue

print(full_day_one)

#
# Preprocess SVG
#
one_day = datetime.timedelta(days=1)

info_dict = {'date' : parse(full_day_one).astimezone(tzlocal())}
for i in range(4):  # 4 day forcast
    info_dict['day{}'.format(i)] = (day_one + i*one_day)
    info_dict['high{}'.format(i)] = highs[i]
    info_dict['low{}'.format(i)] = lows[i]
    info_dict['icon{}'.format(i)] = icons[i]
print(type((day_one + one_day)))
# Open SVG to process
output = codecs.open('weather-script-preprocess.svg', 'r',  encoding='utf-8').read()

output = output
# Write output
codecs.open('weather-script-output.svg', 'w',
             encoding='utf-8').write(output.format(**info_dict))
