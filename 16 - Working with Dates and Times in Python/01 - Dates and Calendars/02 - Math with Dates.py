from datetime import date, timedelta
import pickle

from numpy.random.mtrand import random

# Create date objects for May 9th, 2007 and December 13th, 2007
start = date(2007, 5, 9)
end = date(2007, 12, 13)

# Calculate the difference between the two dates and print the number of days
days_difference = (end - start).days
print("Number of days between start and end:", days_difference)

# Initialize a dictionary to count hurricanes per calendar month
hurricanes_each_month = {month: 0 for month in range(1, 13)}

# Load the data from the pickle file (provide the correct file path)
with open('../data/florida_hurricane_dates.pkl', 'rb') as file:
    florida_hurricane_dates = pickle.load(file)

# Loop over hurricane dates and count hurricanes for each month
for hurricane in florida_hurricane_dates:
    month = hurricane.month
    hurricanes_each_month[month] += 1

print("Number of hurricanes each month:", hurricanes_each_month)

# Generate a list of dates within the specified range
dates_scrambled = [start + timedelta(days=i) for i in range((end - start).days + 1)]

# Shuffle the list of dates to create a scrambled order
random.shuffle(dates_scrambled)

# Print the first and last dates from the scrambled list
print("First scrambled date:", dates_scrambled[0])
print("Last scrambled date:", dates_scrambled[-1])

# Sort the scrambled dates list and print the first and last dates
dates_ordered = sorted(dates_scrambled)
print("First ordered date:", dates_ordered[0])
print("Last ordered date:", dates_ordered[-1])