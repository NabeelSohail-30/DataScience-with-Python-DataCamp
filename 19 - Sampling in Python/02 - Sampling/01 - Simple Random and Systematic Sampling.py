import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

attrition_pop = pd.read_feather('attrition.feather')

# Set the random seed and sample 70 rows using simple random sampling
attrition_samp = attrition_pop.sample(n=70, random_state=18900217)

# Print the sample dataset
print(attrition_samp)

# Set the sample size to 70
sample_size = 70

# Calculate the population size from attrition_pop (assuming it's the number of rows)
pop_size = len(attrition_pop)

# Calculate the interval
interval = pop_size / sample_size

# Set the sample size to 70
sample_size = 70

# Calculate the population size from attrition_pop
pop_size = len(attrition_pop)

# Calculate the interval
interval = pop_size // sample_size

# Systematically sample 70 rows
attrition_sys_samp = attrition_pop.iloc[::interval]

# Print the sample
print(attrition_sys_samp)


# Add an index column to attrition_pop
attrition_pop_id = attrition_pop.reset_index()

# Plot YearsAtCompany vs. index for attrition_pop_id
attrition_pop_id.plot(x='index', y='YearsAtCompany', kind='scatter',
                      title='Scatter Plot: YearsAtCompany vs. Index')

plt.show()

# Shuffle the rows of attrition_pop
attrition_shuffled = attrition_pop.sample(frac=1)

# Reset the row indexes and create an index column
attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()

# Plot YearsAtCompany vs. index for attrition_shuffled
attrition_shuffled.plot(x="index", y="YearsAtCompany", kind="scatter")
plt.show()
