""" Increment Function"""
from calc.history.calculations import Calculations

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
    def add_numbers(tuple_values: tuple):
        """ adds list of numbers"""
        # create an addition object
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiplication number from result"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ division number from result"""
        Calculations.add_division_calculation(tuple_values)
        return True
