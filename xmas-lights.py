from microbit import *
import random

selected_animation = 0
display.show(selected_animation)
pins = [pin0, pin1, pin2, pin8, pin12, pin13, pin14, pin15]

# For animation 5
animating = []
last_added_running_time = 0
LED_INDEX = 0
LEVEL_INDEX = 1
STEP_INDEX = 2
MAX_ANIMATING = 3
LED_INTERVAL = 500
STEP = 5
ANALOG_HIGH_VALUE = 512

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
    while (len(pins_copy)) > 0:
        pin = random.choice(pins_copy)
        pin.write_digital(value)
        pins_copy.remove(pin)
        sleep(150)

def animation_4():
    operate_random_pin(1)
    operate_random_pin(0)

def animation_5():
    global last_added_running_time
    
    if len(animating) < MAX_ANIMATING and running_time() - last_added_running_time >= LED_INTERVAL:
        x = random.randint(0, len(pins) - 1)
        animating.append([x, 0, STEP])
        last_added_running_time = running_time()

    for to_animate in animating:
        pins[to_animate[LED_INDEX]].write_analog(to_animate[LEVEL_INDEX])

        to_animate[LEVEL_INDEX] = to_animate[LEVEL_INDEX] + to_animate[STEP_INDEX]
        
        if to_animate[LEVEL_INDEX] >= ANALOG_HIGH_VALUE:
            to_animate[STEP_INDEX] = -to_animate[STEP_INDEX]
        if to_animate[LEVEL_INDEX] == 0 and to_animate[STEP_INDEX] < 0:
            animating.remove(to_animate)
        
    sleep(10)

animations = [animation_0, animation_1, animation_2, animation_3, animation_4, animation_5]     

while True:
    if button_b.was_pressed():
        selected_animation = (selected_animation + 1) % len(animations)
        display.show(selected_animation)
        
    if button_a.was_pressed():
        selected_animation = (selected_animation - 1) % len(animations)
        display.show(selected_animation)
    
    animations[selected_animation]()
