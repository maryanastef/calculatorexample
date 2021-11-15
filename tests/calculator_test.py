"""Testing the Calculator"""
import pprint
import pytest
from calculator.calculator import Calculator


@pytest.fixture
def clear_history():
    Calculator.clear_history()


def test_calculator_adding():
    """Testing the addition"""
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.adding_numbers(3, 2) == 5
    assert Calculator.adding_numbers(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)


def test_clear_history():
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.adding_numbers(3, 2) == 5
    assert Calculator.adding_numbers(4, 2) == 6
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    assert Calculator.clear_history() is True


def test_count_history():
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.history_count() == 2
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0


def test_get_last_calculation_result():
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 4


def test_get_first_calculation_result():
    assert Calculator.adding_numbers(1, 2) == 3
    assert Calculator.adding_numbers(2, 2) == 4
    assert Calculator.get_result_of_first_calculation_added_to_history() == 3


def test_calculator_subtracting():
    """Testing the subtraction"""
    assert Calculator.subtracting_numbers(4, 2) == 2
    assert Calculator.subtracting_numbers(1, 2) == -1
    assert Calculator.subtracting_numbers(3, 2) == 1
    assert Calculator.subtracting_numbers(1, 1) == 0
    assert Calculator.history_count() == 8
    assert Calculator.get_result_of_last_calculation_added_to_history() == 0
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0


def test_calculator_multiplying():
    """Testing multiplication of two numbers"""
    assert Calculator.multiplying_numbers(4, 2) == 8
    assert Calculator.multiplying_numbers(1, 2) == 2
    assert Calculator.multiplying_numbers(3, 2) == 6
    assert Calculator.multiplying_numbers(2, 2) == 4
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 4
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0


def test_calculator_dividing():
    """Testing division of two numbers"""
    assert Calculator.dividing_numbers(4, 2) == 2
    assert Calculator.dividing_numbers(1, 1) == 1
    with pytest.raises(ZeroDivisionError):
        Calculator.dividing_numbers(1, 0)
        print("Cannot divide by zero")
