# Import necessary libraries
from thefuzz import process
import pandas as pd

# Load the restaurants dataset
restaurants = pd.read_csv('../datasets/restaurants_L2.csv')

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()

# Calculate similarity of 'asian' to all values of unique_types
print("Similarity to 'asian':")
print(process.extract('asian', unique_types, limit=len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
print("\nSimilarity to 'american':")
print(process.extract('american', unique_types, limit=len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
print("\nSimilarity to 'italian':")
print(process.extract('italian', unique_types, limit=len(unique_types)))

# Inspect the unique values of the cuisine_type column
print("\nUnique values of cuisine_type column:")
print(restaurants['cuisine_type'].unique())

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

# Inspect the first 5 matches
print("\nFirst 5 matches for 'italian':")
print(matches[0:5])

# Iterate through the list of matches for 'italian'
for match in matches:
    # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
        # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
        restaurants.loc[restaurants['cuisine_type'] == match[0]] = 'italian'

# List of standardized categories
categories = ['asian', 'american', 'italian']

# Iterate through categories
for cuisine in categories:
    # Create a list of matches, comparing cuisine with the cuisine_type column
    matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

    # Iterate through the list of matches
    for match in matches:
        # Check whether the similarity score is greater than or equal to 80
        if match[1] >= 80:
            # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
            restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine

# Inspect the final result of standardized cuisine types
print("\nFinal standardized cuisine types:")
print(restaurants['cuisine_type'].unique())
