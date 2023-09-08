# Why you need logistic regression

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have your churn data loaded into a DataFrame called 'churn_data'

# Create the displot with col parameter to split histograms
sns.displot(data=churn, x="time_since_last_purchase",
            hue="has_churned", col="has_churned", bins=20, kde=True)

# Add labels and a title
plt.xlabel("Time Since Last Purchase")
plt.ylabel("Frequency")
# Adjust title position
plt.suptitle(
    "Distribution of Time Since Last Purchase (Churn vs. No Churn)", y=1.02)

# Show the plot
plt.show()

# Create the displot with col parameter to split histograms
sns.displot(data=churn, x="time_since_first_purchase",
            hue="has_churned", col="has_churned", bins=20, kde=True)

# Add labels and a title
plt.xlabel("Time Since First Purchase")
plt.ylabel("Frequency")
# Adjust title position
plt.suptitle(
    "Distribution of Time Since First Purchase (Churn vs. No Churn)", y=1.02)

# Show the plot
plt.show()
