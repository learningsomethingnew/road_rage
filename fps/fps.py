##########################################################
# FPS tool that will return True when 1 second has passed
##########################################################

import time

start = time.time()

ticks = 0

def fps_controller(start, ticks):
    while True:
        elapsed = time.time() - start
        if elapsed >= 1:
            start = time.time()
            print("Start in if: ", start)
            ticks += 1
            print('1 sec elapsed, update! {}'.format(ticks))
            return True


fps_controller(start, ticks)