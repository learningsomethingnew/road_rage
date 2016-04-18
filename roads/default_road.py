import numpy as np
from random import randint

class DefaultRoad:
    def __init__(self, max_size_road = 1000, curves=0):
        self.road = np.zeros(max_size_road)
        self.curve_chance = curves


    """Returns the curves distance."""
    def get_curve_distance(self):
        return (400, 600)

    def get_road_length(self):
        return len(self.road)

if __name__ == '__main__':
    f = DefaultRoad(100)


