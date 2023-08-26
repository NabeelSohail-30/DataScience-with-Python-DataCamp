# Import the necessary library
import recordlinkage

# Create an indexer object and find possible pairs based on blocking on cuisine_type
indexer = recordlinkage.Index()
indexer.block('cuisine_type')
pairs = indexer.index(restaurants, restaurants_new)

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Define comparison criteria for exact matches on city and cuisine_type
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')

# Define comparison criteria for similar matches of rest_name with a threshold of 0.8
comp_cl.string('rest_name', 'rest_name', label='name', threshold=0.8)

# Get potential matches using the comparison criteria and print them
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)