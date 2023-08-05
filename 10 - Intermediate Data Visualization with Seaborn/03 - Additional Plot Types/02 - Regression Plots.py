import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../datasets/schoolimprovement2010grants.csv')

# Display a regression plot for Tuition
sns.regplot(data=df,
         y='Tuition',
         x='SAT_AVG_ALL',
         marker='^',
         color='g')

plt.show()
plt.clf()


# Display the residual plot
sns.residplot(data=df,
          y='Tuition',
          x='SAT_AVG_ALL',
          color='g')

plt.show()
plt.clf()

# Plot a regression plot of Tuition and the Percentage of Pell Grants
sns.regplot(data=df,
            y='Tuition',
            x='PCTPELL')

plt.show()
plt.clf()


# Create another plot that estimates the tuition by PCTPELL
sns.regplot(data=df,
            y='Tuition',
            x='PCTPELL',
            x_bins=5)

plt.show()
plt.clf()


# The final plot should include a line using a 2nd order polynomial
sns.regplot(data=df,
            y='Tuition',
            x='PCTPELL',
            x_bins=5,
            order=2)

plt.show()
plt.clf()


# Create a scatter plot by disabling the regression line
sns.regplot(data=df,
            y='Tuition',
            x='UG',
            fit_reg=False)

plt.show()
plt.clf()


# Create a scatter plot and bin the data into 5 bins
sns.regplot(data=df,
            y='Tuition',
            x='UG',
            x_bins=5)

plt.show()
plt.clf()


# Create a regplot and bin the data into 8 bins
sns.regplot(data=df,
         y='Tuition',
         x='UG',
         x_bins=8)

plt.show()
plt.clf()