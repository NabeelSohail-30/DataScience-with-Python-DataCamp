import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv('../datasets/climate_change.csv', parse_dates=["date"], index_col="date")

print(climate_change.head())

fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()

fig1, ax1 = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01" : "1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax1.plot(seventies.index, seventies["co2"])
ax1.set_xlabel('Time')
ax1.set_ylabel('co2')

# Show the figure
plt.show()