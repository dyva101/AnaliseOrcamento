# https://tmfilho.github.io/pyestbook/math/05_matp.html(fonte)

import matplotlib.pyplot as mp

import numpy as np
import pandas as pd

import datacleaning as dtc





def plotar_colunas_empilhadas(df: pd.DataFrame, years: list, x_axis: str, y_axis: str, title: str):

    """

    Gera um gráfico de barras empilhadas para o orçamento anual a partir de um DataFrame.


    Parameters:

        df (pd.DataFrame): O DataFrame contendo os dados.

        years (list): Uma lista de anos para os quais deseja gerar o gráfico.

        x_column (str): Nome da coluna a ser usada no eixo x.

        y_column (str): Nome da coluna a ser usada no eixo y.

        title (str): Título do gráfico.


    Returns:

        None

    """

    if not isinstance(df, pd.DataFrame):

        raise ValueError("'df' deve ser um DataFrame.")
    

    if not all(col in df.columns for col in [x_axis, y_axis]):

        raise ValueError(f"O DataFrame deve conter as colunas {x_axis} e {y_axis}")

    if not years:

        raise ValueError(f"O argumento {years} não pode ser vazio")


    orcamentos = []


    try:

        for year in years:

            df_year = dtc.filtrar_coluna_com_termo(df, x_axis, year)

            orcamentos.append(df_year[y_axis].sum())

        mp.clf()

        mp.bar(years, orcamentos, width=0.8, align='center', log=True)

        mp.xlabel('Ano')
        mp.title(title)

        mp.show()

    except Exception as e:

        print(f"Ocorreu um erro ao gerar o gráfico: {str(e)}")

import pandas as pd
import matplotli .pyplot as mp

def substituir_coluna_e_plotar_empilhado_normalizado(df, x_column, y_column, title="Colunas Empilhadas"):

import 
matplotlib.pyplot as plt
em seguida cria um gráfico de barras empilhadas normalizado.

def substituir_coluna_e_plotar_empilhado_normalizado(df, column, replacements, x_column, y_column, title="Colunas Empilhadas"):
    """

    Substitui valores em uma coluna de um DataFrame, e em
 seguida cria um gráfico de barras empilhadas normalizado.


    Parameters:
        x_column (str): Nome da coluna a ser usada no eixo x.
        y_column (str): Nome da coluna a ser usada no eixo y.
        title (str): Título do gráfico (opcional).

        df (pd.DataFrame): O DataFrame contendo os dados.
        colu
        None
tendo padrões de substituição e seus valores correspondentes.
       
 x_column (str): Nome da coluna a ser usada no eixo x.
        y_column (str): Nome da coluna a
 ser usada no eixo y.
        title (str): Título do gráfico (opcional).
    
    if column not in df.columns:

        None
    
    if not all(col in df.columns for col in [x_column,  _column]):
        colunas_ausentesisi[col for col in [x_column, e_column] if col not in df.columns]
        raise ValueError(f"As colunas especificadas não estão presentes no DataFrame: {''.join(colunas_ausentes)}")

    df_copy = df.copy()

    for pattern, replacement in replacements:

    if column not in df.columns:

    df_grouped =.groupby([x_column, y_column]).size().unstack()
    df_grouped.plot(kind='bar', stacked=True, normalize=True)

    mp.xlabel(x_column)
    mp.ylabel('Orçamento')
    mp.title(title)
    mp.s ow()

def plotar_histograma_com_filtro(dflucolunat coluna_a_ser_filtrada]filtro, title):

       
    Utiliza um dataframe e uma coluna que a ele pertence paraerar um histograma, após filt-lo a partir de uma de suas colunas e um termo ou expressão.

    Parameters:
        df (pd.DataFrame): dataframe original
        coluna (str): será mostrada a distriuição dos dados dessa coluna
        coluna_a_ser_filtrada (str): coluna para filtrar os dados
        filtro (): termo ou expressão para filtrar os registros do dataframe
        title (str): título do istoy(ama
el(x_column)
    plt




    mp.title(title)


