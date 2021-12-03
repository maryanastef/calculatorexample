import pandas as pd
import numpy as np
from calc.calculator import Calculator
import time
import os


class CsvReader:
    """This is the CsvReader Class"""

    calc_log =np.array([])

    @staticmethod
    def write_to_csv(numpy_array):
        # np.savetxt("calc_log.csv", numpy_array, delimiter=",")
        df = pd.DataFrame(numpy_array, columns= ['Rec_Num', 'Unix Time', 'Filename', 'Operation', 'Result'])
        # noinspection PyTypeChecker
        df.to_csv(r'calc_log.csv', index= False)


    @staticmethod
    def create_calc_log(rec_num, utime, filename, operation, result):
        temp_array = np.array([rec_num, utime, filename, operation, result])
        if len(CsvReader.calc_log) == 0:
            CsvReader.calc_log = np.append(CsvReader.calc_log, temp_array)
        else:
            CsvReader.calc_log = np.vstack([CsvReader.calc_log, temp_array])

    @staticmethod
    def do_calcs (rec_num, row_array, func, calc_type, filename):
        result = func(row_array)
        if type(result) == str:
            print("error = " + result)
        CsvReader.create_calc_log(rec_num, time.time(), filename, calc_type, result)

    def process_csv(self, nump_arr, filename : str):
        rows, columns = nump_arr.shape
        absolute_path = os.path.abspath(__file__)
        print("Full path from pandas_csv_test: " + absolute_path)

        for row in range(rows):
            CsvReader.do_calcs((row * 4)+0, nump_arr[row][1:], Calculator.add, "Addition", filename)
            CsvReader.do_calcs((row * 4)+1, nump_arr[row][1:], Calculator.subtract, "Subtraction", filename)
            CsvReader.do_calcs((row * 4)+2, nump_arr[row][1:], Calculator.multiply, "Multiplication", filename)
            CsvReader.do_calcs((row * 4)+3, nump_arr[row][1:], Calculator.divide, "Division", filename)
        print("calc_log:")
        print(CsvReader.calc_log)
        print("Writing to CSV")
        CsvReader.write_to_csv(CsvReader.calc_log)
        print('done')

    def read_csv_file(self, eventsrcpath: str):
        print("***pandas_csv.py***")
        df = pd.read_csv(eventsrcpath)
        print(df.columns)
        nump_arr = df.to_numpy()
        print("***Numpy array:***")
        print(nump_arr)
        return nump_arr
