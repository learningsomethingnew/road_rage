import multiprocessing
import logging
import sys
import time
from random import randint
from simulation import Simulation

class Worker(multiprocessing.Process):
    def __init__(self, sim_num):
        self.sim_num = sim_num

    def run(self):
        name = multiprocessing.current_process().name
        Simulation(self.sim_num)
        sys.stdout.flush()
        print("{} Exiting".format(name))

if __name__ == '__main__':
    jobs = []
    multiprocessing.log_to_stderr(logging.DEBUG)
    print(multiprocessing.cpu_count())
    for i in range(8):
        p = Worker(i)
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()