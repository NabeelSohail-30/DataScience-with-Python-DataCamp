# Get the actual responses
from statsmodels.graphics.mosaicplot import mosaic
from statsmodels.formula.api import logit
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the churn dataset
churn = pd.read_csv('./datasets/churn.csv')

# Fit a logistic regression of churn vs. length of relationship using the churn dataset
formula = "has_churned ~ time_since_first_purchase"
mdl_churn_vs_relationship = logit(formula, data=churn).fit()

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

# Extract TN, TP, FN, and FP from conf_matrix
TN = conf_matrix[0, 0]
FP = conf_matrix[0, 1]
FN = conf_matrix[1, 0]
TP = conf_matrix[1, 1]

# Calculate the accuracy
accuracy = (TP + TN) / (TP + TN + FP + FN)

# Calculate the sensitivity (True Positive Rate)
sensitivity = TP / (TP + FN)

# Calculate the specificity (True Negative Rate)
specificity = TN / (TN + FP)

# Print the results
print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)
print("Accuracy:", accuracy)
print("Sensitivity (True Positive Rate):", sensitivity)
print("Specificity (True Negative Rate):", specificity)
