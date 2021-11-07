""" increment function"""


class Calculator:
    """ created calculator class"""

    result = 0

    def get_result(self):
        """ getting result of calculation"""
        return self.result

    def adding_numbers(self, value_x):
        """ adds number to result"""
        self.result = self.result + value_x
        return self.result

    def subtracting_numbers(self, value_x):
        """ subtract number from result"""
        self.result = self.result - value_x
        return self.result

    def multiplying_numbers(self, value_x, value_y):
        """ multiply two numbers and store the result"""
        self.result = value_x * value_y
        return self.result

    def dividing_numbers(self, value_x, value_y):
        """ divide two numbers and store the result"""
        self.result = value_x / value_y
        return self.result
    try:
        value_x = 1
        value_y = 0
        print(value_x/value_y)
    except ZeroDivisionError:
        print("Cannot divide by zero")
