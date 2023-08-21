import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load MATLAB file using scipy.io
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype of mat
print("Datatype of mat:", type(mat))

# Print the keys present in the MATLAB dictionary
print("Keys in the dictionary:", mat.keys())

# Print the datatype of the value corresponding to the key 'CYratioCyt'
print("Datatype of 'CYratioCyt' value:", type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print("Shape of 'CYratioCyt' value:", np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (expression)')
plt.show()
