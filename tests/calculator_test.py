"""Testing the Calculator"""
import os
import sys
import pytest
import pandas as pd
from calc.calculator import Calculator
from calc.history.calculations import Calculations

# use pandas to read csv file, loop through csv file, call assert on each calculation

# setting a path
directory = os.getcwd()
path = os.path.dirname(directory)
sys.path.append(path)

# setting up current directory of files
test_data = os.path.dirname(os.path.abspath(__file__)) + "/test_data/"


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
# You have to add the fixture function as a parameter to the test that you want to use it with


def test_calculator_add(clear_history_fixture):
    """testing the add function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    addition = pd.read_csv(test_data + "addition_sample.csv")
    for item in range(len(addition)):
        Calculator.add_numbers(addition.loc[item]["value_x"], addition.loc[item]["value_y"])
        assert Calculator.get_last_result_value() == addition.loc[item]["result"]


def test_calculator_subtract(clear_history_fixture):
    """Testing the subtract function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    subtraction = pd.read_csv(test_data + "subtraction_sample.csv")
    for item in range(len(subtraction)):
        Calculator.subtract_numbers(subtraction.loc[item]["value_x"], subtraction.loc[item]["value_y"])
        assert Calculator.get_last_result_value() == subtraction.loc[item]["result"]


def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiplication function of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    multiplication = pd.read_csv(test_data + "multiplication_sample.csv")
    for item in range(len(multiplication)):
        Calculator.multiply_numbers(multiplication.loc[item]["value_x"], multiplication.loc[item]["value_y"])
        assert Calculator.get_last_result_value() == multiplication.loc[item]["result"]


def test_calculator_divide_static(clear_history_fixture):
    """ Testing the division function of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    division = pd.read_csv(test_data + "division_sample.csv")
    for item in range(len(division)):
        if item == 0:
            assert Calculator.get_last_result_value() == "Cannot divide by zero"
        else:
            Calculator.divide_numbers(division.loc[item]["value_x"], division.loc[item]["value_y"])
            assert Calculator.get_last_result_value() == division.loc[item]["result"]
