import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5, min_time, max_time)
print("prob less than 5: ", prob_less_than_5)

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1 - uniform.cdf(5, min_time, max_time)
print("prob greater than 5: ", prob_greater_than_5)

prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time)
print("prob between 10 and 20: ", prob_between_10_and_20)

np.random.seed(334)

# Generate 1000 wait times between 0 and 30 min
wait_time = uniform.rvs(0, 30, size=1000)
print("1000 wait time between 0 and 30 mins: ", wait_time)

# Create a histogram of simulated times and show plot
plt.hist(wait_time)
plt.show()