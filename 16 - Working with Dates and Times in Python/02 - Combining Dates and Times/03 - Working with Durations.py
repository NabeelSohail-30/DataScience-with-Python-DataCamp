# Import necessary libraries
from datetime import datetime
import pandas as pd

# Load the data into a DataFrame
onebike_datetimes = pd.read_csv('../data/capital-onebike.csv')

# Initialize a list for all the trip durations
onebike_durations = []

# Loop over each trip in the DataFrame
for trip in onebike_datetimes.iterrows():
    # Extract start and end times from the trip
    start_time = trip[1]['start']
    end_time = trip[1]['end']

    # Convert start and end times to datetime objects
    start_datetime = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_datetime = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    # Calculate the duration of the trip as a timedelta object
    trip_duration = end_datetime - start_datetime

    # Get the total elapsed seconds in trip_duration
    trip_length_seconds = trip_duration.total_seconds()

    # Append the trip length in seconds to the list
    onebike_durations.append(trip_length_seconds)

# Calculate the total elapsed time and number of trips
total_elapsed_time = sum(onebike_durations)
number_of_trips = len(onebike_durations)

# Calculate the average trip duration
average_trip_duration = total_elapsed_time / number_of_trips

# Print the average trip duration
print("Average trip duration:", average_trip_duration, "seconds")

# Calculate the shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)

# Print out the results
print("The shortest trip was", shortest_trip, "seconds")
print("The longest trip was", longest_trip, "seconds")
