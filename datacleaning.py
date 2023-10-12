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
    df = df[colunas_desejadas]
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
    filtro = df[coluna_a_ser_filtrada].str.contains(topico_desejado, case=False)
    df = df[filtro]

    return df

def filtrar_colunas_numericas(df, coluna_a_ser_filtrada: str, restricao: int):
    """filtrar_coluna_numericas

    #(descricao da funcao)#

    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada (str): _description_
        restricao (str): _description_

    Returns:
        dataframe: _description_
    """
    if restricao == 1:
        filtro = df[coluna_a_ser_filtrada] >= 0

    elif restricao == 0:
        filtro = df[coluna_a_ser_filtrada] < 0

    return df[filtro]

def filtrar_datas(df, datas_desejadas: list):
    filtro = df["EXERCÍCIO"].str.contains(datas_desejadas)

    return df[filtro]

def valores_invalidos(df):
    for column in df.columns:
        quantidade_tipos_de_dados = df[column].nunique()
        if quantidade_tipos_de_dados == 1:
            return
        else:
            return
            # TODO: tratamentos de exceção