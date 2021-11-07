"""calculator test"""

from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_adding():
    """Testing the addition"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    # Act by calling the method to be tested
    calc.adding_numbers(2)
    # Assert that the results are correct
    assert calc.result == 2

def test_calculator_subtracting():
    """Testing the subtraction"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    # Act by calling the method to be tested
    calc.subtracting_numbers(2)
    # Assert that the results are correct
    assert calc.get_result() == -2

def test_calculator_multiplying():
    """Testing multiplication of two numbers"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    # Act by calling the method to be tested
    result = calc.multiplying_numbers(2 ,2)
    # Assert that the results are correct
    assert result == 4

def test_calculator_dividing():
    """Testing division of two numbers"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    # Act by calling the method to be tested
    result = calc.dividing_numbers(2 ,2)
    # Assert that the results are correct
    assert result == 1
