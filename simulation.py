from roads.default_road import DefaultRoad
from cars.cars import DefaultCar
from data_structures.mod_queue import ModQueue
from fps.fps import start_fps
from os import *
import numpy as np

#######################################
# Manages the actual simulation. Intended to
# be multitasked.

#road_diff = Straight track course or the 4 curves track course
#######################################

class Simulation():

    def __init__(self, sim_number, a_num_cars=30, road_diff = 1):
        #kick off road creation
        self.num_of_roads = 7 #used in create_roads
        self.road_length = 1000
        self.road_setup(road_diff)

        #kick off car creation
        self.num_of_cars = a_num_cars
        self.car_queue = ModQueue(30)
        self.create_car()

        #Sim Parameters
        self.num_of_cycles = 10

        # track sim info
        self.sim_number = "{}/".format(sim_number)
        self.directory = '/Users/Nic/TIY/W3/road_rage/sim_stats/'
        self.directory = self.join_paths(self.directory, self.sim_number)
        self.create_dir(self.directory)


########################## Roads ########################################
    def road_setup(self, road_diff):
        # road dictionary for storing a more difficult course
        if road_diff == 1:
            self.road = self.create_roads(road_diff)
        else:
            self.road_dict = {}
            curve_list = [0, .4, 0, 1, 0, .2, 0]
            self.create_roads(road_diff)

    def create_roads(self, road_diff):
        if road_diff == 1:
            return DefaultRoad(self.road_length)
        else:
            for num in range(self.num_of_roads):
                temp_name = "r{}".format(num)
                self.road_dict[temp_name] = DefaultRoad(self.road_length)

########################## Cars #########################################

    def create_car(self):
        for num in range(self.num_of_cars):
            temp_name = "Car {}".format(num)
            self.car_queue.append_right(DefaultCar(temp_name, ((num*30)+5) ) )

    """Gets the cars moving"""
    def car_drive(self):
        for cars in range(self.car_queue.get_len_queue()):
            current_car = self.car_queue.pop()
            print(current_car)
            next_car = self.check_next_car_position()
            current_car.position_update(self.road_length, next_car)
            self.car_queue.append_right(current_car)
            self.check_car_position()

    """Returns the position of the car ahead"""
    def check_next_car_position(self):
        next_car_position = self.car_queue.peek_left().get_bumper()
        #next_car_name = self.car_queue.peek_left().get_name()
        #print("Peeking at Car {} @ position {}".format(next_car_name, next_car_position))
        return next_car_position

    """Test print for making sure that the cars work"""
    def check_car_position(self):
        current_car = self.car_queue.peek_right()
        print(current_car)



########################## Sim Loop ######################################

    def sim_loop(self):
        sim_loop = 0
        while sim_loop < self.num_of_cycles:
            if start_fps():
                self.car_drive()
            sim_loop +=1

        #Saves the stats for processing
        self.car_stats()


########################## Stats ######################################
    def car_stats(self):
        for num in range(self.car_queue.get_len_queue()):
            current_car = self.car_queue.pop()
            temp_name = current_car.get_name()
            temp_speed = current_car.get_speed_array()
            temp_too_close = current_car.get_too_close()
            self.write_to_file(temp_name, temp_speed)


    def join_paths(self, a_dir, a_file):
        return path.join(a_dir, a_file)

    def create_dir(self, a_dir):
        if not path.exists(a_dir):
            makedirs(a_dir)

    def write_to_file(self, temp_name, nparray):
        temp_dir = self.join_paths(self.directory, '{}.txt'.format(temp_name))
        np.savetxt(temp_dir, nparray[None], fmt='%i', delimiter=",")


if __name__ == '__main__':
    f = Simulation(1, 30, 1)
    f.sim_loop()

