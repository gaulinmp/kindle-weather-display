#!/bin/sh

/usr/sbin/eips -c
/usr/sbin/eips -c

/usr/sbin/eips -g /mnt/us/weather/weather-script-output.png
date | /usr/sbin/eips 20 1
