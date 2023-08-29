from dateutil import tz
import pandas as pd

# Load the data into a DataFrame
onebike_datetimes = pd.read_csv('../data/capital-onebike.csv')

# Check for ambiguous start or end times
for trip in onebike_datetimes:
    if tz.datetime_ambiguous(trip['start']):
        print("Ambiguous start at", trip['start'])
    if tz.datetime_ambiguous(trip['end']):
        print("Ambiguous end at", trip['end'])

trip_durations = []
for trip in onebike_datetimes:
    start, end = trip['start'], trip['end']
    if start > end:
        end = tz.enfold(end)
    start_utc, end_utc = start.astimezone(tz.UTC), end.astimezone(tz.UTC)
    trip_durations.append((end_utc - start_utc).total_seconds())

# Find the shortest trip duration
shortest_duration = min(trip_durations)
print("Shortest trip:", shortest_duration)
