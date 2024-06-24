import pandas as pd


# Multiline string containing the data
data=r"""
\documentclass{article}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{amsmath}
\begin{document}
\begin{tabular}{ll}
\toprule
Order_Status & Date_created \\
\midrule
fulfilled & 2023-01-01 0:37:08 \\
\bottomrule
\end{tabular}
\end{document}
"""


# Split lines and keep only the ones with data
lines = data.splitlines()
table_lines = [line.strip() for line in lines if "&" in line and not line.startswith("%")]
clean_lines = [line.replace("\\\\", "") for line in table_lines]


# Separate the header and get columns
header_line = clean_lines[0]
columns = [col.strip() for col in header_line.split('&')]


# Fill data rows
data = []

for line in clean_lines[1:]:
    row = [field.strip() for field in line.split('&')]
    data.append(row)


# Read the data into a DataFrame
df = pd.DataFrame(data, columns=columns)

print(df)
