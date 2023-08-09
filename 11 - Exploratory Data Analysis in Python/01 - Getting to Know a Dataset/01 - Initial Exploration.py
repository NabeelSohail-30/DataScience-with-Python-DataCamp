import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

unemployment = pd.read_csv('../datasets/clean_unemployment.csv')

# Print the first five rows of unemployment
print(unemployment.head())

# Print a summary of non-missing values and data types in the unemployment DataFrame
print(unemployment.info())

# Print summary statistics for numerical columns in unemployment
print(unemployment.describe())

# Count the values associated with each continent in unemployment
print(unemployment.value_counts('continent'))

# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(data=unemployment, x='2021', binwidth=1)
plt.show()