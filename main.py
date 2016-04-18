from multiprocessing import *
from simulation import Simulation

class Main():
    def __init__(self):
        self.core_limit = 6
        self.jobs = []

    def run_simulations(self):
        for i in range(10):
            f = Simulation(i)
            self.jobs.append(f)
            f.start()
        for j in self.jobs:
            j.join()

    #
    # def make_road(self):
    #     self.main_road = Road(self.road_size)




if __name__ == "__main__":
    f = Main()
    f.run_simulations()

