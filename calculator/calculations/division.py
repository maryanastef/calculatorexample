""" Division Class"""
# namespace
from calculator.calculations.calculation import Calculation


class Division(Calculation):
    """"Division calculation object"""
    def get_result(self):
        """get the division results"""
        result = 1.0
        for value in self.values:
            try:
                result = result / value
            except ZeroDivisionError as error:
                raise ZeroDivisionError from error
