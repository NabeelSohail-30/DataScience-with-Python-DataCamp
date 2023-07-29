import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from numpy import median

student_data = pd.read_csv('../datasets/student-alcohol-consumption.csv')

# Set the style for all plots
sns.set(style='whitegrid')

# Create a point plot of family relationship vs. absences
sns.catplot(x='famrel', y='absences', data=student_data, kind='point', palette='pastel')

# Add title and labels
plt.title('Family Relationship vs. Absences')
plt.xlabel('Family Relationship')
plt.ylabel('Absences')

# Show plot
plt.show()

# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences", data=student_data, kind="point", capsize=0.2, palette='pastel')

# Add title and labels
plt.title('Family Relationship vs. Absences')
plt.xlabel('Family Relationship')
plt.ylabel('Absences')

# Show plot
plt.show()

# Remove the lines joining the points
sns.catplot(x="famrel", y="absences", data=student_data, kind="point", capsize=0.2, join=False, palette='pastel')

# Add title and labels
plt.title('Family Relationship vs. Absences')
plt.xlabel('Family Relationship')
plt.ylabel('Absences')

# Show plot
plt.show()

# Create a point plot that uses color to create subgroups
sns.catplot(x='romantic', y='absences', data=student_data, kind='point', hue='school', palette='muted')

# Add title and labels
plt.title('Absences by Romantic Relationship Status')
plt.xlabel('Romantic Relationship')
plt.ylabel('Absences')

# Show plot
plt.show()

# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences", data=student_data, kind="point", hue="school", ci=None, palette='muted')

# Add title and labels
plt.title('Absences by Romantic Relationship Status')
plt.xlabel('Romantic Relationship')
plt.ylabel('Absences')

# Show plot
plt.show()

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences", data=student_data, kind="point", hue="school", ci=None, estimator=median, palette='muted')

# Add title and labels
plt.title('Median Absences by Romantic Relationship Status')
plt.xlabel('Romantic Relationship')
plt.ylabel('Median Absences')

# Show plot
plt.show()