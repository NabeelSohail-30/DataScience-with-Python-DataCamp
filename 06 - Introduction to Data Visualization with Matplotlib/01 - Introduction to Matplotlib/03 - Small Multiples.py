# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('../datasets/seattle_weather.csv')
austin_weather = pd.read_csv('../datasets/austin_weather.csv')

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot DATE and Seattle precipitation
ax[0, 0].plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot DATE and Seattle temperatures
ax[0, 1].plot(seattle_weather["DATE"], seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot DATE and Austin precipitations
ax[1, 0].plot(austin_weather["DATE"], austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot DATE and Austin temperatures
ax[1, 1].plot(austin_weather["DATE"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig1, ax1 = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation in the top axes
ax1[0].plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-NORMAL"], color='b')
ax1[0].plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-25PCTL"], color='b', linestyle='--')
ax1[0].plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-75PCTL"], color='b', linestyle='--')

# Plot Austin precipitation in the bottom axes
ax1[1].plot(austin_weather["DATE"], austin_weather["MLY-PRCP-NORMAL"], color='r')
ax1[1].plot(austin_weather["DATE"], austin_weather["MLY-PRCP-25PCTL"], color='r', linestyle='--')
ax1[1].plot(austin_weather["DATE"], austin_weather["MLY-PRCP-75PCTL"], color='r', linestyle='--')

plt.show()