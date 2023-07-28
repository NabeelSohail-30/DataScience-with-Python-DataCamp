import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

mpg = pd.read_csv('../datasets/mpg.csv')

# Create scatter plot of horsepower vs. mpg
sns.relplot(x='horsepower', y='mpg', data=mpg, kind='scatter', size='cylinders')
plt.xlabel('Horsepower')
plt.ylabel('Miles Per Gallon (MPG)')
plt.title('Horsepower vs. MPG')
plt.show()

# Create scatter plot of horsepower vs. mpg with different colors for each cylinder value
sns.relplot(x="horsepower", y="mpg",
            data=mpg, kind="scatter",
            size="cylinders",
            hue='cylinders')
plt.xlabel('Horsepower')
plt.ylabel('Miles Per Gallon (MPG)')
plt.title('Horsepower vs. MPG with Cylinder Differentiation')
plt.show()

# Create a scatter plot of acceleration vs. mpg with different markers and colors for each origin
sns.relplot(x='acceleration', y='mpg', data=mpg, kind='scatter', size='origin', hue='origin', style='origin')
plt.xlabel('Acceleration (0-60 mph time)')
plt.ylabel('Miles Per Gallon (MPG)')
plt.title('Acceleration vs. MPG with Origin Differentiation')
plt.show()