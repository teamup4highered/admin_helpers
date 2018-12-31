# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
mydir='app_excel2txt'
myfile = 'test_input.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(mydir + '\\' + myfile)

# Find the sheet names
sheetnames = xl.sheet_names

# Loop over all sheets in the file
for isheet in sheetnames:
    # read data into a dataframe
    #df1 = xl.parse(isheet)
    df1= xl.parse(isheet, header=0)

    # find dataframe size
    myshape=df1.shape

    #find column names
    mycolumns=list(df1)
# print(df1)
# print("------")
#  for row in df1.itertuples():
#     print(row)
# print(df1.iloc[1][1])