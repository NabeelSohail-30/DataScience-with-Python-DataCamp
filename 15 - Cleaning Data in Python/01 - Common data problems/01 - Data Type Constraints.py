import pandas as pd

ride_sharing = pd.read_csv('../datasets/ride_sharing_new.csv')

# Print the information about the DataFrame
print("DataFrame information:")
print(ride_sharing.info())

# Print summary statistics of the 'user_type' column
print("\nSummary statistics of 'user_type' column:")
print(ride_sharing['user_type'].describe())

# Convert 'user_type' from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Assert statement to confirm the dtype change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics of the categorical column
print("\nSummary statistics of 'user_type_cat' column:")
print(ride_sharing['user_type_cat'].describe())

# Strip 'minutes' from 'duration' column
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert 'duration_trim' to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Assert statement to confirm the conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print the new columns and calculate average ride duration
print("\nColumns with duration details:")
print(ride_sharing[['duration', 'duration_trim', 'duration_time']])
print("Average ride duration:", ride_sharing['duration_time'].mean())
