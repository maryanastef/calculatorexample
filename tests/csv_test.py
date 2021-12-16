import os

import pandas
import pandas as pd

from csvreader.read import Read
from csvreader.write import Write


def write_csv_test():
    """Testing the write method"""
    # arrange
    filename = "data_csv.csv"
    path = "tests/test_data"
    full_path = path + "/" + filename
    dictionary = {
        "value1" : ["1", "2", "3", "4"],
        "value2" : ["2", "6", "2", "2"],
        "result" : ["3", "8", "5", "6"]
    }

    # act
    df = pd.DataFrame(dictionary)
    Write.df_to_csv_file(full_path, df)

    #assert
    assert os.path.exists(full_path)


def test_read_csv():
    """Testing the read method"""
    # arrange
    filename = "data_csv.csv"
    path = "tests/test_data"
    full_path = path + "/" + filename

    # act
    df = Read.df_from_csv_file(full_path)

    # assert
    assert type(df) is pandas.DataFrame
