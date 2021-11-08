""" Division calculation that inherits the value_x and value_y from the class"""
# namespace
from calc.calculation import Calculation


class Division(Calculation):
    """"Division class has one method to get the result"""
    def get_result(self):
        # referencing data contained in the instance of the object
        try:
            return self.value_x / self.value_y
        except ZeroDivisionError as err:
            raise ZeroDivisionError from err
