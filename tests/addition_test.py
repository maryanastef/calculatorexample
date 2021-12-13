
"""Testing Addition"""
from calc.calculations.addition import Addition


def test_calculation_addition(mynum):
    """testing that our calculator has a static method for addition"""
    # Arrange
    mynum = (1.0, 2.0)
    addition = Addition(mynum)
    # Act
    # Assert
    assert addition.get_result() == 3.0