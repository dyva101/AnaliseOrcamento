import pandas as pd

def coletar_colunas(df, colunas_desejadas: list):
    """coletar_colunas

    função que gera, a partir do dataframe original, um novo dataframe apenas com as colunas desejadas

    Parameters:
        df (dataframe): dataframe original
        colunas_desejadas (list): lista com strings representando as colunas desejadas

    Returns:
        dataframe: dataframe apenas com as colunas desejadas
    """
    df = df[[colunas_desejadas]]
    return df