import numpy as np
from random import randint

class Road:
    def __init__(self, max_size_road, curves=0):
        self.road = np.zeros(max_size_road)
        self.curve_chance = curves

    """Returns the curves distance."""
    def get_curve_distance(self):
        return (400, 600)



if __name__ == '__main__':
    f = Road(100)


