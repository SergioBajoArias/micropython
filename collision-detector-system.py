#
# Connect Neopixel to P2
# Connect Sonar's trigger to P0 and Sonar's echo to P1
#

from microbit import *

I2C_LCD1602.lcd_init(0x27)
I2C_LCD1602.show_string("Distancia: ", 0, 0)
I2C_LCD1602.backlight_on()

highBrightness = 20
lowBrightness = 0
maxDistance = 30
strip = neopixel.create(DigitalPin.P2, 1, NeoPixelMode.RGB)
strip.set_brightness(lowBrightness)
semaphoreColors = [NeoPixelColors.RED, NeoPixelColors.ORANGE, NeoPixelColors.GREEN]

def on_forever():
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    I2C_LCD1602.show_string("     ", 11, 0)
    I2C_LCD1602.show_number(distance, 11, 0)
    if(distance < maxDistance):
        strip.set_brightness(highBrightness)
        colorIndex = Math.round(pins.map(distance, 0, maxDistance, 0, len(semaphoreColors) - 1))
        basic.show_number(colorIndex)
        strip.show_color(semaphoreColors[colorIndex])
    else:
        strip.set_brightness(lowBrightness)
    basic.pause(100)

basic.forever(on_forever)
