# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('../datasets/seattle_weather.csv')
austin_weather = pd.read_csv('../datasets/austin_weather.csv')

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against the DATE
ax.plot(seattle_weather["DATE"], seattle_weather['MLY-PRCP-NORMAL'])

# Plot MLY-PRCP-NORMAL from austin_weather against DATE
ax.plot(austin_weather["DATE"], austin_weather['MLY-PRCP-NORMAL'])

# Call the show function
plt.show()