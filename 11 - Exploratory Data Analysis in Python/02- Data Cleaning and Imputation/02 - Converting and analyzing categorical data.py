import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

planes = pd.read_csv('../datasets/planes.csv')

# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes("object")

# Loop through columns
for col in non_numeric.columns:
    # Print the number of unique values
    print(f"Number of unique values in {col} column: ", non_numeric[col].nunique())


# Create a list of categories
flight_categories = [
    "Short-haul",
    "Medium",
    "Long-haul"
]


# Create short_flights
short_flights = "^0h|^1h|^2h|^3h|^4h"

# Create medium_flights
medium_flights = "^5h|^6h|^7h|^8h|^9h"

# Create long_flights
long_flights = "10h|11h|12h|13h|14h|15h|16h"


# Create conditions for values in flight_categories to be created
conditions = [
    (planes["Duration"].str.contains(short_flights)),
    (planes["Duration"].str.contains(medium_flights)),
    (planes["Duration"].str.contains(long_flights))
]

# Apply the conditions list to the flight_categories
planes["Duration_Category"] = np.select(conditions,
                                        flight_categories,
                                        default="Extreme duration")

# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")
plt.show()


