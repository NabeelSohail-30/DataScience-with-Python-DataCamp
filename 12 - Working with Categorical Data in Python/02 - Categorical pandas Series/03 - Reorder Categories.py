import pandas as pd

dogs = pd.read_csv('../datasets/ShelterDogs.csv')

# Print out the current categories of the size variable
print(dogs["size"].cat.categories)

# Reorder the categories, specifying the Series is ordinal, and overwriting the original series
dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered=True,
  inplace=True
)

# How many Male/Female dogs are available of each size?
print(dogs.groupby('size')['sex'].value_counts())

# Do larger dogs need more room to roam?
print(dogs.groupby('size')['keep_in'].value_counts())