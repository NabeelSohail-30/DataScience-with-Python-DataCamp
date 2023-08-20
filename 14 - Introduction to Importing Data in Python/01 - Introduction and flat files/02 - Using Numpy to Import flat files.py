import numpy as np
import matplotlib.pyplot as plt

# Load and display an image from CSV file
digits_file = 'digits.csv'
digits = np.loadtxt(digits_file, delimiter=',')
print("Datatype of digits:", type(digits))

# Select and reshape a row from digits array
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Display the reshaped image using matplotlib
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

# Load data from a file with a header and specific columns
header_data_file = 'digits_header.txt'
data = np.loadtxt(header_data_file, delimiter='\t', skiprows=1, usecols=(0, 2))
print("Loaded data:", data)

# Load and process string data from a file
seaslug_file = 'seaslug.txt'
data_str = np.loadtxt(seaslug_file, delimiter='\t', dtype=str)
print("First element of data_str:", data_str[0])

# Load and process numeric data from the same file
data_float = np.loadtxt(seaslug_file, delimiter='\t', dtype='float', skiprows=1)
print("10th element of data_float:", data_float[9])

# Create a scatterplot using loaded data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

# Load and display structured data from a CSV file
titanic_file = 'titanic.csv'
d = np.recfromcsv(titanic_file)
print("First three entries of d:", d[:3])