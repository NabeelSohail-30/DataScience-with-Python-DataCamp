import pandas as pd

dogs = pd.read_csv('../datasets/ShelterDogs.csv')

# Fix the misspelled word
replace_map = {"Malez": "male"}

# Update the sex column using the created map
dogs["sex"] = dogs["sex"].replace(replace_map)

# Strip away leading whitespace
dogs["sex"] = dogs["sex"].str.strip()

# Make all responses lowercase
dogs["sex"] = dogs["sex"].str.lower()

# Convert to a categorical Series
dogs["sex"] = dogs["sex"].astype('category')

print(dogs["sex"].value_counts())

# Print the category of the coat for ID 23807
print(dogs.loc[23807, "coat"])

# Find the count of male and female dogs who have a "long" coat
print(dogs.loc[dogs["coat"] == "long", "sex"].value_counts())

# Print the mean age of dogs with a breed of "English Cocker Spaniel"
print(dogs.loc[dogs["breed"] == "English Cocker Spaniel", "age"].mean())

# Count the number of dogs that have "English" in their breed name
print(dogs[dogs["breed"].str.contains("English", regex=False)].shape[0])