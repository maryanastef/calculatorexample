import os
import pandas as pd


class Read:
    @staticmethod
    def df_from_csv_file(filename):
        return pd.read_csv(os.path.abspath(filename))
