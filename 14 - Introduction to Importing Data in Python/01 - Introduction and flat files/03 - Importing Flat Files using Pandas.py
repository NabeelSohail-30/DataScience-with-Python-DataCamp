import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read Titanic data from a CSV file and view the first few rows
titanic_file = 'titanic.csv'
titanic_df = pd.read_csv(titanic_file)
print("Titanic DataFrame head:")
print(titanic_df.head())

# Read a subset of rows from a CSV file and convert to a numpy array
digits_file = 'digits.csv'
data_subset = pd.read_csv(digits_file, nrows=5, header=None)
data_array = np.array(data_subset)
print("Datatype of data_array:", type(data_array))

# Read corrupted data from a tab-separated text file and view the head
corrupt_file = 'titanic_corrupt.txt'
corrupt_data = pd.read_csv(corrupt_file, sep='\t', comment='#', na_values=['Nothing'])
print("Corrupted DataFrame head:")
print(corrupt_data.head())

# Plot a histogram of the 'Age' variable from the corrupted DataFrame
pd.DataFrame.hist(corrupt_data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()