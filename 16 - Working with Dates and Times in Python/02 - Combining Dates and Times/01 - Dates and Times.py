from datetime import datetime
import pandas as pd

# Read the data into a DataFrame
onebike_datetimes = pd.read_csv('../data/capital-onebike.csv')

# Create a datetime object
dt = datetime(2017, 10, 1, 15, 26, 26)

# Print the results in ISO 8601 format
print("Formatted datetime:", dt.isoformat())

# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)

# Print the results in ISO 8601 format
print("Formatted datetime:", dt.isoformat())

# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)

# Replace the year with 1917
dt_old = dt.replace(year=1917)

# Print the results in ISO 8601 format
print("Updated year:", dt_old)

# Initialize a dictionary to hold trip counts
trip_counts = {'AM': 0, 'PM': 0}

# Loop over all trips
for index, trip in onebike_datetimes.iterrows():
    # Check if the trip starts before noon
    if trip['start'].hour < 12:
        # Increment the counter for before noon trips
        trip_counts['AM'] += 1
    else:
        # Increment the counter for after noon trips
        trip_counts['PM'] += 1

print("Trip counts:", trip_counts)
