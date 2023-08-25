import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno

# Load the banking dataset
banking = pd.read_csv('../datasets/banking_dirty.csv')

# Print the number of missing values in each column
print("Number of missing values in each column:")
print(banking.isna().sum())

# Visualize the missingness matrix
print("Visualizing missingness matrix:")
msno.matrix(banking)
plt.show()

# Isolate rows with missing and non-missing 'inv_amount'
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# Sort banking by age and visualize the missingness matrix
print("Visualizing sorted banking by age:")
banking_sorted = banking.sort_values(by='age')
msno.matrix(banking_sorted)
plt.show()

# Drop missing values of 'cust_id'
banking_fullid = banking.dropna(subset=['cust_id'])

# Compute estimated 'acct_amount'
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing 'acct_amount' with corresponding 'acct_imp'
banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})

# Print the number of missing values after imputation
print("Number of missing values after imputation:")
print(banking_imputed.isna().sum())
