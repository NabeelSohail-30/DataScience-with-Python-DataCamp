import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

unemployment = pd.read_csv('../datasets/clean_unemployment.csv')

# Print the mean and standard deviation of rates by year
print(unemployment.agg(["mean", "std"]))

# Print yearly mean and standard deviation grouped by continent
print(unemployment.groupby('continent').agg(["mean", "std"]))

continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021 = ("2021", "mean"),
    # Create the std_rate_2021 column
    std_rate_2021 = ("2021", "std"),
)
print(continent_summary)

# Create a bar plot of continents and their average unemployment
sns.barplot(data=unemployment, x='continent', y='2021')
plt.show()