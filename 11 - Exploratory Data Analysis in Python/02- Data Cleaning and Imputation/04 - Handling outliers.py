import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

planes = pd.read_csv('../datasets/planes.csv')

# Plot a histogram of flight prices
sns.histplot(x='Price', data=planes)
plt.show()

# Display descriptive statistics for flight duration
print(planes['Duration'].describe())

# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

# Subset the data
planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]

print(planes["Price"].describe())