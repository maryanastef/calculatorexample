"""Testing Addition"""
from calc.calculations.addition import Addition


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    # Arrange
    my_num = (1.0, 2.0)
    addition = Addition(my_num)
    # Act
    # Assert
    assert addition.get_result() == 3.0
