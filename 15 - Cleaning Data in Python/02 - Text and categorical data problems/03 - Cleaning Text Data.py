# Import necessary packages
import pandas as pd

# Load the airlines dataset
airlines = pd.read_csv('../datasets/airlines_final.csv')

# Remove honorifics from the 'full_name' column
honorifics = ["Dr.", "Mr.", "Miss", "Ms."]
for honorific in honorifics:
    airlines['full_name'] = airlines['full_name'].str.replace(honorific, "")

# Assert that 'full_name' has no remaining honorifics
assert not airlines['full_name'].str.contains('|'.join(honorifics)).any()

# Calculate the length of each row in the 'survey_response' column
resp_length = airlines['survey_response'].str.len()

# Select rows where response length is greater than 40 characters
airlines_survey = airlines[resp_length > 40]

# Assert that the minimum 'survey_response' length is greater than 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print the 'survey_response' column for the selected rows
print("Selected 'survey_response' column:")
print(airlines_survey['survey_response'])