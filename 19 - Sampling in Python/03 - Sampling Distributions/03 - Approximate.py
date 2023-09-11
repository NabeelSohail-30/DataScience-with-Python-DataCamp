import numpy as np
import pandas as pd
import itertools

# Define the number of dice and sides
num_dice = 5
num_sides = 8

# Create a list of all possible values for a single die
possible_values = list(range(1, num_sides + 1))

# Create a list of all possible combinations for throwing five dice
combinations = list(itertools.product(possible_values, repeat=num_dice))

# Create a DataFrame from the combinations
dice = pd.DataFrame(combinations, columns=[
                    'die1', 'die2', 'die3', 'die4', 'die5'])

# Print the result
print(dice)

# Expand a grid representing 5 8-sided dice
dice = expand_grid(
    {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
     'die2': [1, 2, 3, 4, 5, 6, 7, 8],
     'die3': [1, 2, 3, 4, 5, 6, 7, 8],
     'die4': [1, 2, 3, 4, 5, 6, 7, 8],
     'die5': [1, 2, 3, 4, 5, 6, 7, 8]
     })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = (dice['die1'] + dice['die2'] +
                     dice['die3'] + dice['die4'] +
                     dice['die5']) / 5
dice['mean_roll'] = dice['mean_roll'].astype('category')

# Print result
print(dice)

# Expand a grid representing 5 8-sided dice
dice = expand_grid(
    {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
     'die2': [1, 2, 3, 4, 5, 6, 7, 8],
     'die3': [1, 2, 3, 4, 5, 6, 7, 8],
     'die4': [1, 2, 3, 4, 5, 6, 7, 8],
     'die5': [1, 2, 3, 4, 5, 6, 7, 8]
     })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = (dice['die1'] + dice['die2'] +
                     dice['die3'] + dice['die4'] +
                     dice['die5']) / 5
dice['mean_roll'] = dice['mean_roll'].astype('category')

# Draw a bar plot of mean_roll
dice['mean_roll'].value_counts(sort=False).plot(kind="bar")
plt.show()


# Sample one to eight, five times, with replacement
five_rolls = np.random.choice(np.arange(1, 9), size=5, replace=True)

# Calculate the mean of five_rolls
mean_five_rolls = np.mean(five_rolls)

# Print the mean of five_rolls
print(mean_five_rolls)


# Create an empty list to store the sample means
sample_means_1000 = []

# Replicate the sampling code 1000 times
for i in range(1000):
    sample_mean = np.random.choice(
        list(range(1, 9)), size=5, replace=True).mean()
    sample_means_1000.append(sample_mean)

# Print the first 10 entries of the result
print(sample_means_1000[:10])

# Draw a histogram of sample_means_1000 with 20 bins
plt.hist(sample_means_1000, bins=20, edgecolor='k')
plt.xlabel('Sample Means')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Means (1000 Samples)')
plt.show()
