import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

spotify_population = pd.read_feather('./dataset/spotify_2000_2020.feather')

# Create a histogram of the 'acousticness' column with specified bins
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
bin_edges = np.arange(0, 1.01, 0.01)  # Specify bin edges with a step of 0.01
spotify_population['acousticness'].hist(bins=bin_edges, edgecolor='k')
plt.xlabel('Acousticness')
plt.ylabel('Frequency')
plt.title('Acousticness Distribution in Spotify Population')
plt.grid(True)

# Show the histogram
plt.show()

# Create a histogram of the 'acousticness' column with specified bins
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
bin_edges = np.arange(0, 1.01, 0.01)  # Specify bin edges with a step of 0.01
spotify_mysterious_sample['acousticness'].hist(bins=bin_edges, edgecolor='k')
plt.xlabel('Acousticness')
plt.ylabel('Frequency')
plt.title('Acousticness Distribution in Spotify Mysterious Sample')
plt.grid(True)

# Show the histogram
plt.show()

# Create a histogram of the 'duration_minutes' column with specified bins
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
spotify_population['duration_minutes'].hist(
    bins=np.arange(0, 15.5, 0.5), edgecolor='k')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.title('Duration Distribution in Spotify Population')
plt.grid(True)

# Show the histogram
plt.show()

# Create a histogram of the 'duration_minutes' column with specified bins
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
spotify_mysterious_sample2['duration_minutes'].hist(
    bins=np.arange(0, 15.5, 0.5), edgecolor='k')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.title('Duration Distribution in Spotify Population')
plt.grid(True)

# Show the histogram
plt.show()
