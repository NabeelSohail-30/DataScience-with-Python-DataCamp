import pandas as pd
import numpy as np

used_cars = pd.read_csv('../datasets/cars.csv')

# Print the frequency table of body_type and include NaN values
print(used_cars["body_type"].value_counts(dropna=False))

# Update NaN values
used_cars.loc[used_cars["body_type"].isna(), "body_type"] = "other"

# Convert body_type to title case
used_cars["body_type"] = used_cars["body_type"].str.title()

# Check the dtype
print(used_cars['body_type'].dtype)

# Print the frequency table of Sale Rating
print(used_cars['Sale Rating'].value_counts())

# Find the average score
average_score = used_cars["Sale Rating"].astype('int').mean()

# Print the average
print(average_score)