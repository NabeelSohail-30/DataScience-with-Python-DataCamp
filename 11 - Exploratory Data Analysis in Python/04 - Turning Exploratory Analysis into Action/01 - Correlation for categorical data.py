import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

salaries = pd.read_csv('../datasets/ds_salaries_clean.csv')

# Print the relative frequency of Job_Category
print(salaries['Job_Category'].value_counts())

# Print the relative frequency of Job_Category
print(salaries['Job_Category'].value_counts(normalize=True))


# Cross-tabulate Company_Size and Experience
print(pd.crosstab(salaries["Company_Size"], salaries["Experience"]))


# Cross-tabulate Job_Category and Company_Size
print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"]))


# Cross-tabulate Job_Category and Company_Size
print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"],
            values=salaries["Salary_USD"], aggfunc="median"))


# Cross-tabulate Job_Category and Company_Size
print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"],
            values=salaries["Salary_USD"], aggfunc="mean"))