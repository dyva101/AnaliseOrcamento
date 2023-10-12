import pandas as pd
import datacleaning as dtc
import analiseexporatoria as ae
import matplotlib.pyplot as plt

print(ae.df_final['ORÇAMENTO REALIZADO (R$)']) 
plt.boxplot([ae.df_final['ORÇAMENTO REALIZADO (R$)']])

plt.title('Boxplot ORÇAMENTO REALIZADO (R$)')
plt.ylabel('Boxplot ORÇAMENTO REALIZADO (R$)')

plt.show()

#teste de coommits