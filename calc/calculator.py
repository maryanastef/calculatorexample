""" Increment Function"""
from idlelib import history

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
        Calculations.add_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiplication number from result"""
        Calculations.add_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ division number from result"""
        Calculations.add_calculation(tuple_values)
        return True

    @staticmethod
    def get_history():
        """Get history """
        return Calculations.history()

    @staticmethod
    def get_history_from_csv():
        """Get history from csv file"""
        return Calculations.read_history_from_csv()

    @staticmethod
    def write_history_to_csv():
        """Write history """
        return Calculations.write_history_to_csv()
