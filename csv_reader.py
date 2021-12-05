import pandas as pd

# Add Data, create data frame, write to a file
data = {"x_value": [1, 2, 3, 40, 5, 23, 7, 8, 9], "y_value": [2, 6, 2, 2, 10, 2, 2, 0, 2]}
df = pd.DataFrame(data)
df.to_csv("data_csv.csv")

df = pd.read_csv("data_csv.csv", index_col=0)
print(df)
