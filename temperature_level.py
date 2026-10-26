from microbit import temperature, sleep, pin0
import log
import math

interval = 30 * 60 * 1000

def getMicrobitTemperature():
    return temperature()

def getDHT11Temperature():
    pin0Val = pin0.read_analog()
    volt = pin0Val * 3.3 / 1023.0
    resist = 10 / ((3.3 / volt) -1)
    return round(1 / (1 / 25 + math.log(resist / 10) / 3997))

while True:
    log.add({
        'Temperature Microbit': getMicrobitTemperature(),
        'Temperature DHT11': getDHT11Temperature()
    })
    sleep(interval)
