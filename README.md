# Kindle Weather Display


Original from mpetroff/kindle-weather-display


Edited a bit to run on a Raspberry Pi, with static paths, then SCPed over the USB cable. 
I chose this route because I have a Kindle 2I, which only  has whispernet (no WIFI).
There were connection issues when testing, so I decided to just use one of the ports on my B+.


The generation code is the same as the original from mpetroff, but then the RPI SCPs the png file over, and runs a simple script on the kindle to eips -g the image where the SCP placed it.

I also replaced TODAY and TOMORROW with the day names because forgetfulness.
