import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('')

# Set style, enable color code, and create a magenta displot
sns.set(color_codes=True)
sns.displot(df['fmr_3'], color='m')

# Show the plot
plt.show()

# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.displot(df['fmr_3'])
    plt.show()

    # Clear the plots
    plt.clf()

# Create the Purples palette
sns.palplot(sns.color_palette("Purples", 8))
plt.show()

sns.palplot(sns.color_palette("husl", 10))
plt.show()

sns.palplot(sns.color_palette("coolwarm", 6))
plt.show()