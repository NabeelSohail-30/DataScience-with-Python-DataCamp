import pandas as pd
import numpy as np

used_cars = pd.read_csv('../datasets/cars.csv')

# Create one-hot encoding for just two columns
used_cars_simple = pd.get_dummies(
  used_cars,
  # Specify the columns from the instructions
  columns=["manufacturer_name", "transmission"],
  # Set the prefix
  prefix="dummy"
)

# Print the shape of the new dataset
print(used_cars_simple.shape)


