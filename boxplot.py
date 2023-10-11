import pandas as pd
import analiseexporatoria as ae
import matplotlib.pyplot as plt

# Selecionar apenas as colunas numéricas do DataFrame
numeric_columns = ae.df_final.select_dtypes(include=['number'])

fig, axes = plt.subplots(figsize=(10, 6), nrows=1, ncols=len(numeric_columns.columns))

for i, column in enumerate(numeric_columns.columns):
    numeric_columns[column].plot(kind='box', ax=axes[i])

plt.show()
