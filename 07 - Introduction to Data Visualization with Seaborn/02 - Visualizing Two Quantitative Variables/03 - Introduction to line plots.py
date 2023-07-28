import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

mpg = pd.read_csv('../datasets/mpg.csv')

# Create line plot showing the trend of MPG over the years
sns.relplot(x='model_year', y='mpg', data=mpg, kind='line')
plt.xlabel('Model Year')
plt.ylabel('Miles Per Gallon (MPG)')
plt.title('MPG Trend Over the Years')
plt.show()

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg", data=mpg, kind="line", ci='sd')
plt.xlabel('Model Year')
plt.ylabel('Miles Per Gallon (MPG)')
plt.title('MPG Trend Over the Years with Standard Deviation')
plt.show()

# Create line plot of model year vs. horsepower without confidence intervals
sns.relplot(x='model_year', y='horsepower', data=mpg, kind='line', ci=None)
plt.xlabel('Model Year')
plt.ylabel('Horsepower')
plt.title('Horsepower Trend Over the Years')
plt.show()

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", data=mpg, kind="line", ci=None, style='origin', hue='origin')
plt.xlabel('Model Year')
plt.ylabel('Horsepower')
plt.title('Horsepower Trend Over the Years with Origin Differentiation')
plt.show()

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", data=mpg, kind="line", ci=None, style="origin", hue="origin", markers=True, dashes=False)
plt.xlabel('Model Year')
plt.ylabel('Horsepower')
plt.title('Horsepower Trend Over the Years with Origin Differentiation and Markers')
plt.show()