import pandas as pd


# Multiline string containing the data
data = """
| Order Status       | Date created       |
|:-------------------|:-------------------|
| fulfilled          | 2023-01-01 0:37:08 |
…
"""


# Splitting the data into rows and removing any leading/trailing whitespace characters.
rows = data.strip().split('\n')


# Extracting the header and data rows.
header = [h.strip() for h in rows[0].split('|')]
data_rows = [[value.strip() for value in row.split('|')] for row in rows[2:]]


# Creating a DataFrame using the extracted data.
df = pd.DataFrame(data_rows, columns=header)

print(df)
