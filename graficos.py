# https://tmfilho.github.io/pyestbook/math/05_matp.html(fonte)
import matplotlib.pyplot as mp
import numpy as np
import pandas as pd
import analiseexporatoria as ae
import datacleaning as dtc


df = ae.df_sem_outliers
"""
coluna_subfuncao = df['NOME SUBFUNÇÃO']

df['NOME SUBFUNÇÃO'] = df['NOME SUBFUNÇÃO'].replace(r'Outros encargos especiais|Difusão do conhecimento científico e tecnológico|Educação infantil|Outras transferências|Transferências para a educação básica|Comunicação social|Educação especial|Educação de jovens e adultos|Desenvolvimento científico|Alimentação e nutrição|Suporte profilático e terapêutico|Administração financeira|Serviços financeiros', 'Outros', regex=True)

frequencia_subfuncao = df['NOME SUBFUNÇÃO'].value_counts()


mp.figure(figsize=(6, 6))  # Defina o tamanho da figura
mp.pie(frequencia_subfuncao, labels=frequencia_subfuncao.index, autopct='%1.1f%%', startangle=140)
mp.title('Frequência das Palavras')
mp.axis('equal')  # Isso garante que o círculo seja desenhado de forma equilibrada

mp.show()

# Ajuste o título do gráfico
mp.title('Gastos com Educação')

# Exiba o gráfico
mp.show()
"""
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