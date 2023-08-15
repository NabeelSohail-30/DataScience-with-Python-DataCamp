import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

reviews = pd.read_csv('../datasets/lasvegas_tripadvisor.csv')

# Create a catplot for each "Period of stay" broken down by "Review weekday"
ax = sns.catplot(
  # Make sure Review weekday is along the x-axis
  x='Review weekday',
  # Specify Period of stay as the column to create individual graphics for
  col='Period of stay',
  # Specify that a count plot should be created
  kind='count',
  # Wrap the plots after every 2nd graphic.
  col_wrap=2,
  data=reviews
)
plt.show()

# Adjust the color
ax = sns.catplot(
  x="Free internet", y="Score",
  hue="Traveler type", kind="bar",
  data=reviews,
  palette=sns.color_palette('Set2')
)

# Add a title
ax.fig.suptitle("Hotel Score by Traveler Type and Free Internet Access")

# Update the axis labels
ax.set_axis_labels("Free Internet", "Average Review Rating")

# Adjust the starting height of the graphic
plt.subplots_adjust(top=.93)
plt.show()