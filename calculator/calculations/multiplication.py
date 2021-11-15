""" Multiplication calculation that inherits the value_x and value_y from the class"""
# namespace
from calculator.calculations.calculation import Calculation


class Multiplication(Calculation):
    """"Multiplication class has one method to get the result"""
    def get_result(self):
        """referencing data contained in the instance of the object"""
        return self.value_x * self.value_y
