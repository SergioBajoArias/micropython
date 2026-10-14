#
# For https://python.microbit.org/v/3
# Connect something that requires a digital input to P0 in order to make it work
# It will be activated with A button and deactivated with B button
#

from microbit import pin0, button_a, button_b, sleep

while True:
    if(button_a.is_pressed()):
        pin0.write_digital(1)
    if(button_b.is_pressed()):
        pin0.write_digital(0)
    sleep(100)
