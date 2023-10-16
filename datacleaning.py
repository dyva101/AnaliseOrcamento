import pandas as pd

def coletar_colunas(df, colunas_desejadas: list):
    """Essa função gera um novo dataframe contendo apenas as colunas desejadas do dataframe original

    exemplo: 
        >>> dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        >>> df = DataFrame(dataframe)
        >>> coletar_colunas(df, ['A', 'B'])
          A     B  
          1  EMAp 
        999 força 
         31 ficar 
         
        >>> coletar_colunas(df, ['A', 'C'])
          A    C
          1  8.7
        999  7.5
         31  3.7
         
        >>> coletar_colunas(df, ['A','F'])
        KeyError: A coluna desejada não pertence ao dataframe passado
        
        >>> coletar_colunas(df, ['2'])
        TypeError: Não foi passado uma lista de colunas válidas
        
        >>> coletar_colunas(osmar, ['A','B'])
        TypeError: Não foi passado um dataframe válido
 
    Parameters:
        df (dataframe): dataframe original
        colunas_desejadas (list): lista com strings representando as colunas desejadas

    Returns:
        dataframe: dataframe apenas com as colunas desejadas
    """
    try:
        
        if colunas_desejadas==[]:
            return pd.DataFrame()
        
        df = df[colunas_desejadas]
        return df
    
    except TypeError:
        if isinstance(df, pd.DataFrame):
            raise TypeError("Não foi passado um dataframe válido!")
        elif isinstance(colunas_desejadas, list):
            raise TypeError("Não foi passado uma lista de colunas válidas")
    except KeyError:
        raise KeyError("A coluna desejada não pertence ao dataframe passado")
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

def filtrar_coluna_com_termo(df, coluna_a_ser_filtrada: str, topico_desejado):
    """Essa função filtra a coluna de um dataframe com base em um termo desejado. Só restarão as linhas nas quais esteja escrito esse termo (e somente ele)
    
    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada (str): nome da coluna para filtrar
        topico_desejado (str): termo ou expressão exata que deve ser identificada

        Ex: 
        >>> dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        >>> df = DataFrame(dataframe)


        >>> filtrar_coluna_com_termo(df, 'letras do alfabeto', 'a')

        letras do alfabeto 
               a                 
        #TODO: "acrescentar esse tratamento"
        >>> filtrar_coluna_com_termo(df, 'forma maiúscula', 'k')
        NaoContemValor: foi passado um DataFrame vazio
        
        >>> filtrar_coluna_com_termo(df, 'forma maiúscula', '2')
        TypeError: você não passou um termo válido

        >>> filtrar_coluna_com_termo(df, 'forma numérica', 'a')
        KeyError: A coluna desejada não pertence ao dataframe passado

        >>> filtrar_coluna_com_termo(almir, 'forma maiúscula', 'c')
        TypeError: Não foi passado um dataframe válido
            #TODO: "acrescentar esse tratamento"
        >>> filtrar_coluna_com_termo(df, ['forma maiúscula', 'letras do alfabeto'], 'a')
        TypeError: você só pode passar uma coluna por vez


    Returns:
        dataframe: dataframe filtrado
    """
    try:
        if type(topico_desejado) == str:
            filtro = df[coluna_a_ser_filtrada].str.contains(topico_desejado, case=False)
            df = df[filtro]
            return df
        else:
            filtro = df[coluna_a_ser_filtrada] == topico_desejado
            df = df[filtro]
            return df
    except TypeError:
        if not isinstance(df, pd.DataFrame):
            print("Não foi passado um dataframe válido!")
        elif not isinstance(coluna_a_ser_filtrada, list):
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
    try:
        if restricao == 1:
            filtro = df[coluna_a_ser_filtrada] >= 0

        elif restricao == 0:
            filtro = df[coluna_a_ser_filtrada] < 0

        else:
            raise ValueError("A restrição deve ser ou igual à 0 ou igual à 1")
        
        return df[filtro]
    except TypeError:
        if isinstance(df, pd.DataFrame):
            print("Não foi passado um dataframe válido!")
        elif isinstance(coluna_a_ser_filtrada, list):
            print("Não foi passado uma lista de colunas válidas")
        elif isinstance(restricao, int):
            print("O número passado não é um inteiro")
    except KeyError:
        print("A coluna desejada não pertence ao dataframe passado")
            
def valores_invalidos(df):
    """Identificar colunas com valores inválidos em um DataFrame.

    Parameters:
        df (dataframe): Dataframe desejado
    """
    error_columns = []

    for column in df.columns:
        tipos_de_dados = df[column].apply(type).unique()

        # Guardando as colunas e posições onde há valores inválidos
        if df[column].isna().any():
            index = df.index[df[column].isnan()].tolist()
            error_columns.append((column, index))

        # Levantando erro caso haja mais de um tipo de dado em uma coluna
        if len(tipos_de_dados) > 1:
            raise ValueError(f"A coluna '{column}' contém valores com tipos de dados diferentes.")

    if error_columns:
        # Se houver colunas com valores inválidos
        raise ValueError(f"As colunas com valores inválidos são: {error_columns}")

def filtrar_coluna_com_termos(df, coluna_a_ser_filtrada: str, topicos_desejados):
    """Essa função filtra a coluna de um dataframe com base em uma lista de termos desejados. 
       Só restarão as linhas que contenham pelo menos um dos termos da lista na coluna.

    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada (str): nome da coluna para filtrar
        topicos_desejados (list): lista de termos ou expressões a serem identificados

    Returns:
        dataframe: dataframe filtrado
    """
    try:
        if df.empty:
            raise ValueError("O dataframe está vazio")
    
        if not isinstance(topicos_desejados, list):
            raise TypeError("Você deve passar uma lista de termos válidos")
        
        if len(topicos_desejados) == 0:
            raise ValueError("A lista de termos desejados está vazia")
        
        # Use .str.contains para verificar se algum dos termos aparece na coluna
        filtro = df[coluna_a_ser_filtrada].str.contains('|'.join(topicos_desejados), case=False)
        df = df[filtro]
        return df
    except TypeError as e:
        print(e)
    except KeyError:
        print("A coluna desejada não pertence ao dataframe passado")
    except ValueError as e:
        print(e)
    except:
        print("Ocorreu um erro não especificado.")
