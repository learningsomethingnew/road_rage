from collections import deque

class Road:
    def __init__(self, a_road_length):
        self.new_road = deque(maxlen=a_road_length)
        self.max_size = a_road_length

    def populate_empty_road(self):
        self.new_road.append(1)
        for num in range(self.max_size):
            self.new_road.append(0)
            print(self.new_road)

if __name__ == '__main__':
    f = Road(10)
    f.populate_empty_road()
    f.new_road.append(5)
    print(len(f.new_road))
    print(f.new_road)

