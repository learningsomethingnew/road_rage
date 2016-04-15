from fps.fps import start_fps

class Main:
    def __init__(self):
        self.main_loop()
        self.one_km_road = []

    def main_loop(self):
        m_loop = True
        while m_loop:
            if start_fps():
                self.do_something()


    def do_something(self):
        print("I did something")

    def driver_on_road(self):
        pass

    def make_road(self):
        for num in range(100):
            self.one_km_road.append(0)


if __name__ == "__main__":
    f = Main()

