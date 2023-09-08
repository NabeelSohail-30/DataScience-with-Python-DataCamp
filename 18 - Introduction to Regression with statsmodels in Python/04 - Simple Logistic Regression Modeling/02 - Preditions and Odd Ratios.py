# Create prediction_data and store predictions
prediction_data = explanatory_data.assign(
    has_churned=mdl_churn_vs_relationship.predict(explanatory_data)
)

# Print the first five lines of the prediction DataFrame
print(prediction_data.head())

fig = plt.figure()

# Create a scatter plot with logistic trend line
sns.regplot(data=churn, x="time_since_first_purchase", y="has_churned",
            logistic=True, scatter_kws={'s': 10}, line_kws={"color": "blue"})

# Overlay with prediction_data, colored red
sns.scatterplot(data=prediction_data,
                x="time_since_first_purchase", y="has_churned", color="red")

# Add labels and a title
plt.xlabel("Time Since First Purchase")
plt.ylabel("Has Churned")
plt.title("Scatter Plot of Has Churned vs. Time Since First Purchase")

plt.show()

# Update prediction data by adding most_likely_outcome
prediction_data["most_likely_outcome"] = np.round(
    prediction_data["has_churned"])

# Print the head
print(prediction_data.head())
