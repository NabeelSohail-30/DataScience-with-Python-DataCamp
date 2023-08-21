import pickle
import pandas as pd

# Load pickled data from a file
with open('data.pkl', mode='rb') as file:
    d = pickle.load(file)

# Print the loaded data
print("Loaded data:")
print(d)

# Print the datatype of the loaded data
print("Datatype of loaded data:", type(d))


# Assign spreadsheet filename
file = 'battledeath.xlsx'

# Load the Excel spreadsheet using pandas
xls = pd.ExcelFile(file)

# Print sheet names
print("Sheet names:", xls.sheet_names)

# Load a specific sheet into a DataFrame by name
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print("Head of df1:")
print(df1.head())

# Load a specific sheet into a DataFrame by index
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print("Head of df2:")
print(df2.head())

# Parse the first sheet, skip rows, and rename columns
df1 = xls.parse(0, skiprows=1, names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print("Head of df1 (modified):")
print(df1.head())

# Parse the first column of the second sheet and rename the column
df2 = xls.parse(1, usecols={0}, skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print("Head of df2 (modified):")
print(df2.head())
