import pandas as pd

# Load the airlines dataset
airlines = pd.read_csv('../datasets/airlines_final.csv')

# Create a dictionary to define categorical values
data = {
    'cleanliness': ['Clean', 'Average', 'Somewhat clean', 'Somewhat dirty', 'Dirty'],
    'safety': ['Neutral', 'Very safe', 'Somewhat safe', 'Very unsafe', 'Somewhat unsafe'],
    'satisfaction': ['Very satisfied', 'Neutral', 'Somewhat satisfied', 'Somewhat unsatisfied', 'Very unsatisfied']
}

# Create a DataFrame to define categorical categories
categories = pd.DataFrame(data)

# Print the categories DataFrame
print("Categories DataFrame:")
print(categories)

# Print unique values of survey columns in the airlines DataFrame
print("\nUnique values in survey columns:")
print('Cleanliness:', airlines['cleanliness'].unique())
print('Safety:', airlines['safety'].unique())
print('Satisfaction:', airlines['satisfaction'].unique())

# Find the cleanliness categories in airlines that are not in the categories DataFrame
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with cleanliness categories that are inconsistent
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent cleanliness categories
print("\nRows with inconsistent cleanliness categories:")
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print("\nRows with consistent categories:")
print(airlines[~cat_clean_rows])
