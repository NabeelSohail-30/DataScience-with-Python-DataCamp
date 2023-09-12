import numpy as np
import pandas as pd

spotify_sample = pd.read_feather('./datasets/spotify_2000_2020.feather')

# Initialize an empty list to store the means
mean_popularity_2000_samp = []

# Generate a sampling distribution of 2000 replicates
for _ in range(2000):
    # Sample 500 rows without replacement
    sample = spotify_population.sample(n=500, replace=False)

    # Calculate the mean popularity for the sampled rows
    mean_popularity = np.mean(sample['popularity'])

    # Append the mean to the list
    mean_popularity_2000_samp.append(mean_popularity)

# Print the sampling distribution results
print(mean_popularity_2000_samp)


# Initialize an empty list to store the means
mean_popularity_2000_boot = []

# Generate a bootstrap distribution of 2000 replicates
for _ in range(2000):
    # Resample 500 rows with replacement from the sample
    resample = spotify_sample.sample(n=500, replace=True)

    # Calculate the mean popularity for the resample
    mean_popularity = np.mean(resample['popularity'])

    # Append the mean to the list
    mean_popularity_2000_boot.append(mean_popularity)

# Print the bootstrap distribution results
print(mean_popularity_2000_boot)

# Calculate the population mean popularity
pop_mean = spotify_population['popularity'].mean()

# Calculate the original sample mean popularity
samp_mean = spotify_sample['popularity'].mean()

# Calculate the sampling dist'n estimate of mean popularity
samp_distn_mean = np.mean(sampling_distribution)

# Calculate the bootstrap dist'n estimate of mean popularity
boot_distn_mean = np.mean(bootstrap_distribution)

# Print the means
print([pop_mean, samp_mean, samp_distn_mean, boot_distn_mean])


# Calculate the population std dev popularity
pop_sd = spotify_population['popularity'].std(ddof=0)

# Calculate the original sample std dev popularity
samp_sd = spotify_sample['popularity'].std()

# Calculate the sampling dist'n estimate of std dev popularity
samp_distn_sd = np.std(sampling_distribution, ddof=1) * np.sqrt(5000)

# Calculate the bootstrap dist'n estimate of std dev popularity
boot_distn_sd = np.std(bootstrap_distribution, ddof=1) * np.sqrt(5000)

# Print the standard deviations
print([pop_sd, samp_sd, samp_distn_sd, boot_distn_sd])
