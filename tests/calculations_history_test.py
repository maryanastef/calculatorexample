"""Testing the Calculator"""
import pytest
import pandas as pd
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
    # You have to add the fixture function as a parameter to the test that you want to use it with


@pytest.fixture
def setup_calc_fixture():
    add_calc = Addition((10, 20))
    Calculations.add_calculation(add_calc)
    add_calc = Addition((1, 2))
    Calculations.add_calculation(add_calc)


def test_get_calculation_first(clear_history_fixture, setup_calc_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation() == 30


def test_get_calc_last_result_value(clear_history_fixture, setup_calc_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == 3


def test_history_count(clear_history_fixture, setup_calc_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.history_count() == 2


def test_get_history(clear_history_fixture, setup_calc_fixture):
    """This should be a list of values from the history"""
    assert Calculations.history_count() == 2
    history_list = Calculations.get_calc_result_history()
    assert len(history_list) == 2
    assert history_list[0] == 30
    assert history_list[-1] == 3


def test_clear_calculation_history(clear_history_fixture, setup_calc_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.history_count() == 2
    Calculations.clear_history()
    assert Calculations.history_count() == 0
    assert Calculations.clear_history() is True
