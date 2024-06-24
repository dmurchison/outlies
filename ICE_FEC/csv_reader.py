import pandas as pd
from io import StringIO


# Multiline string containing the data
data = """
Order Status;Date created

fulfilled;2023-01-01 0:37:08
…
"""

# Use StringIO to convert the string data into a file-like object
data_io = StringIO(data)

# Read the CSV data using pandas, specifying the delimiter
df = pd.read_csv(data_io, delimiter=';')

print(df)
