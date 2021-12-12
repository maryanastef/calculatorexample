import os
import pandas as pd


class Read:
    @staticmethod
    def df_from_csv_file(filename):
        return pd.read_csv(os.path.abspath(filename))

    @staticmethod
    def read_csv_to_history(history):
        return pd.read_csv(history)
