import matplotlib.pyplot as plt
import numpy as np

# Assuming the 'group_size' column exists in the DataFrame 'restaurant_groups'
group_size_data = restaurant_groups['group_size']

# Define the bins
bins = [2, 3, 4, 5, 6]

# Create the histogram
plt.hist(group_size_data, bins=bins, edgecolor='black')

# Add labels and title
plt.xlabel('Group Size')
plt.ylabel('Frequency')
plt.title('Histogram of Group Size')

# Show the plot
plt.show()

# Create a histogram of restaurant_groups and show plot
restaurant_groups['group_size'].hist(bins=[2, 3, 4, 5, 6])
plt.show()

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / 10

# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

print(size_dist)

# Calculate expected value
expected_value = (size_dist['group_size'] * size_dist['prob']).sum()
print(expected_value)

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

# Expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size']>=4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more = groups_4_or_more['prob'].sum()
print(prob_4_or_more)