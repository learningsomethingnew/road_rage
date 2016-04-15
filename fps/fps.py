##########################################################
# FPS tool that will return True when 1 second has passed
##########################################################

import time



def fps_controller(start, ticks):
    while True:
        elapsed = time.time() - start
        if elapsed >= 1:
            start = time.time()
            ticks += 1
            print('1 sec elapsed, update! {}'.format(ticks))
            return True


def start_fps():
    start = time.time()
    ticks = 0
    return fps_controller(start, ticks)
