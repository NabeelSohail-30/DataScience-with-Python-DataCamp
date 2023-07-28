import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

student_data = pd.read_csv('../datasets/student-alcohol-consumption.csv')

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x='absences', y='G3', data=student_data, hue='location')
plt.xlabel("Absences")
plt.ylabel("Final Grade")
plt.title("Absences vs. Final Grade with Location")
plt.show()

# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3",
                data=student_data, kind='scatter')

# Show plot
plt.show()

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            col="study_time")

# Show plot
plt.show()

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            row="study_time")

# Show plot
plt.show()

# Create a scatter plot of G1 vs. G3
sns.relplot(x='G1', y='G3', data=student_data, kind='scatter')

# Show plot
plt.show()

# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col='schoolsup',
            col_order=[
                "yes", "no"
            ])

# Show plot
plt.show()

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=["yes", "no"],
            row='famsup',
            row_order=[
                "yes", "no"
            ])

# Show plot
plt.show()