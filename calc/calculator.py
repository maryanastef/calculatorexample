""" Increment Function"""
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division

# The calculator class just contains the methods to calculate


class Calculator:
    """ This is the Calculator Class"""
    # The calculator class just calls methods on Calculation Class
    @staticmethod
    def get_last_result_value():
        """This is the gets the result of the calculation"""
        # this method doesn't allow more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def add_numbers(values):
        """ adds list of numbers"""
        # create an addition object
        add = Addition(values)
        Calculations.add_addition_calculation(add)
        return Calculations.get_result()

    @staticmethod
    def subtract_numbers(values):
        """ subtract a list of numbers from result"""
        subtract = Subtraction(values)
        Calculations.add_subtraction_calculation(subtract)
        return Calculations.get_result()

    @staticmethod
    def multiply_numbers(values):
        """ multiplication number from result"""
        multiply = Multiplication(values)
        Calculations.add_multiplication_calculation(multiply)
        return Calculations.get_result()

    @staticmethod
    def divide_numbers(values):
        """ division number from result"""
        div = Division(values)
        Calculations.add_division_calculation(div)
        return Calculations.get_result()
