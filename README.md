# CONFITURE

A co-routine based executive for a NeoPixel jamjar,
running on a Pi Pico (RP2040).

## Dramatis Personae

* A jam jar, jam eaten, jar de-labelled and washed
* Pi Pico
* NeoPixel LED string (I blew up the first pixel, so I've cut it off)
* Adafruit CircuitPython 9.2.8
* Rotary encoder with push button


## Confiture v3 board

In kicad-test directory.

Fabricated x3 by aisler.

This works.

Problems to fix if I make v4:

i) the mounting holes for USB connector are too small, so the connector
rides a bit high and is not as securely connected as I want.

ii) There is no facility for protective capacitor and resistor. This is
fine for small battery powered projects, but it would be nice to have
the option to add: for capacitor, this could be entirely optional points
across the power bus. For the resistor, probably ok to make it compulsory
with an option to use a direct link not a resistor when placing components.

iii) v. minor some of the writing is off the side of the board or
hidden by components. This could all be tidied up.

iv) add cable tie strain relief hole

## minicom

To talk to micropython:

minicom --device=/dev/ttyACM0 --baud=115200

then press ctrl-C to interrupt and get a python prompt -- otherwise it
sits there with no output as it runs the LEDs.

## third party drivers

neopixel.py in this repo is neopixel.py from
0ba2f2122a54a71b1bc3576f87b1ba7dfc9db11e of 
https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/
