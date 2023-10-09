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

def filtrar_coluna_com_termo(df, coluna_a_ser_filtrada: str, topico_desejado: str):
    """filtrar_coluna_com_termo

    #(descricao da funcao)#

    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada (str): _description_
        topico_desejado (str): _description_

    Returns:
        _type_: _description_
    """
    filtro = df['coluna_a_ser_filtrada'].str.contains(topico_desejado, case=False)
    df = df[filtro]
    
    return df