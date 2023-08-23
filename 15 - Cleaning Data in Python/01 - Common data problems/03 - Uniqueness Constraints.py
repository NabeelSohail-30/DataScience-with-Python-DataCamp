import pandas as pd

# Load the dataset
ride_sharing = pd.read_csv('../datasets/ride_sharing_new.csv')

# Find duplicates based on 'ride_id'
duplicates = ride_sharing.duplicated(subset='ride_id', keep=False)

# Sort the duplicated rides based on 'ride_id'
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated rides
print("Relevant columns of duplicated rides:")
print(duplicated_rides[['ride_id', 'duration', 'user_birth_year']])

# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create a dictionary for aggregation functions
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by 'ride_id' and compute new statistics using aggregation
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset='ride_id', keep=False)
duplicated_rides = ride_unique[duplicates]

# Assert that duplicated rides are processed
assert duplicated_rides.shape[0] == 0
