import pandas as pd

# Load the banking dataset
banking = pd.read_csv('../datasets/banking_dirty.csv')

# Find rows where 'acct_cur' is equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert 'acct_amount' from euro to dollars for the selected rows
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify 'acct_cur' column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only 'dollar' currency remains in 'acct_cur'
assert banking['acct_cur'].unique() == 'dollar'

# Print the header of the 'account_opened' column
print("Header of 'account_opened' column:")
print(banking['account_opened'].head())

# Convert 'account_opened' to datetime format
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           infer_datetime_format=True,
                                           errors='coerce')

# Extract the year from 'account_opened' and create 'acct_year' column
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print the 'acct_year' column
print("Acct_year column:")
print(banking['acct_year'])
