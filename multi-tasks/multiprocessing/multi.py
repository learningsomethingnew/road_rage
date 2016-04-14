import multiprocessing
import logging
import sys
import time
from random import randint

class Worker(multiprocessing.Process):

    def run(self):
        name = multiprocessing.current_process().name
        print('Doing some work')
        print("{} Starting".format(name))
        print('Worker:', )
        time.sleep(randint(1,5))
        sys.stdout.flush()
        print("{} Exiting".format(name))

if __name__ == '__main__':
    jobs = []
    multiprocessing.log_to_stderr(logging.DEBUG)
    print(multiprocessing.cpu_count())
    for i in range(8):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()