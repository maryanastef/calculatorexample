""" Calculation History Class """
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


class Calculations:
    """ Calculations class manages the history of calculations"""
    history = []
    # pylint: disable=too-few-public-methods

    # method to write history to a csv file
    @staticmethod
    def read_history_from_csv():
        """Read history from csv"""

        return Calculations.read_history_from_csv()

    @staticmethod
    def write_history_to_csv():
        """Write history to csv"""

    @staticmethod
    def clear_history():
        """Clear the history of the calculator"""
        Calculations.history.clear()
        return True

    @staticmethod
    def history_count():
        """Get number of items in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """Get last calculation"""
        return Calculations.history[-1].get_result()

    @staticmethod
    def get_first_calculation():
        """Get first calculation"""
        return Calculations.history[0].get_result()

    @staticmethod
    def get_calculation(num):
        """get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """Get a generic calculation from history"""
        Calculations.history.append(calculation)
        return True

    @staticmethod
    def add_addition_calculation_to_history(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation_to_history(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation_to_history(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation_to_history(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True

    @staticmethod
    def get_calc_result_history():
        """This returns a list of results """
        results = []
        for item in Calculations.history:
            results.append(item.get_result())
        return results

# retrieve back the history, send this to table
# convert data frame into correct format to be printed
# table data in a dictionary , method on history that returns back a dictionary
    @staticmethod
    def data_to_table():
        data_dict = {}
        for item in Calculations.history:
            data_dict[item] = str(item)
        return data_dict
