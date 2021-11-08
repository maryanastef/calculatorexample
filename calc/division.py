""" Division calculation that inherits the value_x and value_y from the class"""
# namespace
from calc.calculation import Calculation


class Division(Calculation):
    """"Division class has one method to get the result"""
    def getResult(self):
        # referencing data contained in the instance of the object
        try:
            value_x = 1
            value_y = 0
            print(value_x / value_y)
        except ZeroDivisionError:
            print("Cannot divide by zero")
