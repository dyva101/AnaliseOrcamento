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

def substituir_coluna_por_lista_especificada(df: pd.DataFrame, column: str, replacements: list):
    """
    Substitui valores em uma coluna de um DataFrame, e devolve o dataframe com a coluna modificada.

    Parameters:
        df (pd.DataFrame): O DataFrame contendo os dados.
        column (str): O nome da coluna a ser modificada.
        replacements (list of tuples): Uma lista de tuplas contendo padrões de substituição e seus valores correspondentes.

    Returns:
        pd.DataFrame: O DataFrame com os valores substituídos.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("O argumento 'df' deve ser um DataFrame válido.")
    
    if column not in df.columns:
        raise ValueError(f"A coluna '{column}' não está presente no DataFrame.")

    df_copy = df.copy()

    for pattern, replacement in replacements:
        df_copy[column] = df_copy[column].replace(pattern, replacement, regex=True)

    return df_copy

def plotar_colunas_empilhadas_normalizado(df: pd.DataFrame, x_column: str, y_column: str, title="Colunas Empilhadas"):
    """
    Cria um gráfico de barras empilhadas normalizado a partir de um DataFrame, dadas as 2 colunas que serão os eixos.

    Parameters:
        df (pd.DataFrame): O DataFrame contendo os dados.
        x_column (str): Nome da coluna a ser usada no eixo x.
        y_column (str): Nome da coluna a ser usada no eixo y.
        title (str): Título do gráfico (opcional).

    Returns:
        None
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("O argumento 'df' deve ser um DataFrame válido.")
    
    if not all(col in df.columns for col in [x_column, y_column]):
        colunas_ausentes = [col for col in [x_column, y_column] if col not in df.columns]
        raise ValueError(f"As colunas especificadas não estão presentes no DataFrame: {', '.join(colunas_ausentes)}")

    df_grouped = df.groupby([x_column, y_column]).size().unstack()
    df_grouped.plot(kind='bar', stacked=True, normalize=True)

    mp.xlabel(x_column)  # Correção
    mp.ylabel('Orçamento')  # Correção
    mp.title(title)
    mp.show()

def plotar_histograma_com_filtro(df, coluna, coluna_a_ser_filtrada, filtro, title):
    """
    Utiliza um dataframe e uma coluna que a ele pertence para gerar um histograma, após filtrá-lo a partir de uma de suas colunas e um termo ou expressão.

    Parameters:
        df (pd.DataFrame): dataframe original
        coluna (str): será mostrada a distribuição dos dados dessa coluna
        coluna_a_ser_filtrada (str): coluna para filtrar os dados
        filtro (): termo ou expressão para filtrar os registros do dataframe
        title (str): título do histograma
    """
    df_hist = df[df[coluna_a_ser_filtrada] == filtro]
    coluna_hist = df_hist[coluna]

    mp.hist(df[coluna], bins=50, log=True)
    mp.title(title)

    mp.show()
