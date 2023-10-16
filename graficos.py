import importlib
# https://tmfilho.github.io/pyestbook/math/05_matp.html(fonte)
import matplotlib.pyplot as mp
import numpy as np
import pandas as pd
import datacleaning as dtc



def plotar_colunas(df: pd.DataFrame, coluna_de_empilhamento: str, y_column: str, title="Colunas Empilhadas"):
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

    if df.empty:
        raise ValueError("O DataFrame está vazio.")

    if not isinstance(df, pd.DataFrame):
        raise TypeError("O argumento 'df' deve ser um DataFrame válido.")

    if not all(col in df.columns for col in [coluna_de_empilhamento, y_column]):
        colunas_ausentes = [col for col in [coluna_de_empilhamento, y_column] if col not in df.columns]
        raise ValueError(f"As colunas especificadas não estão presentes no DataFrame: {', '.join(colunas_ausentes)}")

    df_for_stacked_chart = pd.DataFrame({coluna_de_empilhamento: df[coluna_de_empilhamento], coluna_de_empilhamento: df[coluna_de_empilhamento], y_column: df[y_column]})

    if df_for_stacked_chart.isnull().values.any():
        raise ValueError("O DataFrame contém valores NaN nas colunas especificadas.")

    if not df[y_column].dtype in [np.float64, np.int64]:
        raise TypeError(f"The data type of column '{y_column}' is not suitable for plotting.")

    df_for_stacked_chart.groupby(coluna_de_empilhamento)[y_column].sum().plot(kind='bar', stacked=True)

    mp.xlabel(coluna_de_empilhamento)
    mp.ylabel(y_column)
    mp.title(title)

    mp.show()

def substituir_coluna_por_lista_especificada(df: pd.DataFrame, column: str, substituto: str, termos_a_serem_substituidos: list):
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

    for termo in termos_a_serem_substituidos:
        df_copy[column] = df_copy[column].replace(termo, substituto, regex=True)

    return df_copy

def plotar_colunas_empilhadas_normalizado(df: pd.DataFrame, coluna_de_empilhamento: str, x_column: str, y_column: str, title="Colunas Empilhadas Normalizadas"):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("O argumento 'df' deve ser um DataFrame válido.")
    
    if not all(col in df.columns for col in [x_column, y_column, coluna_de_empilhamento]):
        colunas_ausentes = [col for col in [x_column, y_column, coluna_de_empilhamento] if col not in df.columns]
        raise ValueError(f"As colunas especificadas não estão presentes no DataFrame: {', '.join(colunas_ausentes)}")

    # Agregando os valores duplicados antes de pivotar o DataFrame
    df_grouped = df.groupby([x_column, coluna_de_empilhamento])[y_column].sum().reset_index()

    # Pivotando o DataFrame para ter as categorias de empilhamento como colunas
    df_pivoted = df_grouped.pivot(index=x_column, columns=coluna_de_empilhamento, values=y_column).fillna(0)

    # Normalizando para obter as porcentagens
    df_normalized = df_pivoted.div(df_pivoted.sum(axis=1), axis=0) * 100

    # Criando o gráfico de barras empilhadas normalizado
    ax = df_normalized.plot(kind='bar', stacked=True, figsize=(10, 6))

    mp.xlabel(x_column)
    mp.ylabel("Porcentagem")
    mp.title(title)
    mp.legend(title=coluna_de_empilhamento)
    mp.show()

def plotar_histograma_com_filtro(df, coluna, coluna_a_ser_filtrada='', filtro='', title=''):
    """
    Utiliza um dataframe e uma coluna que a ele pertence para gerar um histograma, após filtrá-lo a partir de uma de suas colunas e um termo ou expressão.

    Parameters:
        df (pd.DataFrame): dataframe original
        coluna (str): será mostrada a distribuição dos dados dessa coluna
        coluna_a_ser_filtrada (str): coluna para filtrar os dados
        filtro (): termo ou expressão para filtrar os registros do dataframe
        title (str): título do histograma
    """

    if filtro == '':
        mp.hist(df[coluna], bins=50, log=True)
        mp.title(title)

        mp.show()

    else:

        df_hist = df[df[coluna_a_ser_filtrada] == filtro]

        print(df_hist)

        mp.hist(df_hist[coluna], bins=50, log=True)
        mp.title(title)

        mp.show()


