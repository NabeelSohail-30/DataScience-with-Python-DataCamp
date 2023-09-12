# Generate 1 bootstrap resample
import matplotlib.pyplot as plt
import numpy as np

spotify_1_resample = spotify_sample.sample(frac=1, replace=True)

# Print the resample
print(spotify_1_resample)


# Generate 1 bootstrap resample
spotify_1_resample = spotify_sample.sample(frac=1, replace=True)

# Calculate the mean of the danceability column of spotify_1_resample
mean_danceability_1 = np.mean(spotify_1_resample['danceability'])

# Print the result
print(mean_danceability_1)


# Initialize an empty list to store the means
mean_danceability_1000 = []

# Replicate the process 1000 times
for i in range(1000):
    # Generate a bootstrap resample and calculate its mean danceability
    resample_mean = np.mean(spotify_sample.sample(
        frac=1, replace=True)['danceability'])
    # Append the mean to the list
    mean_danceability_1000.append(resample_mean)

# Print the result (list of means)
print(mean_danceability_1000)


# Initialize an empty list to store the means
mean_danceability_1000 = []

# Replicate the process 1000 times
for i in range(1000):
    # Generate a bootstrap resample and calculate its mean danceability
    resample_mean = np.mean(spotify_sample.sample(
        frac=1, replace=True)['danceability'])
    # Append the mean to the list
    mean_danceability_1000.append(resample_mean)

# Draw a histogram of the resample means
plt.hist(mean_danceability_1000, bins=30, edgecolor='k')
plt.xlabel('Mean Danceability')
plt.ylabel('Frequency')
plt.title('Bootstrap Distribution of Mean Danceability')
plt.show()
