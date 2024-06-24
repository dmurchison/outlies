import pandas as pd
from io import StringIO


# Multiline string containing the data
data = """
[{
  "Order Status": "fulfilled",
  "Date created": "2023-01-01 00:37:08"
}]
"""

# Use StringIO to convert the string data into a file-like object
data_io = StringIO(data)

# Read the JSON data using Pandas
df = pd.read_json(data_io)

print(df)
