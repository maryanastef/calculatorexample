"""Testing the Calculator"""
import pandas as pd
from calc.calculator import Calculator


def test_calculator_add(clear_history_fixture):
    """testing the add function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers((1, 2, 3)) == 6


def test_calculator_subtract(clear_history_fixture):
    """Testing the subtract function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_numbers((20, 4, 9)) == 7


def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiplication function of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers((4, 7, 1)) == 28


def test_calculator_divide_static(clear_history_fixture):
    """ Testing the division function of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers((20, 4, 0)) == "Cannot divide by zero"
