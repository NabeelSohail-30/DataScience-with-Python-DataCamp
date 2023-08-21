import pandas as pd
import matplotlib.pyplot as plt
from sas7bdat import SAS7BDAT

# Load SAS file into a pandas DataFrame
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print the head of the DataFrame
print("Head of df_sas:")
print(df_sas.head())

# Plot a histogram of a DataFrame feature
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()


# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame
print("Head of df:")
print(df.head())

# Plot a histogram of a column from the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()
