"""Testing the Calculator"""
import pytest

from calculator.main import Calculator
import pprint


@pytest.fixture
def clear_history():
    Calculator.clear_history()


def test_calculator_adding(clear_history):
    """Testing the addition"""
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.adding_numbers(3, 2) == 5
    assert Calculator.adding_numbers(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)


def test_clear_history(clear_history):
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.adding_numbers(3, 2) == 5
    assert Calculator.adding_numbers(4, 2) == 6
    assert Calculator.history.count() == 4
    assert Calculator.clear_history() == True
    assert Calculator.history.count() == 0


def test_count_history(clear_history):
    assert Calculator.history_count() == 0
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.history_count() == 2

def test_get_last_calculation_result(clear_history):
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 4

def test_get_first_calculation_result(clear_history):
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.get_result_of_first_calculation_added_to_history() == 3


def test_calculator_subtracting(clear_history):
    """Testing the subtraction"""
    assert Calculator.subtracting_numbers(1, 2) == -1


def test_calculator_multiplying(clear_history):
    """Testing multiplication of two numbers"""
    assert Calculator.multiplying_numbers(1, 2) == 2


def test_calculator_dividing(clear_history):
    """Testing division of two numbers"""
    assert Calculator.dividing_numbers(4, 2) == 2
