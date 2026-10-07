#
# Connect something that requires a digital input to P0 in order to make it work
# It will be activated with A button and deactivated with B button
#

from microbit import *

def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 1)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P0, 0)

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
