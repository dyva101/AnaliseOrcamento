import pandas as pd
import datacleaning as dtc
import matplotlib.pyplot as plt 

def boxplot_coluna_de_dataframe(df, coluna):
    data = df[coluna]

    plt.boxplot([data])

    plt.show()

    """
    Cria um gráfico de boxplot para uma coluna específica de um DataFrame.

    Parameters:
        df (pandas.DataFrame): O DataFrame contendo os dados.
        coluna (str): O nome da coluna a ser visualizada no gráfico de boxplot.

    Returns:
        None
    """

def separar_outliers_colunas_numericas(df, coluna_numerica):
    
    data = df[coluna_numerica]
    boxplot = plt.boxplot(data)
    whiskers = [item.get_ydata() for item in boxplot['whiskers']]
    limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]

    df_com_outliers = df[(df[coluna_numerica] < limite_inferior) | (df[coluna_numerica] > limite_superior)]

    return df_com_outliers
    
    """
    Separa os outliers de uma coluna numérica de um DataFrame com base em um boxplot.

    Parameters:
        df (pandas.DataFrame): O DataFrame contendo os dados.
        coluna_numerica (str): O nome da coluna numérica que deseja separar os outliers.

    Returns:
        pandas.DataFrame: Um novo DataFrame contendo apenas as linhas que correspondem aos outliers da coluna numérica.
    """

def criar_dataframe_sem_outliers(df, coluna_numerica):
    data = df[coluna_numerica]
    boxplot = plt.boxplot(data)
    whiskers = [item.get_ydata() for item in boxplot['whiskers']]
    limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]
    df_sem_outliers = df[
    (df[coluna_numerica] >= limite_inferior) &
    (df[coluna_numerica] <= limite_superior)
    ]

    return df_sem_outliers 