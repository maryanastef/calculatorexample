""" Multiplication calculation that inherits the value_x and value_y from the class"""
# namespace
from calc.calculation import Calculation


class Multiplication(Calculation):
    """"Multiplication class has one method to get the result"""
    def getResult(self):
        # referencing data contained in the instance of the object
        return self.value_x * self.value_y
