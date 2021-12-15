"""CSV Reader"""

import pandas as pd

# Add Data, create data frame, write to a file

# read csv file
# columns = ["Value1", "Value2", "Result"]
df = pd.read_csv("addition_sample.csv", index_col=0)

# save to html
df.to_html("table.htm")

html_file = df.to_html()
print(html_file)
