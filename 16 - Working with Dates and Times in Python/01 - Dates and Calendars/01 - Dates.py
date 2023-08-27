# Import date from datetime module
from datetime import date
import pickle

# Create a date object for Hurricane Andrew
hurricane_andrew = date(1992, 8, 24)

# Determine the day of the week for Hurricane Andrew (Monday = 0, Sunday = 6)
print("Day of the week for Hurricane Andrew:", hurricane_andrew.weekday())

# Load the data from the pickle file (provide the correct file path)
with open('../data/florida_hurricane_dates.pkl', 'rb') as file:
    florida_hurricane_dates = pickle.load(file)

# Initialize a counter for hurricanes before June 1
early_hurricanes = 0

# Loop over the hurricane dates
for hurricane in florida_hurricane_dates:
    # Check if the month is before June (month number 6)
    if hurricane.month < 6:
        early_hurricanes = early_hurricanes + 1

# Print the count of hurricanes that occurred before June 1
print("Number of hurricanes before June 1:", early_hurricanes)
