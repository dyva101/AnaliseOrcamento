import pandas as pd
import datacleaning as dtc
import analiseexporatoria as ae
import matplotlib.pyplot as plt

print (ae.df_final['ORÇAMENTO REALIZADO (R$)'])
data = ae.df_final['ORÇAMENTO REALIZADO (R$)']

# Crie o boxplot e obtenha os limites dos bigodes
boxplot = plt.boxplot([data])

# Obtenha os limites superior e inferior dos bigodes
whiskers = [item.get_ydata() for item in boxplot['whiskers']]
limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]

outliers = data[(data < limite_inferior) | (data > limite_superior)]
print (outliers)

# Plote o boxplot
plt.boxplot([data])

plt.title('Boxplot ORÇAMENTO REALIZADO (R$)')
plt.ylabel('Boxplot ORÇAMENTO REALIZADO (R$)')

plt.show()