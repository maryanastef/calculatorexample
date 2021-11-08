""" Division calculation that inherits the value_x and value_y from the class"""
# namespace
from calc.calculation import Calculation


class Division(Calculation):
    """"Division class has one method to get the result"""
    def getResult(self):
        # referencing data contained in the instance of the object
        while True:
            if self.value_y == 0 or self.value_x == 0:
                print("Cannot divide by zero")
            else:
                return self.value_x / self.value_y
