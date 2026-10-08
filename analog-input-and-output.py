#
# Connect Joystick to P0 and LED to P1
#

from microbit import *

def on_forever():
    joystickVal = pins.analog_read_pin(AnalogPin.P0)
    pins.analog_write_pin(AnalogPin.P1, joystickVal)

basic.forever(on_forever)
