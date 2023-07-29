import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the datasets
survey_data = pd.read_csv('../datasets/young-people-survey-responses.csv')
student_data = pd.read_csv('../datasets/student-alcohol-consumption.csv')

# Set the style for all plots
sns.set(style='whitegrid')

# Create count plot of internet usage
sns.catplot(x='Internet usage', data=survey_data, kind='count', palette='pastel')

# Add title and labels
plt.title('Internet Usage Frequency')
plt.xlabel('Internet Usage')
plt.ylabel('Count')

# Show plot
plt.show()

# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data, kind="count", palette='pastel')

# Add title and labels
plt.title('Internet Usage Frequency')
plt.xlabel('Count')
plt.ylabel('Internet Usage')

# Show plot
plt.show()

# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data, kind="count", col='Age', palette='pastel')

# Add title and labels
plt.subplots_adjust(top=0.8)  # Adjust the plot's title position
plt.suptitle('Internet Usage Frequency by Age Group')
plt.xlabel('Count')
plt.ylabel('Internet Usage')

# Show plot
plt.show()

# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender', y='Mathematics', kind='bar', data=survey_data, palette='muted')

# Add title and labels
plt.title('Interest in Mathematics by Gender')
plt.xlabel('Gender')
plt.ylabel('Interest in Mathematics')

# Show plot
plt.show()

# Create bar plot of average final grade in each study category
sns.catplot(x='study_time', y='G3', kind='bar', data=student_data, palette='muted')

# Add title and labels
plt.title('Average Final Grade by Study Time')
plt.xlabel('Study Time')
plt.ylabel('Average Final Grade')

# Show plot
plt.show()

# List of categories from lowest to highest
category_order = ["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]

# Rearrange the categories
sns.catplot(x="study_time", y="G3", data=student_data, kind="bar", order=category_order, palette='muted')

# Add title and labels
plt.title('Average Final Grade by Study Time')
plt.xlabel('Study Time')
plt.ylabel('Average Final Grade')

# Show plot
plt.show()

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3", data=student_data, kind="bar", order=category_order, ci=None, palette='muted')

# Add title and labels
plt.title('Average Final Grade by Study Time')
plt.xlabel('Study Time')
plt.ylabel('Average Final Grade')

# Show plot
plt.show()