

# Get potential matches using the comparison criteria and print them
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

# Isolate potential matches with a row sum >= 3
matches = potential_matches[potential_matches.sum(axis=1) >= 3]

# Get values of the second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values using the matching_indices
non_dup = restaurants_new[~restaurants_new.index.get_level_values(0).isin(matching_indices)]

# Append non_dup to restaurants to create a complete dataset
full_restaurants = restaurants.append(non_dup)

# Print the resulting complete dataset
print(full_restaurants)