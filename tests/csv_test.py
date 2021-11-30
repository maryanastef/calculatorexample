import unittest
from csvreader.csvreader import ReadCSV


class CsvTest(unittest.TestCase):

    def setUp(self) = None:
        self.csv_reader = ReadCSV("C:/Users/maryanastef/PycharmProjects/calculatorexample/csvreader/addition_sample.csv")

    def test_return_data_as_object(self):
        people