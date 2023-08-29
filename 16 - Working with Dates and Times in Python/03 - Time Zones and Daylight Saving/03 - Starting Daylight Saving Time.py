from datetime import datetime, timedelta
from dateutil import tz

# Define time zones
ny_tz = tz.gettz('America/New_York')
utc_tz = tz.gettz('UTC')

# Define starting date in New York timezone
start = datetime(2017, 3, 12, tzinfo=ny_tz)

# Calculate end time by adding 6 hours
end = start + timedelta(hours=6)

# Print time range and elapsed hours
print(f"Time range: {start.isoformat()} to {end.isoformat()}")
print(f"Elapsed hours: {(end - start).total_seconds() / (60 * 60)}")

# Calculate elapsed hours in UTC
elapsed_hours_utc = (end.astimezone(utc_tz) - start.astimezone(utc_tz)).total_seconds() / (60 * 60)
print(f"Elapsed hours in UTC: {elapsed_hours_utc:.2f}")

# Create starting date
start_date = datetime(2000, 3, 29, tzinfo=tz.gettz('Europe/London'))

# Generate ISO timestamps for multiple years
for year in range(2000, 2011):
    new_date = start_date.replace(year=year)
    print(new_date.isoformat())
