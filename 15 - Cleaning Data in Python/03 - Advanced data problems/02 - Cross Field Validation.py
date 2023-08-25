import datetime
import pandas as pd

# Load the banking dataset
banking = pd.read_csv('../datasets/banking_dirty.csv')

# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where the sum of fund_columns matches 'inv_amount'
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Print the number of inconsistent investments
print("Number of inconsistent investments:", inconsistent_inv.shape[0])

# Store today's date and calculate ages manually
today = datetime.date.today()
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where 'age' column matches 'ages_manual'
age_equ = banking['age'] == ages_manual

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Print the number of inconsistent ages
print("Number of inconsistent ages:", inconsistent_ages.shape[0])
