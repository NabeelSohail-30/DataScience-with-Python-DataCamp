import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mpg = pd.read_csv('../datasets/mpg.csv')
survey_data = pd.read_csv('../datasets/young-people-survey-responses.csv')

# Set the style to "whitegrid" and color palette to "Purples"
sns.set_style('whitegrid')
sns.set_palette('Purples')

# Create a count plot of survey responses for "Parents Advice"
sns.catplot(x="Parents' advice", data=survey_data, kind="count")
plt.title("Survey Responses for Parents Advice")
plt.show()

# Change the color palette to "RdBu"
sns.set_palette("RdBu")

# Create a count plot of survey responses for "Parents Advice"
sns.catplot(x="Parents' advice", data=survey_data, kind="count")
plt.title("Survey Responses for Parents Advice")
plt.show()

# Set the context to "paper"
sns.set_context('paper')

# Create bar plot of "Feels Lonely" vs. "Number of Siblings"
sns.catplot(x="Siblings", y="Loneliness", data=survey_data, kind="bar")
plt.title("Loneliness vs. Number of Siblings (Paper Context)")
plt.show()

# Change the context to "notebook"
sns.set_context("notebook")

# Create bar plot of "Feels Lonely" vs. "Number of Siblings"
sns.catplot(x="Siblings", y="Loneliness", data=survey_data, kind="bar")
plt.title("Loneliness vs. Number of Siblings (Notebook Context)")
plt.show()

# Change the context to "talk"
sns.set_context("talk")

# Create bar plot of "Feels Lonely" vs. "Number of Siblings"
sns.catplot(x="Siblings", y="Loneliness", data=survey_data, kind="bar")
plt.title("Loneliness vs. Number of Siblings (Talk Context)")
plt.show()

# Change the context to "poster"
sns.set_context("poster")

# Create bar plot of "Feels Lonely" vs. "Number of Siblings"
sns.catplot(x="Siblings", y="Loneliness", data=survey_data, kind="bar")
plt.title("Loneliness vs. Number of Siblings (Poster Context)")
plt.show()

# Set the style to "darkgrid" and a custom color palette
sns.set_style('darkgrid')
sns.set_palette(["#39A7D0", "#36ADA4"])

# Create a box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", data=survey_data, kind="box")
plt.title("Age Distribution by Gender")
plt.show()

# Create scatter plot of "weight" vs. "horsepower" from the 'mpg' dataset
g = sns.relplot(x="weight", y="horsepower", data=mpg, kind="scatter")
g.fig.suptitle("Car Weight vs. Horsepower")
plt.show()

# Create line plot of "model_year" vs. "mpg_mean" with 'origin' as hue
g = sns.lineplot(x="model_year", y="mpg", data=mpg, hue="origin")
g.set_title("Average MPG Over Time")
g.set(xlabel='Car Model Year', ylabel='Average MPG')
plt.show()

# Create point plot of "origin" vs. "acceleration" from the 'mpg' dataset
sns.catplot(x="origin", y="acceleration", data=mpg, kind="point", join=False, capsize=0.1)
plt.xticks(rotation=90)
plt.title("Acceleration by Car Origin")
plt.show()

# Set palette to "Blues" and create a box plot with subgroups based on "Interested in Pets"
sns.set_palette('Blues')
g = sns.catplot(x="Gender", y="Age", data=survey_data, kind="box", hue='Pets')
g.fig.suptitle("Age of Those Interested in Pets vs. Not", y=1.02)
plt.show()

# Set the figure style to "dark" and create subplots per gender
sns.set_style('dark')
g = sns.catplot(x="Village - town", y="Techno", data=survey_data, kind="bar", col='Gender')
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", ylabel="% Who Like Techno")
plt.show()