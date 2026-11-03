# Imports go at the top
from microbit import temperature, sleep, pin0, display
from Lib_DHT11 import DHT11
import log
import speech

# interval = 30 * 60 * 1000
interval = 5000

sensor = DHT11(pin0)

def beep():
    display.set_pixel(2, 2, 9)
    speech.pronounce('Midiendo temperatura')
    sleep(100)
    display.set_pixel(2, 2, 0)
    
while True:
    beep()
    dht11_temp, dth11_hum = sensor.read()
    log.add({
        'Temperature Microbit': temperature(),
        'Temperature DHT11': dht11_temp,
        'Humidity DHT11': dth11_hum,
    })
    sleep(interval)
