import numpy as np
import pandas as pd

# Set the seed for reproducibility
np.random.seed(2022)

# Assuming you have a DataFrame called 'attrition_pop' with the attrition data
# If your data is stored in a different way, you may need to adjust the code accordingly

# Generate a simple random sample of 50 rows
attrition_srs50 = attrition_pop.sample(n=50)

# Calculate the mean employee attrition in the sample
mean_attrition_srs50 = attrition_srs50['Attrition'].mean()

# Calculate the relative error percentage
mean_attrition_pop = attrition_pop['Attrition'].mean()
rel_error_pct50 = (
    abs(mean_attrition_pop - mean_attrition_srs50) / mean_attrition_pop) * 100

# Print rel_error_pct50
print(rel_error_pct50)


# Set the seed for reproducibility
np.random.seed(2022)

# Assuming you have a DataFrame called 'attrition_pop' with the attrition data
# If your data is stored in a different way, you may need to adjust the code accordingly

# Generate a simple random sample of 100 rows
attrition_srs100 = attrition_pop.sample(n=100)

# Calculate the mean employee attrition in the sample
mean_attrition_srs100 = attrition_srs100['Attrition'].mean()

# Calculate the relative error percentage
mean_attrition_pop = attrition_pop['Attrition'].mean()
rel_error_pct100 = (
    abs(mean_attrition_pop - mean_attrition_srs100) / mean_attrition_pop) * 100

# Print rel_error_pct100
print(rel_error_pct100)
