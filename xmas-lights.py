from microbit import *
import random

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

def animation_2():
    for pin in pins:
        pin.write_digital(1)
        sleep(150)
        pin.write_digital(0)
        sleep(5)
    for pin in reversed(pins):
        pin.write_digital(1)
        sleep(150)
        pin.write_digital(0)
        sleep(5)

def animation_3():
    for pin in pins:
        pin.write_digital(1)
        sleep(150)
    for pin in pins:
        pin.write_digital(0)
        sleep(150)

def operate_random_pin(value):
    pins_copy = pins.copy()
    while((len(pins_copy)) > 0):
        pin = random.choice(pins_copy)
        pin.write_digital(value)
        pins_copy.remove(pin)
        sleep(150)

def animation_4():
    operate_random_pin(1)
    operate_random_pin(0)

animations = [animation_0, animation_1, animation_2, animation_3, animation_4]     

while True:
    if(button_b.was_pressed() and selected_animation < len(animations) - 1):
        selected_animation += 1
        display.show(selected_animation)
        
    if(button_a.was_pressed() and selected_animation > 0):
        selected_animation -= 1
        display.show(selected_animation)
    
    animations[selected_animation]()
