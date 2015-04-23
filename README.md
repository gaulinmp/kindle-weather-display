# Kindle Weather Display

Original from mpetroff/kindle-weather-display

## Changes

Edited a bit to run on a Raspberry Pi, with static paths, then `SCP`ed over the USB cable. 
I chose this route because I have a Kindle 2I, which only  has whispernet (no WIFI).
There were connection issues when testing, so I decided to just use one of the ports on my B+.

The generation code is the same as the original from mpetroff, but then the RPI `SCP`s the png file over, and runs a simple script on the kindle (just `eips -g`) to display the new image.

I also replaced TODAY and TOMORROW with the day names because forgetfulness.

### Forecast.io
I changed the data source to use forecast.io's very friendly API (get a key [here](https://developer.forecast.io/register)).
It allows for much more data, as well as current temperature and conditions. 
If the raw return is passed into python's string.format, all of the formatting could go in the SVG file where currently I have things like {temp:.0f}.

### Screenshot

![screenshot](https://raw.githubusercontent.com/gaulinmp/kindle-weather-display/master/server/weather-script-output.png)


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
I put the jailbreak files in the [jailbreak folder](https://github.com/gaulinmp/kindle-weather-display/tree/master/jailbreak) just in case mobileread forums go down and the files get lost.
