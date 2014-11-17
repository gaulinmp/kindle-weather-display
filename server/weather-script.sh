#!/bin/sh

#cd "$(dirname "$0")"
cd /

python2 weather-script.py
rsvg-convert --background-color=white -o weather-script-output-raw.png weather-script-output.svg
pngcrush -c 0 weather-script-output-raw.png weather-script-output.png
# cp -f weather-script-output.png /var/www/weather/weather-script-output.png
scp weather-script-output.png kindle:/mnt/us/weather/  
