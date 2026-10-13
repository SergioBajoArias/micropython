#
# Connect Sx pin of the joystick to P0 and LED to P1
#

from microbit import pin0, pin1

while True: 
    joystickVal = pin0.read_analog()
    pin1.write_analog(joystickVal)
