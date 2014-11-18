#!/bin/sh

cd /home/pi/projects/kindle-weather-display/server

python2 weather-script.py
rsvg-convert --background-color=white -o weather-script-output-raw.png weather-script-output.svg
pngcrush -c 0 weather-script-output-raw.png weather-script-output.png
scp weather-script-output.png kindle:/mnt/us/weather/  
ssh kindle "/bin/sh /mnt/us/weather/show.sh"
