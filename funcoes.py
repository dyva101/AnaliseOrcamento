# https://tmfilho.github.io/pyestbook/math/05_matp.html(fonte)
import matplotlib.pyplot as mp
import numpy as np
import pandas as pd


mp.plot([0, 1], [1, 0]) #plotar um gráfico de linhas
figura_vazia = mp.figure()

df = pd.DataFrame({'length': [1.5, 0.5, 1.2, 0.9, 3],
                  'width': [0.7, 0.2, 0.15, 0.2, 1.1]},
                  index=['pig', 'rabbit', 'duck', 'chicken', 'horse'])
plot = df.plot(title="DataFrame Plot")

# Exemplo de dados
dados = {'Categoria': ['A', 'B', 'C', 'D'],
         'Valores': [30, 40, 20, 10]}

# Crie um DataFrame
df = pd.DataFrame(dados)

# Plote o gráfico de pizza
df.plot(kind='pie', y='Valores', labels=df['Categoria'], autopct='%1.1f%%', legend=False)

# Ajuste o título do gráfico
mp.title('Gráfico de Pizza')

# Exiba o gráfico
mp.show()

"""

'''
‘bar’ or ‘barh’ for bar plots

‘hist’ fo+r histogram

‘box’ for boxplot

‘kde’ or ‘density’ for density plots

‘area’ for area plots

‘scatter’ for scatter plots

‘hexbin’ for hexagonal bin plots

‘pie’ for pie plots
'''

# Criar o gráfico de boxplot
fig, ax = mp.subplots()

# Personalizar as cores das caixas
boxprops = dict(linestyle='--', linewidth=1.5, color='red') # estilo de linha da caixa
flierprops = dict(marker='o', markerfacecolor='purple', markersize=5, alpha=0.5)
medianprops = dict(linestyle='-.', linewidth=1.5, color='blue')
whiskerprops = dict(linestyle='-', linewidth=1.5, color='green')
ax.boxplot(dados, boxprops=boxprops, flierprops=flierprops, medianprops=medianprops, whiskerprops=whiskerprops)

# Personalizar os títulos e os rótulos dos eixos
ax.set_title('Gráfico de Boxplot Personalizado')
ax.set_xlabel('Conjunto de Dados')
ax.set_ylabel('Valores')

# Personalizar o eixo x
xticks = ['Dados 1', 'Dados 2', 'Dados 3']
ax.set_xticklabels(xticks)

"""