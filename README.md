# Kindle Weather Display

Original from mpetroff/kindle-weather-display

## How to do

Basically, I followed [this blog post](http://www.turnkeylinux.org/blog/kindle-root). Everything more or less worked as advertised. 

The only annoying part was after getting the USBNethack files on the Kindle, trying to make it show up under ifconfig on the rpi. The blog post (and much of the internet) says:
```
# doesn't work!
;debugOn
~help # just for fun
~usbNetwork
;debugOff
```
But that just didn't work for me. Turns out, instead of ~ (tilde), I had to use ` (backtick). 
```
# does work!
;debugOn
`help # just for fun
`usbNetwork
;debugOff
```
After figuring that out, everything worked as advertised. 

## Changes

Edited a bit to run on a Raspberry Pi, with static paths, then SCPed over the USB cable. 
I chose this route because I have a Kindle 2I, which only  has whispernet (no WIFI).
There were connection issues when testing, so I decided to just use one of the ports on my B+.

The generation code is the same as the original from mpetroff, but then the RPI SCPs the png file over, and runs a simple script on the kindle to eips -g the image where the SCP placed it.

I also replaced TODAY and TOMORROW with the day names because forgetfulness.

![screenshot](https://raw.githubusercontent.com/gaulinmp/kindle-weather-display/master/server/weather-script-output.png)
