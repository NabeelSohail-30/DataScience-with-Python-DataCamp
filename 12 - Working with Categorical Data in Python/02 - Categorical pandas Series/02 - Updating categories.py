import pandas as pd

dogs = pd.read_csv('../datasets/ShelterDogs.csv')

# Create the my_changes dictionary
my_changes = {"Maybe?": "Maybe"}

# Rename the categories listed in the my_changes dictionary
dogs["likes_children"] = dogs["likes_children"].cat.rename_categories(my_changes)

# Use a lambda function to convert all categories to uppercase using upper()
dogs["likes_children"] =  dogs["likes_children"].cat.rename_categories(lambda c: c.upper())

# Print the list of categories
print(dogs["likes_children"].cat.categories)

# Create the update_coats dictionary
update_coats = {'wirehaired' : 'medium', 'medium-long' : 'medium'}

# Create a new column, coat_collapsed
dogs["coat_collapsed"] = dogs["coat"].replace(update_coats)

# Convert the column to categorical
dogs["coat_collapsed"] = dogs["coat_collapsed"].astype('category')

# Print the frequency table
print(dogs["coat_collapsed"].value_counts())