# Import necessary libraries
from dateutil import tz
import pandas as pd

# Load the data into a DataFrame
onebike_datetimes = pd.read_csv('../data/capital-onebike.csv')

# Create a timezone object for Eastern Time (America/New_York)
et = tz.gettz('America/New_York')

# Loop over the first 10 trips and update their datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
    trip['start'] = trip['start'].replace(tzinfo=et)
    trip['end'] = trip['end'].replace(tzinfo=et)

# Print the first trip's start time in Eastern Time
print("Start time in Eastern Time:", onebike_datetimes[0]['start'].isoformat())

# Create the timezone object for UK (Europe/London)
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# Convert the start time to UK time
notlocal = local.astimezone(uk)

# Print the original and converted start times
print("Original:", local.isoformat())
print("UK Time:", notlocal.isoformat())

# Create the timezone object for India (Asia/Kolkata)
ist = tz.gettz('Asia/Kolkata')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# Convert the start time to India time
notlocal = local.astimezone(ist)

# Print the original and converted start times
print("Original:", local.isoformat())
print("India Time:", notlocal.isoformat())

# Create the timezone object for Samoa (Pacific/Apia)
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# Convert the start time to Samoa time
notlocal = local.astimezone(sm)

# Print the original and converted start times
print("Original:", local.isoformat())
print("Samoa Time:", notlocal.isoformat())
