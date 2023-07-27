import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('../datasets/seattle_weather.csv')
austin_weather = pd.read_csv('../datasets/austin_weather.csv')

# Use the "ggplot" style and create new Figure/Axes
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(seattle_weather["DATE"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

# Use the "bmh" style and create new Figure/Axes
plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(seattle_weather["DATE"], seattle_weather["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["DATE"], austin_weather["MLY-TAVG-NORMAL"])
ax.set_xlabel("Time (DATEs)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()

# Use the "seaborn-colorblind" style and create new Figure/Axes
plt.style.use("seaborn-colorblind")
fig, ax = plt.subplots()
ax.plot(seattle_weather["DATE"], seattle_weather["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["DATE"], austin_weather["MLY-TAVG-NORMAL"])
ax.set_xlabel("Time (DATEs)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()

# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(austin_weather["DATE"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()