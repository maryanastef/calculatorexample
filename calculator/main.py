""" Increment Function"""
# importing the addition namespace
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division


class Calculator:
    """ history is a numbered list of calculations"""
    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        return Calculator.history[0].get_result()

    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        # -1 gets the last item added to the list automatically
        return Calculator.history[-1].get_result()

    @staticmethod
    def adding_numbers(value_x, value_y):
        """ adds number to result"""
        # create an addition object
        Calculator.add_calculation_to_history(Addition.create(value_x, value_y))
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtracting_numbers(value_x, value_y):
        """ subtract number from result"""
        # create a subtraction object
        Calculator.add_calculation_to_history(Subtraction.create(value_x, value_y))
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiplying_numbers(value_x, value_y):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(Multiplication.create(value_x, value_y))
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def dividing_numbers(value_x, value_y):
        """ divide two numbers and store the result"""
        Calculator.add_calculation_to_history(Division.create(value_x, value_y))
        return Calculator.get_result_of_last_calculation_added_to_history()
