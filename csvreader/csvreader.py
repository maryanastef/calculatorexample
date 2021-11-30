import csv
import pandas as pd
from pathlib import Path

class ReadCSV:
    data = []
    def __init__(self,filepath):
        self.data=[]

    def get_df_from_csv(self,addition_sample.csv):
    # return a data frame with method called csv reader
        return pd.read_csv("addition_sample.csv")

class file_utilities:
    # takes filename in, uses API to get the absolute path and return it
    @staticmethod
    def absolutepath(filepath):
        relative = Path(filepath)
        return relative.absolute()