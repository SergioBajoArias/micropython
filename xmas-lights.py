from microbit import *

display.off()

pins = [pin0, pin1, pin2, pin3, pin4, pin6, pin7, pin8]

while True:
    for pin in pins:
        pin.write_digital(1)
        sleep(150)
        pin.write_digital(0)
        sleep(5)
