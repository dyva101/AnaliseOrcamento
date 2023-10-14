# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import boxplot as bx
import datacleaning as dtc
import graficos as grf
import analiseexporatoria as ae

df_geral = pd.read_csv("data/")

### Boxplot E Estatísticas para análise dos outliers ###

# Remove outliers from the data
df_sem_outliers = ae.df_sem_outliers

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

### Análise de correlação entre o ano eleitoral e os outros anos ###

    # Calculate the mean for the non-election years
    # Calculate the mean for the election years
    # Compare the difference in means and show if it does conffirms the hypothesis

### Análise da queda brusca de investimento no período pandêmico (2019-2021) ###

    # Calculate the mean for the pre-pandemic years
    # Calculate the mean for the pandemic years
    # Hypothesis: the mean for the pandemic years is lower than the mean for the pre-pandemic years
        # Plot a stacked bar chart of the 10 year period 2014-2023
        # Plot histograms of 2020 and 2021
    # Use all the intel gathered to confirm or reject the hypothesis

### Rankings: Governos com maior investimento bruto em educação e seus subcampos ###

    #Ranking com os 3 mandadtos do período, em ordem de investimento bruto em educação (stacked bar chart)
    #Ranking com os 3 mandatos do período, em ordem de investimento bruto em educação básica (stacked bar chart)
    #Ranking com os 3 mandatos do período, em ordem de investimento bruto em educação superior (stacked bar chart)
    #Ranking com os 3 mandatos do período, em ordem de investimento bruto em educação profissional (stacked bar chart)