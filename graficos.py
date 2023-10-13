# https://tmfilho.github.io/pyestbook/math/05_matp.html(fonte)
import matplotlib.pyplot as mp
import numpy as np
import pandas as pd
import analiseexporatoria as ae
import datacleaning as dtc


df = ae.df_sem_outliers
#-------------------------------------------------------------------------------------------
def plot_orcamentos_anuais(df, years):
    """
    Gera um gráfico de barras empilhadas para o orçamento anual a partir de um DataFrame.

    Parameters:
        df (pd.DataFrame): O DataFrame contendo os dados.
        years (list): Uma lista de anos para os quais deseja gerar o gráfico.

    Returns:
        None
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' deve ser um DataFrame.")
    
    if not all(col in df.columns for col in ['EXERCÍCIO', 'ORÇAMENTO REALIZADO (R$)']) or not years:
        raise ValueError("O DataFrame deve conter as colunas 'EXERCÍCIO' e 'ORÇAMENTO REALIZADO (R$)' e 'years' não deve estar vazio.")

    orcamentos = []

    try:
        for year in years:
            df_year = dtc.filtrar_coluna_com_termo(df, 'EXERCÍCIO', year)
            orcamentos.append(df_year['ORÇAMENTO REALIZADO (R$)'].sum())

        mp.clf()
        mp.bar(list(map(str, years)), orcamentos, width=0.8, align='center', log=True)
        mp.xlabel('Ano')
        mp.title("ORÇAMENTO ANUAL ({}-{})".format(years[0], years[-1]))
        mp.show()
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o gráfico: {str(e)}")

#-------------------------------------------------------------------------------------------
mp.clf()
df_subset = df.copy()
df_subset['NOME SUBFUNÇÃO'] = df['NOME SUBFUNÇÃO'].replace(
    r'(Outros encargos especiais|Difusão do conhecimento científico e tecnológico|'
    r'Educação infantil|Outras transferências|Transferências para a educação básica|'
    r'Comunicação social|Educação especial|Educação de jovens e adultos|'
    r'Desenvolvimento científico|Alimentação e nutrição|Suporte profilático e terapêutico|'
    r'Administração financeira|Serviços financeiros)', 'Outros', regex=True
)
df_for_stacked_chart = pd.DataFrame({'EXERCÍCIO': df_subset['EXERCÍCIO'],
                                     'NOME SUBFUNÇÃO': df_subset['NOME SUBFUNÇÃO'],
                                     'ORÇAMENTO REALIZADO (R$)': df_subset['ORÇAMENTO REALIZADO (R$)']
                                    })

df_for_stacked_chart.groupby(['EXERCÍCIO', 'NOME SUBFUNÇÃO']).size().unstack().plot(kind='bar', stacked=True )

mp.xlabel('Ano')
mp.ylabel('Orçamento')
mp.title('Orçamento por subfunção')
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