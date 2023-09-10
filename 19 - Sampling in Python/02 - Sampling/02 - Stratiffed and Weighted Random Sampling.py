# Calculate the proportion of employees by Education level
import matplotlib.pyplot as plt
education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Proportional stratified sampling for 40% of each Education group
attrition_strat = attrition_pop.groupby('Education')\
    .sample(frac=0.4, random_state=2022)

# Print the sample
print(attrition_strat)

# Proportion of employees by Education level in the original population (attrition_pop)
education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Proportional stratified sampling for 40% of each Education group
attrition_strat = attrition_pop.groupby('Education')\
    .sample(frac=0.4, random_state=2022)

# Calculate the Education level proportions from attrition_strat
education_counts_strat = attrition_strat['Education'].value_counts(
    normalize=True)

# Print education_counts_strat
print(education_counts_strat)

# Get 30 employees from each Education group
attrition_eq = attrition_pop.groupby('Education')\
    .sample(n=30, random_state=2022)

# Print the sample
print(attrition_eq)

# Get 30 employees from each Education group
attrition_eq = attrition_pop.groupby('Education')\
    .sample(n=30, random_state=2022)

# Calculate the Education level proportions from attrition_eq
education_counts_eq = attrition_eq['Education'].value_counts(normalize=True)

# Print the proportions
print(education_counts_eq)


# Plot YearsAtCompany from attrition_pop as a histogram
plt.hist(attrition_pop['YearsAtCompany'],
         bins=range(0, 41, 1), edgecolor='black')
plt.xlabel('Years at Company')
plt.ylabel('Frequency')
plt.title('Histogram of YearsAtCompany')
plt.grid(axis='y', alpha=0.75)

plt.show()


# Sample 400 employees weighted by YearsAtCompany
attrition_weight = attrition_pop.sample(n=400, weights="YearsAtCompany")

# Print the sample
print(attrition_weight)

# Plot YearsAtCompany from attrition_weight as a histogram
attrition_weight['YearsAtCompany'].hist(
    bins=np.arange(0, 41, 1), edgecolor='black')
plt.xlabel('Years at Company')
plt.ylabel('Frequency')
plt.title('Histogram of YearsAtCompany (Weighted Sample)')
plt.grid(axis='y', alpha=0.75)
plt.show()
