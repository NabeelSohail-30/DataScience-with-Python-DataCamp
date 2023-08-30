# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York')

# Print first value
print(rides['Start date'].iloc[0])

