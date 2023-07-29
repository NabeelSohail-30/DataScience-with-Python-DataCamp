import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

student_data = pd.read_csv('../datasets/student-alcohol-consumption.csv')

# Set the style for all plots
sns.set(style='whitegrid')

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x='study_time', y='G3', data=student_data, kind='box', order=study_time_order, palette='pastel')

# Add title and labels
plt.title('Final Grade Distribution by Study Time')
plt.xlabel('Study Time')
plt.ylabel('Final Grade')

# Show plot
plt.show()

# Create a box plot with subgroups and omit the outliers
sns.catplot(x='internet', y='G3', data=student_data, kind='box', col='location', hue='location', palette='muted', sym='', dodge=False)

# Add title and labels
plt.subplots_adjust(top=0.8)  # Adjust the plot's title position
plt.suptitle('Final Grade Distribution by Internet Access and Location')
plt.xlabel('Internet Access')
plt.ylabel('Final Grade')

# Show plot
plt.show()

# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3", data=student_data, kind="box", whis=0.5, palette='pastel')

# Add title and labels
plt.title('Final Grade Distribution by Romantic Relationship Status')
plt.xlabel('Romantic Relationship')
plt.ylabel('Final Grade')

# Show plot
plt.show()

# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3", data=student_data, kind="box", whis=[5, 95], palette='pastel')

# Add title and labels
plt.title('Final Grade Distribution by Romantic Relationship Status')
plt.xlabel('Romantic Relationship')
plt.ylabel('Final Grade')

# Show plot
plt.show()

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3", data=student_data, kind="box", whis=[0, 100], palette='pastel')

# Add title and labels
plt.title('Final Grade Distribution by Romantic Relationship Status')
plt.xlabel('Romantic Relationship')
plt.ylabel('Final Grade')

# Show plot
plt.show()