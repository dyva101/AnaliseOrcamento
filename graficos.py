# https://tmfilho.github.io/pyestbook/math/05_matp.html(fonte)
import matplotlib.pyplot as mp
import numpy as np
import pandas as pd
import analiseexporatoria as ae
import datacleaning as dtc


df = ae.df_sem_outliers

def grafico_de_barras(df, coluna):
    """
    Cria um gráfico de barras, onde o eixo x seja  a partir de um DataFrame.
    
    Parameters:
    df (DataFrame): O DataFrame contendo os dados a serem plotados.
    coluna (str): O nome da coluna no DataFrame a ser usado para criar o gráfico de barras.
    
    Retorna:
    None
    """
    data = df[coluna]
    data = data.value_counts()
    data = data.sort_index()
    data.plot.bar()
    mp.show()
#-------------------------------------------------------------------------------------------
orcamentos = list()
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

for year in years:
    df_year = dtc.filtrar_coluna_com_termo(df, 'EXERCÍCIO', year)
    orcamentos.append(df_year['ORÇAMENTO REALIZADO (R$)'].sum())

mp.clf()

height = orcamentos

mp.bar(list(map(str, years)), height, width=0.8, align='center', log=True)

mp.xlabel('Ano')
mp.title("ORÇAMENTO ANUAL (2014-2023)")
mp.show()

"""

'''
‘bar’ or ‘barh’ for bar plots

‘hist’ for histogram

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