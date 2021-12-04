import pandas as pd


def csv_test():
    df = pd.read_csv(data="addition_sample.csv")
    print(df.to_string())
