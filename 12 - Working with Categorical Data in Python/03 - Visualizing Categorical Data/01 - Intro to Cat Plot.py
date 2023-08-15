import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

reviews = pd.read_csv('../datasets/lasvegas_tripadvisor.csv')

# Set the font size to 1.25
sns.set(font_scale=1.25)

# Set the background to "darkgrid"
sns.set_style('darkgrid')

# Create a boxplot
sns.catplot(y='Helpful votes', x='Traveler type', data=reviews, kind='box')

plt.show()