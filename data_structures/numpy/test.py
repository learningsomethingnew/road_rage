import numpy as np
from fps.fps import start_fps
from data_structures.mod_queue import ModQueue

a = np.zeros(30)
# add 1's
run = True

b = a.size-1

loop = True

a[b] = 8

def redraw_frames():
    a[:] = 0

def set_speed(a_current_speed, a_top_speed):
    print("Current speed = {}".format(a_current_speed))
    accel = 2
    if a_current_speed > a_top_speed:
        print("MAX SPEED HIT")
        return (a_current_speed - (a_current_speed - a_top_speed))
    else:
        print("Adding to speed ", a_current_speed + accel)

        return a_current_speed + accel

def car_update(slot, speed, top_speed):
    if slot <= 0:
        slot = a.size - 1
        return slot
    else:
        speed = set_speed(speed, top_speed)
        slot -= speed
    return slot

def draw_car(slot, symbol):
    a[slot] = symbol

def draw_road():
    print(a)


speed = 0
top_speed = 33

while loop:

    draw_road()

    if start_fps():
        redraw_frames()

        b = car_update(b, speed, top_speed)

        draw_car(b, 8)


#print("Loop = {} After Loop\n B = {}, C = {}, D = {}, E= {}, F = {}".format(loop, b, c, d, e, f))



