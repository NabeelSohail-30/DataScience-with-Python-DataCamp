# Generate random numbers from a Uniform(-3, 3)
import numpy as np
import matplotlib.pyplot as plt
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# Print uniforms
print(uniforms)

# Generate random numbers from a Normal(5, 2)
normals = np.random.normal(loc=5, scale=2, size=5000)

# Print normals
print(normals)


# Assuming you have already generated the 'uniforms' data

# Create a histogram of the 'uniforms' data with specified bins
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
bin_edges = np.arange(-3, 3.25, 0.25)  # Specify bin edges with a step of 0.25
plt.hist(uniforms, bins=bin_edges, edgecolor='k')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Uniform(-3, 3)')
plt.grid(True)

# Show the histogram
plt.show()


# Assuming you have already generated the 'random_numbers' data

# Create a histogram of the 'random_numbers' data with specified bins
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
bin_edges = np.arange(-2, 13.5, 0.5)  # Specify bin edges with a step of 0.5
plt.hist(random_numbers, bins=bin_edges, edgecolor='k')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal(5, 2)')
plt.grid(True)

# Show the histogram
plt.show()
