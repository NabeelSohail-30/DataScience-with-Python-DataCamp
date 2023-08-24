import pandas as pd
import numpy as np

# Load the airlines dataset
airlines = pd.read_csv('../datasets/airlines_final.csv')

# Print unique values of both columns
print("Unique values in 'dest_region' column:")
print(airlines['dest_region'].unique())
print("\nUnique values in 'dest_size' column:")
print(airlines['dest_size'].unique())

# Convert 'dest_region' to lowercase and replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur': 'europe'})

# Remove white spaces from 'dest_size'
airlines['dest_size'] = airlines['dest_size'].str.strip()

# Verify changes have been applied
print("\nUpdated 'dest_region' column:")
print(airlines['dest_region'])
print("\nUpdated 'dest_size' column:")
print(airlines['dest_size'])

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create 'wait_type' column using pd.cut()
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins=label_ranges, labels=label_names)

# Create mappings for day of the week
mappings = {
    'Monday': 'weekday', 'Tuesday': 'weekday', 'Wednesday': 'weekday',
    'Thursday': 'weekday', 'Friday': 'weekday',
    'Saturday': 'weekend', 'Sunday': 'weekend'
}

# Replace 'day' values using the mappings
airlines['day_week'] = airlines['day'].replace(mappings)
