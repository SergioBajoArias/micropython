from microbit import temperature, sleep
import log

interval = 30 * 60 * 1000

while True:
    log.add({
        'Temperature Microbit': temperature(),
        'Temperature DHT11': 4
    })
    sleep(interval)
