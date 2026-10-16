from microbit import *

display.off()

selected_animation = 0
pins = [pin0, pin1, pin2, pin3, pin4, pin6, pin7, pin8]

def animation_0():
    for pin in pins:
        pin.write_digital(1)
        sleep(150)
        pin.write_digital(0)
        sleep(5)

def animation_1():
    for pin in pins:
        pin.write_digital(1)
    sleep(150)
    for pin in pins:
        pin.write_digital(0)
    sleep(5)
    
    

animations = [animation_0(), animation_1()]

def show_animation():
    return animations[selected_animation]

while True:
    if(button_a.was_pressed() and selected_animation < len(animations) - 1):
        selected_animation += 1
        
    if(button_b.was_pressed() and selected_animation > 0):
        selected_animation -= 1
    
    show_animation()
