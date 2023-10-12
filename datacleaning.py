import pandas as pd

def coletar_colunas(df, colunas_desejadas: list):
    """Essa função gera um novo dataframe contendo apenas as colunas desejadas do dataframe original

    Parameters:
        df (dataframe): dataframe original
        colunas_desejadas (list): lista com strings representando as colunas desejadas

    Returns:
        dataframe: dataframe apenas com as colunas desejadas
    """
    try:
        df = df[colunas_desejadas]
        return df
    except TypeError:
        if isinstance(df, pd.DataFrame):
            print("Não foi passado um dataframe válido!")
        elif isinstance(colunas_desejadas, list):
            print("Não foi passado uma lista de colunas válidas")
    except KeyError:
        print("A coluna desejada não pertence ao dataframe passado")

def filtrar_coluna_com_termo(df, coluna_a_ser_filtrada: str, topico_desejado: str):
    """Essa função filtra a coluna de um dataframe com base em um termo desejado. Só restarão as linhas nas quais esteja escrito esse termo (e somente ele)

    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada (str): nome da coluna para filtarar
        topico_desejado (str): termo ou expressão exata que deve ser identificada

    Returns:
        dataframe: dataframe filtrado
    """

    try:
        filtro = df[coluna_a_ser_filtrada].str.contains(topico_desejado, case=False)
        df = df[filtro]
        return df
    except TypeError:
        if isinstance(df, pd.DataFrame):
            print("Não foi passado um dataframe válido!")
        elif isinstance(coluna_a_ser_filtrada, list):
            print("Não foi passado uma lista de colunas válidas")
    except KeyError:
        print("A coluna desejada não pertence ao dataframe passado")

def filtrar_colunas_numericas(df, coluna_a_ser_filtrada: str, restricao: int):
    """Esta função filtra um dataframe com base em uma coluna numérica e uma restrição.
    
    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada (str): nome da coluna para aplicar o filtro
        restricao (str): 0 caso queira apenas os valores negativos; 1 para os valores não-negativos (incluindo o zero)

    Returns:
        dataframe: dataframe filtrado
    """
    if restricao == 1:
        filtro = df[coluna_a_ser_filtrada] >= 0

    elif restricao == 0:
        filtro = df[coluna_a_ser_filtrada] < 0

    return df[filtro]

def filtrar_datas(df, datas_desejadas: list):
    """Filtrar um dataframe com base em datas desejadas em uma coluna que contenha datas.

    Parameters:
        df (dataframe): dataframe original
        datas_desejadas (list): lista com as datas para filtragem dos registros

    Returns:
        dataframe: dataframe filtrado
    """
    filtro = df["EXERCÍCIO"].str.contains(datas_desejadas)

    return df[filtro]

def valores_invalidos(df):
    """Identificar colunas com valores inválidos em um DataFrame.

    Parameters:
        df (dataframe): Dataframe desejado
    """
    error_columns = []

    for column in df.columns:
        tipos_de_dados = df[column].apply(type).unique()

        #guardando as colunas e posições onde há valores inválidos
        if df[column].isna().any() == True:
            index = df.index[df[column].isna()].tolist()
            error_columns.append(column)
        #levantando erro caso haja mais de um tipo de dado em uma coluna
        if len(tipos_de_dados) > 1:#
            raise ValueError(f"A coluna '{column}' contém valores com tipos de dados diferentes.")
    
    if not error_columns:
        raise ValueError(f"As colunas '{tipos_de_dados}' contém valores inválidos, respectivamente, nas seguintes posições: {index}")