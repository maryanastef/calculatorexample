""" Calculation Class"""


class Calculation:
    """Calculation abstract base class"""
    # pylint: disable=too-few-public-methods
    def __init__(self, values: tuple):
        """Constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    @classmethod
    # CLass Factory Method
    def create(cls, values: tuple):
        return cls(values)

    @staticmethod
    def convert_args_to_tuple_of_float(values):
        """Standardize values to lists of floats"""
        # tuples are faster than lists
        # convert tuple into standard data format by converting it into float
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
