# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from boxplot import plot_boxplot
from datacleaning import remove_outliers
from graficos import plot_histogram

# Load the data
df = pd.read_csv('data.csv')

# Remove outliers from the data
df_sem_outliers = remove_outliers(df)

# Plot a boxplot of the data
plot_boxplot(df_sem_outliers)

# Plot a histogram of the data
plot_histogram(df_sem_outliers)

# Calculate some statistics of the data
mean = df_sem_outliers.mean()
median = df_sem_outliers.median()
std = df_sem_outliers.std()

# Print the statistics
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std}")
