import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

divorce = pd.read_csv('../datasets/divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

# Create the scatterplot
sns.scatterplot(x='marriage_duration', y='num_kids', data=divorce)
plt.show()

# Create a pairplot for income_woman and marriage_duration
sns.pairplot(data=divorce, vars=['income_woman','marriage_duration'])
plt.show()