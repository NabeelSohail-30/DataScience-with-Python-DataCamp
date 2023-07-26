import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv('../datasets/climate_change.csv', parse_dates=["date"], index_col="date")

print(climate_change.head())

fig, ax = plt.subplots()

# # Plot the CO2 variable in blue
# ax.plot(climate_change.index, climate_change['co2'], color='blue')
#
# # Create a twin Axes that shares the x-axis
# ax2 = ax.twinx()
#
# # Plot the relative temperature in red
# ax2.plot(climate_change.index, climate_change['relative_temp'], color='red')
#
# plt.show()

# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)



# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change['co2'], "blue", 'Time (years)', "CO2 levels")

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], "red", 'Time (years)',
              "Relative temperature (Celsius)")

plt.show()