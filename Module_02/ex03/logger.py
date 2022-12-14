import time
from random import randint
import os
import datetime


def log(f):

    def wrapper(*args, **kwargs):
        name = f.__name__
        user = os.getlogin()
        start = time.time()
        val = f(*args, **kwargs)
        endM = (time.time() - start) * 1000
        endS = (time.time() - start)
        with open('machine.log', 'a') as file:
            if name == 'make_coffee' or name == 'add_water':
                file.write(
                    '({2})Running: {1} [exec-time = {0:.4f} s ]\n'.format(endS, name, user))
            else:
                file.write(
                    '({2})Running: {1} [exec-time = {0:.4f} ms ]\n'.format(endM, name, user))
        return val
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
