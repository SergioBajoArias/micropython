from microbit import *
import random

X_INDEX = 0
Y_INDEX = 1
LEVEL_INDEX = 2
STEP_INDEX = 3
MAX_ANIMATING = 15
STEP = 1

animating = []

def update():
    for to_animate in animating:
        to_animate[LEVEL_INDEX] = to_animate[LEVEL_INDEX] + to_animate[STEP_INDEX]
        
        if to_animate[LEVEL_INDEX] == 9:
            to_animate[STEP_INDEX] = -to_animate[STEP_INDEX]
        if to_animate[LEVEL_INDEX] == 0 and to_animate[STEP_INDEX] < 0:
            animating.remove(to_animate)

def render():
    for to_animate in animating:
        display.set_pixel(to_animate[X_INDEX], 
                          to_animate[Y_INDEX], 
                          to_animate[LEVEL_INDEX])
        
while True:
    if len(animating) < MAX_ANIMATING:
        x, y = random.randint(0, 4), random.randint(0, 4)
        animating.append([x, y, 0, STEP])

    render()
    update()

    sleep(100)
