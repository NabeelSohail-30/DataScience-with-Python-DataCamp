import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

attrition_pop = pd.read_feather('attrition.feather')

# Perform simple random sampling to get 0.25 of the population
attrition_srs = attrition_pop.sample(frac=0.25, random_state=2022)

# Perform stratified sampling to get 0.25 of each RelationshipSatisfaction group
attrition_strat = attrition_pop.groupby(
    'RelationshipSatisfaction').sample(frac=0.25, random_state=2022)

# Create a list of unique RelationshipSatisfaction values
satisfaction_unique = list(attrition_pop['RelationshipSatisfaction'].unique())

# Randomly sample 2 unique satisfaction values
satisfaction_samp = random.sample(satisfaction_unique, k=2)

# Filter for satisfaction_samp and clear unused categories from RelationshipSatisfaction
satis_condition = attrition_pop['RelationshipSatisfaction'].isin(
    satisfaction_samp)
attrition_clust_prep = attrition_pop[satis_condition]
attrition_clust_prep['RelationshipSatisfaction'] = attrition_clust_prep['RelationshipSatisfaction'].cat.remove_unused_categories()

# Perform cluster sampling on the selected group, getting 0.25 of attrition_pop
attrition_clust = attrition_clust_prep.groupby("RelationshipSatisfaction")\
    .sample(n=len(attrition_pop) // 4, random_state=2022)


# Mean Attrition by RelationshipSatisfaction group
mean_attrition_pop = attrition_pop.groupby(
    'RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_pop)

# Calculate the proportion of employee attrition for each RelationshipSatisfaction group in the simple random sample
mean_attrition_srs = attrition_srs.groupby(
    'RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_srs)

# Calculate the proportion of employee attrition for each RelationshipSatisfaction group in the stratified sample
mean_attrition_strat = attrition_strat.groupby(
    'RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_strat)

# Calculate the proportion of employee attrition for each RelationshipSatisfaction group in the cluster sample
mean_attrition_clust = attrition_clust.groupby(
    'RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_clust)
