import numpy as np

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# simulate a single deal, wins 30%
print("single deal: ", binom.rvs(1, 0.3, size=1))

# Simulate 1 week of 3 deals
print("1 week of 3 deals: ", binom.rvs(3, 0.3, size=1))

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size=52)

print("52 weeks 3 deals: ", deals)

print("mean of 52 weeks 3 deals: ", np.mean(deals))

# probality of closing 3 deals out of 3
prob_3 = binom.pmf(3, 3, 0.3)
print("prob 3 out 0f 3: ", prob_3)

# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)
print("prob <=1 out of 3: ", prob_less_than_or_equal_1)

# Probability of closing > 1 deal out of 3 deals
prob_greater_than_or_equal_to_1 = 1 - binom.cdf(1, 3, 0.3)
print("prob >=1 out of 3: ", prob_greater_than_or_equal_to_1)

# Expected number won with 30% win rate
won_30pct = 3 * 0.3
print("expected won with 30%: ", won_30pct)

# Expected number won with 25% win rate
won_25pct = 3 * 0.25
print("expected won with 25%: ", won_25pct)

# Expected number won with 35% win rate
won_35pct = 3 * 0.35
print("expected won with 35%: ", won_35pct)
