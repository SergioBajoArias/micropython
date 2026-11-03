from microbit import temperature, sleep, pin0, display
import log
import math
import music

# interval = 30 * 60 * 1000
interval = 5000

def beep():
    display.set_pixel(2, 2, 9)
    music.play(['a'])
    sleep(100)
    display.set_pixel(2, 2, 0)

def getMicrobitTemperature():
    return temperature()

def getDHT11Temperature(resist):
    return round(1 / (1 / 25 + math.log(resist / 10) / 3997))

def getDHT11Volt():
    pin0Val = pin0.read_analog()
    return pin0Val * 3.3 / 1023.0

def getDHT11Resist(volt):
    if volt > 0:
        return 10 / ((3.3 / volt) -1)
    else:
        return 0
    

while True:
    beep()
    voltDHT11 = getDHT11Volt()
    resistDHT11 = 0
    tempDHT11 = 0
    if(voltDHT11 > 0):
        resistDHT11 = getDHT11Resist(voltDHT11)
        tempDHT11 = getDHT11Temperature(resistDHT11)
    log.add({
        'Temperature Microbit': getMicrobitTemperature(),
        'Temperature DHT11': tempDHT11,
        'Volt DHT11': voltDHT11,
        'Resist DHT11': resistDHT11
    })
    sleep(interval)
