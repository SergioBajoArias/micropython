#
# For https://python.microbit.org/v/3
# Connect the joystick to P0
#

from microbit import *

imageCodeTemplate = "00i00:0iii0:iiiii:0iii0:00i00"

def map(x, in_min, in_max, out_min, out_max): 
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

def renderImage(i):
    imageCode = imageCodeTemplate.replace("i", str(i))
    image = Image(imageCode)
    display.show(image)

while True:
    joystickVal = pin0.read_analog()
    i = round(map(joystickVal, 0, 1023, 0, 9))
    renderImage(i)
    sleep(100)
