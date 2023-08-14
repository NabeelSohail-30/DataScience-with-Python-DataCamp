import pandas as pd

dogs = pd.read_csv('../datasets/ShelterDogs.csv')

# Check frequency counts while also printing the NaN count
print(dogs["keep_in"].value_counts(dropna=False))

# Switch to a categorical variable
dogs["keep_in"] = dogs["keep_in"].astype("category")

# Add new categories
new_categories = ["Unknown History", "Open Yard (Countryside)"]
dogs["keep_in"] = dogs["keep_in"].cat.add_categories(new_categories)

# Check frequency counts one more time
print(dogs["keep_in"].value_counts(dropna=False))

# Set "maybe" to be "no"
dogs.loc[dogs["likes_children"] == "maybe", "likes_children"] = "no"

# Print out categories
print(dogs["likes_children"].cat.categories)

# Print the frequency table
print(dogs["likes_children"].value_counts())

# Remove the "maybe" category
dogs["likes_children"] = dogs["likes_children"].cat.remove_categories(removals=['maybe'])
print(dogs["likes_children"].value_counts())

# Print the categories one more time
print(dogs["likes_children"].cat.categories)