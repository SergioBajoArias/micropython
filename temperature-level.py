#
# Connect two DHT11 sensors to P0 and P1 respectively
#

from microbit import temperature, sleep, pin0, pin1, display
from Lib_DHT11 import DHT11
import log
import math
import speech

interval = 5 * 60 * 1000
sleep(2000)
sensor0 = DHT11(pin0)
sensor1 = DHT11(pin1)

def beep():
    display.set_pixel(2, 2, 9)
    speech.say('Midiendo temperatura')
    sleep(100)
    display.set_pixel(2, 2, 0)

def getMicrobitTemperature():
    return temperature()

def getDHT11Temperature(pin):
    pinVal = pin.read_analog()
    volt = pinVal * 3.3 / 1023.0
    if volt > 0:
        resist = 10 / ((3.3 / volt) -1)
        return round(1 / (1 / 25 + math.log(resist / 10) / 3997))
    else:
        return 0

while True:
    beep()
    try:
        log.add({
            'Temperature Microbit': getMicrobitTemperature(),
            'Temperature DHT11 P0 (alg)': getDHT11Temperature(pin0),
            'Temperature DHT11 P1 (alg)': getDHT11Temperature(pin1),
            'Temperature DHT11 P0 (lib)': sensor0.read(),
            'Temperature DHT11 P1 (lib)': sensor1.read(),
        })
    except Exception as e:
        log.add({
            'Temperature Microbit': getMicrobitTemperature(),
            'Temperature DHT11 P0 (alg)': '---',
            'Temperature DHT11 P1 (alg)': '---',
            'Temperature DHT11 P0 (lib)': '---',
            'Temperature DHT11 P1 (lib)': '---',
        })
    sleep(interval)
