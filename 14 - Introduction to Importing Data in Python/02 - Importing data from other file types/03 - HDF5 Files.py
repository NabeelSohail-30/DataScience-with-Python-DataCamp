import numpy as np
import h5py
import matplotlib.pyplot as plt

# Assign the filename
file = 'LIGO_data.hdf5'

# Load the HDF5 file using h5py
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print("Datatype of loaded file:", type(data))

# Print the keys present in the file
print("Keys in the file:")
for key in data.keys():
    print(key)

# Access the 'strain' group within the file
group = data['strain']

# Print the keys present in the 'strain' group
print("Keys in the 'strain' group:")
for key in group.keys():
    print(key)

# Extract the time series data (strain) as a NumPy array
strain = np.array(data['strain']['Strain'])

# Set the number of time points to sample
num_samples = 10000

# Create a time vector
time = np.arange(0, 1, 1/num_samples)

# Plot the strain data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('Strain')
plt.show()