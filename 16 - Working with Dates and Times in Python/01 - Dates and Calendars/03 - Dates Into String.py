from datetime import date

# Get the earliest hurricane date from the list
first_date = min(florida_hurricane_dates)

# Convert the earliest date to ISO and US formats
iso_format = first_date.isoformat()
us_format = first_date.strftime("%m/%d/%Y")

print("ISO format:", iso_format)
print("US format:", us_format)

# Define a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print("Formatted as 'YYYY-MM':", andrew.strftime('%Y-%m'))

# Print the date in the format 'MONTH (YYYY)'
print("Formatted as 'MONTH (YYYY)':", andrew.strftime('%B (%Y)'))

# Print the date in the format 'YYYY-DDD'
print("Formatted as 'YYYY-DDD':", andrew.strftime('%Y-%j'))
