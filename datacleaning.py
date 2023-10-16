import pandas as pd

def coletar_colunas(df, colunas_desejadas: list):
    """Essa função gera um novo dataframe contendo apenas as colunas desejadas do dataframe original

    exemplo: 
        >>> dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        >>> df = pd.DataFrame(dataframe)
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
        
        >>> coletar_colunas(df, 2)
        TypeError: Não foi passado uma lista de colunas válidas
        
        >>> coletar_colunas("osmar", ['A','B'])
        TypeError: Não foi passado um dataframe válido
 
    Parameters:
        df (dataframe): dataframe original
        colunas_desejadas (list): lista com strings representando as colunas desejadas

    Returns:
        dataframe: dataframe apenas com as colunas desejadas
    """
    try:
        
        if not isinstance(colunas_desejadas, list):
            raise TypeError
        
        if colunas_desejadas == [] or colunas_desejadas == None:
            return pd.DataFrame()
        
        df = df[colunas_desejadas]
        return df
    
    except TypeError:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Não foi passado um dataframe válido!")
        if not isinstance(colunas_desejadas, list):
            raise TypeError("Não foi passado uma lista de colunas válidas") 
    except KeyError:
        raise KeyError("A coluna desejada não pertence ao dataframe passado")
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

def filtrar_coluna_com_termo(df, coluna_a_ser_filtrada, topico_desejado):
    """Essa função filtra a coluna de um dataframe com base em um termo desejado. Só restarão as linhas nas quais esteja escrito esse termo (e somente ele)
    
    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada (str): nome da coluna a ser filtrada
        topico_desejado: termo, valor ou expressão que deve ser identificada

    Exemplos:
        >>> dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        >>> df = pd.DataFrame(dataframe)


        >>> filtrar_coluna_com_termo(df, 'letras do alfabeto', 'a')

        letras do alfabeto 
               a                 
        
        >>> df_empty = pd.DataFrame()
        >>> filtrar_coluna_com_termo(df_empty, 'forma maiúscula', 'k')
        pd.DataFrame()
        
        >>> filtrar_coluna_com_termo(df, 23, 'A')
        TypeError: Não foi passado uma string no nome da coluna a ser filtrada
        
        >>> filtrar_coluna_com_termo(df, 'forma maiúscula', '2')
        pd.DataFrame()

        >>> filtrar_coluna_com_termo(df, 'forma numérica', 'a')
        KeyError: A coluna desejada não pertence ao dataframe passado

        >>> filtrar_coluna_com_termo("almir", 'forma maiúscula', 'c')
        TypeError: Não foi passado um dataframe válido
            
        >>> filtrar_coluna_com_termo(df, ['forma maiúscula', 'letras do alfabeto'], 'a')
        TypeError: você só pode passar uma coluna por vez


    Returns:
        dataframe(pd.DataFrame): dataframe filtrado
    """
    try:
        
        if not isinstance(coluna_a_ser_filtrada, str):
            raise TypeError
        
        if isinstance(topico_desejado, str):
            filtro = df[coluna_a_ser_filtrada].str.contains(topico_desejado, case=False)
            df = df[filtro]
            return df
        
        elif isinstance(topico_desejado, int) or isinstance(topico_desejado, float):
            filtro = df[coluna_a_ser_filtrada] == topico_desejado
            df = df[filtro]
            return df
        
    except TypeError:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Não foi passado um dataframe válido!")
        elif not isinstance(coluna_a_ser_filtrada, str):
            raise TypeError("Não foi passado uma lista de colunas válidas")
        elif isinstance(topico_desejado, list):
            raise TypeError("você só pode passar uma coluna por vez")
    except KeyError:
        raise KeyError("A coluna desejada não pertence ao dataframe passado")

def filtrar_colunas_numericas(df, coluna_a_ser_filtrada: str, restricao: int):
    """
    Esta função filtra um dataframe com base em uma coluna numérica e uma restrição.

    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada (str): nome da coluna para aplicar o filtro
        restricao (int): 0 para valores negativos; 1 para valores não-negativos (incluindo o zero)

    Returns:
        dataframe: dataframe filtrado

    Examples:
    >>> import pandas as pd
    >>> df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})

    # Filtrar valores não-negativos na coluna 'A'
    >>> filtrar_colunas_numericas(df, 'A', 1)
       A  B
    0  1  0
    2  3 -2
    4  5 -4

    # Filtrar valores negativos na coluna 'B'
    >>> filtrar_colunas_numericas(df, 'B', 0)
       A  B
    1 -2  1
    3 -4  3
    4  5 -4

    >>> filtrar_colunas_numericas(df, 'C', 1)
    KeyError: "A coluna desejada não pertence ao dataframe passado"

    >>> filtrar_colunas_numericas(df, 'A', 2.5)
    ValueError: "O número passado não é um inteiro"

    >>> filtrar_colunas_numericas('Isso não é um DataFrame', 'A', 1)
    TypeError: "Não foi passado um dataframe válido!"
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise TypeError
        if coluna_a_ser_filtrada not in df.columns:
            raise KeyError
        if not isinstance(restricao, int):
            raise TypeError

        if restricao == 1:
            filtro = df[coluna_a_ser_filtrada] >= 0
        elif restricao == 0:
            filtro = df[coluna_a_ser_filtrada] < 0
        else:
            raise ValueError

        return df[filtro]

    except TypeError:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Não foi passado um dataframe válido!")
        if not isinstance(restricao, int):
            raise TypeError("O número passado não é um inteiro")
    except KeyError:
        raise KeyError("A coluna desejada não pertence ao dataframe passado")
    except ValueError:
        raise ValueError("A restrição deve ser igual a 0 ou igual a 1")
            
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

        if len(tipos_de_dados) > 1:
            raise ValueError(f"A coluna '{column}' contém valores com tipos de dados diferentes.")

    if error_columns:
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
