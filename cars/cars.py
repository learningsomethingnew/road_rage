from random import randint
import numpy as np


class DefaultCar():
    def __init__(self, name, a_position, a_max_speed=30, a_current_speed=0, a_length=5, a_accel_rate=2):
        self.position = a_position
        self.name = name
        self.max_speed = a_max_speed
        self.current_speed = a_current_speed
        self.length = a_length
        self.acceleration = a_accel_rate

        # Stats
        self.speed_array = []
        self.close_to_front = []

    """Returns name of car"""
    def get_name(self):
        return self.name

    """Returns tuple of back to front coordinates of the car"""

    def get_bumper(self):
        car_bumpers = np.arange(self.position - self.length, self.position + self.current_speed)
        return car_bumpers

    """Looks ahead of the car to verify clear. Returns true if road is clear"""

    def road_clear(self, next_car):
        if np.in1d(self.get_bumper(), next_car).any():
            return False
        else:
            return True

    """Sets the speed for the car"""

    def position_update(self, road_length, next_car_pos):
        # Check to see if car needs to loop
        if self.car_loop_road(road_length) and self.road_clear(next_car_pos):
            # if it does, warps the car with correct position
            loop_position = abs((self.position + self.current_speed) - road_length)
            self.position = loop_position
        elif self.road_clear(next_car_pos):
            self.position += self.car_speed_check()
        else:
            self.current_speed = self.decel()
            self.position = self.position

    """Position check to see if the car need to loop"""

    def car_loop_road(self, road_length):
        next_position = self.position + self.current_speed
        if next_position > road_length:
            print("Loop = True")
            return True

    """Manages the acceleration, decel, and top speed."""

    def car_speed_check(self):
        # If the slow down == True, checks to make sure the car doesn't go reverse
        if self.chance_slow_down():
            print("Chance to Slow = True ")
            return self.decel()
        # Check to see if near top_speed
        elif (self.current_speed + self.acceleration) >= self.max_speed:
            print("Max Speed")
            self.current_speed = self.max_speed
            self.speed_array.append(self.current_speed)
            return self.current_speed
        # Otherwise, speed up
        else:
            self.current_speed += self.acceleration
            print("acceleration, ", self.current_speed)
            self.speed_array.append(self.current_speed)
            return self.current_speed

    """Decels the car if random is true"""

    def decel(self):
        self.current_speed -= self.acceleration
        self.speed_array.append(self.current_speed)
        return self.current_speed

    """Roll of the die to determine if driver slows down, if over a certain speed"""

    def chance_slow_down(self):
        if self.current_speed > 10 and randint(1, 10) == 1:
            return True

    def __str__(self):
        return "{} is @ checking ahead {}, with speed of {}".format(self.name, self.get_bumper(), self.current_speed)


########################## Stats #########################################

    """Returns np array of all speeds"""
    def get_speed_array(self):
        temp = np.array(self.speed_array)
        return temp

    """Returns np array of close encounters"""
    def get_too_close(self):
        temp = np.array(self.close_to_front)
        return temp


if __name__ == '__main__':
    f = DefaultCar('Car1', 30)
    print(f.get_bumper())
    a = np.arange(29, 34)
    f.road_clear(a)
