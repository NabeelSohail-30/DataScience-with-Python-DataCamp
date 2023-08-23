import pandas as pd
import datetime as dt

# Load the dataset
ride_sharing = pd.read_csv('../datasets/ride_sharing_new.csv')

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print description of tire_sizes column
print("Description of 'tire_sizes' column:")
print(ride_sharing['tire_sizes'].describe())

# Convert ride_date to date using pandas datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all dates in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print the maximum date in the ride_dt column
print("Maximum date in 'ride_dt' column:", ride_sharing['ride_dt'].max())
