""" Calculation History Class """


class Calculations:
    """ Calculations class manages the history of calculations"""
    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def add_calculation(calculation):
        """Get a generic calculation from history"""
        Calculations.history.append(calculation)
        return True

    @staticmethod
    def get_first_calculation():
        """Get first calculation"""
        return Calculations.history[0].get_result()

    @staticmethod
    def get_last_calculation_result_value():
        """Get last calculation"""
        return Calculations.history[-1].get_result()

    @staticmethod
    def history_count():
        """Get number of items in history"""
        return len(Calculations.history)

    @staticmethod
    def get_calc_result_history():
        """This returns a list of results """
        results = []
        for item in Calculations.history:
            results.append(item.get_result())
        return results

    @staticmethod
    def clear_history():
        """Clear the history of the calculator"""
        Calculations.history.clear()
        return True

