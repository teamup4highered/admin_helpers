# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'test_input.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')
print(df1)
print("------")
for row in df1.itertuples():
    print(row)
print(df1.iloc[1][1])