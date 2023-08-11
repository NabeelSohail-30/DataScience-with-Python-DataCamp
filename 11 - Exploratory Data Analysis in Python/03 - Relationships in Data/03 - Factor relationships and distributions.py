import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

divorce = pd.read_csv('../datasets/divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

# Create the scatter plot
sns.scatterplot(x='woman_age_marriage', y='income_woman', data=divorce, hue='education_woman')
plt.show()

# Update the KDE plot to show a cumulative distribution function
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0, cumulative=True)
plt.show()