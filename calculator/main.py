""" Increment Function"""
# importing the addition namespace
from calc.addition import Addition
from calc.subtraction import Subtraction


class Calculator:
    """ created calculator class"""
    history = []
    """ history is a numbered list of calculations"""
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
        return Calculator.history[-1].getResult()

    @staticmethod
    def adding_numbers(value_x, value_y):
        """ adds number to result"""
        # create an addition object
        addition = Addition.create(value_x, value_y)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtracting_numbers(value_x, value_y):
        """ subtract number from result"""
        # create a subtraction object
        subtraction = Subtraction.create(value_x, value_y)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiplying_numbers(value_x, value_y):
        """ multiply two numbers and store the result"""
        return value_x * value_y

    @staticmethod
    def dividing_numbers(value_x, value_y):
        """ divide two numbers and store the result"""
        return value_x / value_y
    try:
        value_x = 1
        value_y = 0
        print(value_x/value_y)
    except ZeroDivisionError:
        print("Cannot divide by zero")
