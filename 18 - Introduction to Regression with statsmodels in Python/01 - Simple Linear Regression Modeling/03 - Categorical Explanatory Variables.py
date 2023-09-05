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

# Calculate the mean of price_twd_msq, grouped by house age
mean_price_by_age = taiwan_real_estate.groupby('house_age_years')['price_twd_msq'].mean()

# Print the result
print(mean_price_by_age)
