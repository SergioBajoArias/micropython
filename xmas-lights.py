from microbit import *

selected_animation = 0
display.show(selected_animation)
pins = [pin0, pin1, pin2, pin8, pin12, pin13, pin14, pin15]

def animation_0():
    for pin in pins:
        pin.write_digital(1)
        sleep(150)
        pin.write_digital(0)
        sleep(5)

def animation_1():
    for pin in pins:
        pin.write_digital(1)
    sleep(500)
    for pin in pins:
        pin.write_digital(0)
    sleep(500)

while True:
    if(button_b.was_pressed() and selected_animation < 1):
        selected_animation += 1
        display.show(selected_animation)
        
    if(button_a.was_pressed() and selected_animation > 0):
        selected_animation -= 1
        display.show(selected_animation)
    
    if(selected_animation == 0):
        animation_0()
    elif(selected_animation == 1):
        animation_1()
