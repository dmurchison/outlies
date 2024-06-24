import pandas as pd
from io import StringIO


# Multiline string containing the data
data = """<?xml version='1.0' encoding='utf-8'?>
<root>
<item><Order_Status>fulfilled</Order_Status><Date_created>2023-01-01 0:37:08</Date_created></item>
</root>
"""

# Use StringIO to convert the string data into a file-like object
data_io = StringIO(data)

# Read the XML data using Pandas
df = pd.read_xml(data_io)

print(df)
