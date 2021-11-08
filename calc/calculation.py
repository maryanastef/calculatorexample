""" Parent class for calculations"""


class Calculation:
    """Calculation Class"""
    # constructor with encapsulation
    def __init__(self, value_x, value_y):
        self.value_x = value_x
        self.value_y = value_y


    @classmethod
    # CLass Factory Method
    def create(cls, value_x, value_y):
        return cls(value_x, value_y)
