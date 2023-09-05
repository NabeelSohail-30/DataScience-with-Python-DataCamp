# Import the ols function
from statsmodels.formula.api import ols

# Create the model object
mdl_price_vs_conv = ols('price_twd_msq ~ n_convenience', data=taiwan_real_estate)

# Fit the model
mdl_price_vs_conv = mdl_price_vs_conv.fit()

# Print the parameters of the fitted model
print(mdl_price_vs_conv.params)

# Histograms of price_twd_msq with 10 bins, split by the age of each house
sns.histplot(data=taiwan_real_estate,
             x='price_twd_msq',
             bins=10,
             hue='house_age_years',
             multiple='dodge')  # Use 'dodge' to split by house_age_years into panels

# Show the plot
plt.show()


# Histograms of price_twd_msq with 10 bins, split by the age of each house
sns.displot(data=taiwan_real_estate,
            x="price_twd_msq",
            col="house_age_years",
            bins=10)

# Show the plot
plt.show()

