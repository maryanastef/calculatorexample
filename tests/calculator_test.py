"""Testing the Calculator"""
from calculator.main import Calculator
import pprint
"""importing Calculator Class"""


def test_calculator_adding():
    """Testing the addition"""
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.adding_numbers(3, 2) == 5
    assert Calculator.adding_numbers(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)


def test_calculator_subtracting():
    """Testing the subtraction"""
    assert Calculator.subtracting_numbers(1, 2) == -1


def test_calculator_multiplying():
    """Testing multiplication of two numbers"""
    assert Calculator.multiplying_numbers(1, 2) == 2


def test_calculator_dividing():
    """Testing division of two numbers"""
    assert Calculator.dividing_numbers(4, 2) == 2
