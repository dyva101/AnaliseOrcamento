import pandas as pd
import datacleaning as dtc
import analiseexporatoria as ae
import matplotlib.pyplot as plt

# Certifique-se de que as colunas que você deseja converter para numérico estão corretas
ae.df_final['NOME FUNÇÃO'] = pd.to_numeric(ae.df_final['NOME FUNÇÃO'], errors='coerce')
ae.df_final['NOME SUBFUNÇÃO'] = pd.to_numeric(ae.df_final['NOME SUBFUNÇÃO'], errors='coerce')
ae.df_final['EXERCÍCIO'] = pd.to_numeric(ae.df_final['EXERCÍCIO'], errors='coerce')

# Defina rótulos para os eixos
plt.xlabel('EXERCÍCIO)')
plt.ylabel('ORÇAMENTO REALIZADO (R$)')

# Defina o título do gráfico
plt.title('Box Plot dos Gastos com Educação por Ano')

# Gire os rótulos do eixo x para melhor legibilidade (opcional)
plt.xticks(rotation=45)

# Exiba o gráfico
plt.show()




