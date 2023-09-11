import matplotlib.pyplot as plt
import pandas as pd

attrition_pop = pd.read_feather('dataset/attrition.feather')

# Create an empty list
mean_attritions = []
# Loop 500 times to create 500 sample means
for i in range(500):
    mean_attritions.append(
        attrition_pop.sample(n=60)['Attrition'].mean()
    )

# Print out the first few entries of the list
print(mean_attritions[0:5])


# Create an empty list
mean_attritions = []

# Loop 500 times to create 500 sample means
for i in range(500):
    mean_attritions.append(
        attrition_pop.sample(n=60)['Attrition'].mean()
    )

# Create a histogram of the 500 sample means with 16 bins
plt.hist(mean_attritions, bins=16, edgecolor='k')
plt.xlabel('Mean Attrition')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Means (500 Samples)')
plt.show()
