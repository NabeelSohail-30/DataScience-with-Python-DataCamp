# Get the actual responses
from statsmodels.graphics.mosaicplot import mosaic
actual_response = churn["has_churned"]

# Get the predicted responses
predicted_response = np.round(mdl_churn_vs_relationship.predict())

# Create outcomes as a DataFrame of both Series
outcomes = pd.DataFrame({"actual_response": actual_response,
                         "predicted_response": predicted_response})

# Print the outcomes
print(outcomes.value_counts(sort=False))

# Calculate the confusion matrix conf_matrix using .pred_table()
conf_matrix = mdl_churn_vs_relationship.pred_table()

# Print the confusion matrix
print(conf_matrix)

# Draw a mosaic plot of conf_matrix
mosaic(conf_matrix, title='Confusion Matrix')

# Show the mosaic plot
plt.show()
