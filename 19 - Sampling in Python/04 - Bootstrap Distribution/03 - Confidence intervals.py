from scipy.stats import norm
import numpy as np

# Calculate the lower quantile (2.5th percentile)
lower_quant = np.quantile(bootstrap_distribution, 0.025)

# Calculate the upper quantile (97.5th percentile)
upper_quant = np.quantile(bootstrap_distribution, 0.975)

# Print quantile method confidence interval
print((lower_quant, upper_quant))


# Calculate the point estimate as the mean of the bootstrap distribution
point_estimate = np.mean(bootstrap_distribution)

# Calculate the standard error with ddof=1 as the standard deviation of the bootstrap distribution
standard_error = np.std(bootstrap_distribution, ddof=1)

# Calculate the upper limit of the confidence interval using norm.ppf()
upper_se = norm.ppf(0.975, loc=point_estimate, scale=standard_error)

# Calculate the lower limit of the confidence interval
lower_se = 2 * point_estimate - upper_se

# Print standard error method confidence interval
print((lower_se, upper_se))
