""" Addition Class"""
# namespace
from calc import Calculation


class Addition(Calculation):
    """Calculation Addition Class"""
    def get_result(self):
        """get the addition results"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
