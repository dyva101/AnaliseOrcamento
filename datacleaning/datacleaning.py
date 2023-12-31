""" Módulo para a limpeza e filtragem dos dados
Nesse módulo, funções especializadas em trabalhar com dataframes fazem sua limpeza e filtragem de diferentes maneiras.
Também está presente a função valores_invalidos(), que garante a integridade e homogeneidade dos dados do dataframe em toda as colunas
"""

import pandas as pd
import unittest as un

def coletar_colunas(df, colunas_desejadas: list):
    """Essa função gera um novo dataframe contendo apenas as colunas desejadas do dataframe original
    
    Parameters:
        df (dataframe): dataframe original
        colunas_desejadas (list): lista com as expressões representando as colunas desejadas

    Returns:
        dataframe: dataframe apenas com as colunas desejadas
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
        coluna_a_ser_filtrada: nome da coluna a ser filtrada
        topico_desejado: termo, valor ou expressão que deve ser identificada
    Returns:
        dataframe(pd.DataFrame): dataframe filtrado
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
    """Esta função filtra um dataframe com base em uma coluna numérica e uma restrição.

    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada: nome da coluna para aplicar o filtro
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
    """
    Identifica colunas com valores inválidos em um DataFrame, ou colunas com mais de um tipo de dado presentes, garantindo a sua homogeneidade.

    Parameters:
        df (dataframe): Dataframe desejado

    Examples:
    >>> df = pd.DataFrame({'A': [1, 2, 'three', 4], 'B': [5.1, 6.2, None, 8.4]})
    >>> valores_invalidos(df)
    ValueError: A coluna 'A' contém valores com tipos de dados diferentes.
    
    >>> df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5.1, 6.2, None, 8.4]})
    >>> valores_invalidos(df)
    ValueError: As colunas com valores inválidos são: [('A', [2])]
    
    >>> valores_invalidos("rafael pinho")
    TypeError: Não foi passado um dataframe válido!
    
    >>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5.1, 6.2, 7.3, 8.4]})
    >>> valores_invalidos(df)
    None

    """
    error_columns = []

    try:
        for column in df.columns:
            tipos_de_dados = df[column].apply(type).unique()

            if df[column].isna().any():
                index = df.index[df[column].isna()].tolist()
                error_columns.append((column, index))

            elif len(tipos_de_dados) > 1:
                raise ValueError

        if error_columns:
            raise ValueError
        
        else:
            return None
    except TypeError:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Não foi passado um dataframe válido!")
    except ValueError:
        if len(tipos_de_dados) > 1:
            raise ValueError(f"A coluna '{column}' contém valores com tipos de dados diferentes.")
        if error_columns:
            raise ValueError(f"As colunas com valores inválidos são: {error_columns}")



def filtrar_coluna_com_termos(df, coluna_a_ser_filtrada, topicos_desejados: list):
    """
    Essa função filtra a coluna de um dataframe com base em uma lista de termos desejados. 
    Só restarão as linhas que contenham pelo menos um dos termos da lista na coluna.

    Parameters:
        df (dataframe): dataframe original
        coluna_a_ser_filtrada: nome da coluna para filtrar
        topicos_desejados (list): lista de termos ou expressões a serem identificadas

    Returns:
        dataframe: dataframe filtrado

    Raises:
        TypeError: Se o argumento `topicos_desejados` não for uma lista ou se o argumento `df` não for um DataFrame válido.
        KeyError: Se a coluna especificada não pertencer ao DataFrame passado.
        ValueError: Se a lista de `topicos_desejados` estiver vazia.

    Examples:
    >>> df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
    >>> topicos = ['Taylor', 'AlgLin']
    
    # Filtrar linhas que contenham pelo menos um dos tópicos
    >>> filtrar_coluna_com_termos(df, 'Texto', topicos)
    Textos
    1  August: melhor da Taylor
    3  I Love AlgLin

    # Tentativa de filtro com coluna inexistente
    >>> filtrar_coluna_com_termos(df, 'Conteudo', topicos)
    KeyError: 'A coluna desejada não pertence ao dataframe passado'

    # Tentativa de filtro com lista de termos vazia
    >>> filtrar_coluna_com_termos(df, 'Texto', [])
    ValueError: 'A lista de termos desejados está vazia'

    # Tentativa de filtro com argumento `topicos_desejados` que não é uma lista
    >>> filtrar_coluna_com_termos(df, 'Texto', 'Python')
    TypeError: 'Você deve passar uma lista de termos'
    
    # Tentativa de filtro com objeto não-DataFrame
    >>> filtrar_coluna_com_termos('Isso não é um DataFrame', 'Texto', topicos)
    TypeError: 'Não foi passado um dataframe válido!'
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise TypeError
        
        if df.empty:
            return pd.DataFrame()

        if not isinstance(topicos_desejados, list):
            raise TypeError
        
        if len(topicos_desejados) == 0:
            raise ValueError
        
        filtro = df[coluna_a_ser_filtrada].str.contains('|'.join(topicos_desejados), case=False)
        df = df[filtro]
        return df
    
    except TypeError:
        if not isinstance(topicos_desejados, list):
            raise TypeError("Você deve passar uma lista de termos")
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Não foi passado um dataframe válido!")
    except KeyError:
        if coluna_a_ser_filtrada not in df.columns:
            raise KeyError("A coluna desejada não pertence ao dataframe passado")
    except ValueError:
        if len(topicos_desejados) == 0:
            raise ValueError("A lista de termos desejados está vazia")

### TESTES UNITÁRIOS ###
class TesteColetarColunas(un.TestCase):
    
    def test_valid_dataframe_and_columns(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        result = coletar_colunas(df, ['A', 'B'])
        expected = pd.DataFrame({'A': [1, 999, 31], 'B': ['EMAp', 'força', 'ficar']})
        assert result.equals(expected)

    def test_empty_list_of_columns(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        result = coletar_colunas(df, [])
        expected = pd.DataFrame()
        assert result.equals(expected)
    
    def test_non_list_object_as_second_argument(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        with self.assertRaises(TypeError):
            coletar_colunas(df, 2) 
    
    def test_non_dataframe_object_as_first_argument(self):
        with self.assertRaises(TypeError):
            coletar_colunas("osmar", ['A','B'])   

    def test_column_not_belonging_to_dataframe(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        with self.assertRaises(KeyError):
            coletar_colunas(df, ['A','F'])

    def test_no_list_of_columns_passed(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        result = coletar_colunas(df, ['A', 'B', 'C'])
        expected = pd.DataFrame({'A': [1, 999, 31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]})
        assert result.equals(expected)

class TesteFiltrarColunaComTermo(un.TestCase):
    
    def test_filtered_dataframe_with_desired_term(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        filtered_df = filtrar_coluna_com_termo(df, 'letras do alfabeto', 'a')
        assert filtered_df.equals(pd.DataFrame({'letras do alfabeto': ['a'], 'forma maiúscula': ['A']}))
        
    def test_empty_dataframe_if_no_rows_contain_desired_term(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        filtered_df = filtrar_coluna_com_termo(df, 'letras do alfabeto', 'z')
        assert filtered_df.empty
    
    def test_case_insensitive(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        filtered_df = filtrar_coluna_com_termo(df, 'letras do alfabeto', 'A')
        assert filtered_df.equals(pd.DataFrame({'letras do alfabeto': ['a'], 'forma maiúscula': ['A']}))       
    
    def test_input_dataframe_not_pandas_dataframe(self):
        with self.assertRaises(TypeError):
            filtrar_coluna_com_termo("almir", 'forma maiúscula', 'c')
            
    def test_input_column_name_not_string(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        with self.assertRaises(TypeError):
            filtrar_coluna_com_termo(df, 23, 'A')

    def test_input_column_name_not_exist(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        with self.assertRaises(KeyError):
            filtrar_coluna_com_termo(df, 'forma numérica', 'a')

class TesteFiltrarColunasNumericas:
    
    def test_filter_non_negative_integer_values(self):
            df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
            result = filtrar_colunas_numericas(df, 'A', 1)
            expected = pd.DataFrame({'A': [1, 3, 5], 'B': [0, -2, -4]}, index=[0, 2, 4])
            assert result.equals(expected)
    
    def test_filter_non_negative_float_values(self):
        df = pd.DataFrame({'A': [1.5, -2.5, 3.5, -4.5, 5.5], 'B': [0.5, 1.5, -2.5, 3.5, -4.5]})
        result = filtrar_colunas_numericas(df, 'A', 1)
        expected = pd.DataFrame({'A': [1.5, 3.5, 5.5], 'B': [0.5, -2.5, -4.5]}, index=[0, 2, 4])
        assert result.equals(expected)
        
    def test_filter_column_name_not_string(self):
        df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
        with self.assertRaises(TypeError):
            filtrar_colunas_numericas(df, 23, 1)
            
    def test_filter_non_dataframe_object(self):
        with self.assertRaises(TypeError):
            filtrar_colunas_numericas("almir", 'A', 1)
            
    def test_filter_invalid_integer_restriction(self):
        df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
        with self.assertRaises(ValueError):
            filtrar_colunas_numericas(df, 'A', 2)
            
    def test_filter_non_float_restriction(self):
        df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
        with self.assertRaises(TypeError):
            filtrar_colunas_numericas(df, 'A', 1.5)
    
    def test_filter_non_existing_column(self):
        df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
        with self.assertRaises(KeyError):
            filtrar_colunas_numericas(df, 'C', 1)
            
    def test_filter_empty_dataframe(self):
        df = pd.DataFrame()
        result = filtrar_colunas_numericas(df, 'A', 1)
        expected = pd.DataFrame()
        assert result.equals(expected)
    
class TesteValoresInvalidos(un.TestCase):
    
    def test_no_invalid_values(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5.1, 6.2, 7.3, 8.4]})
        assert valores_invalidos(df) == None

    def test_one_type_of_data(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5.1, 6.2, 7.3, 8.4]})
        assert valores_invalidos(df) == None

    def test_one_column(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4]})
        assert valores_invalidos(df) == None

    def test_all_columns_with_nan(self):
        df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5.1, 6.2, None, 8.4]})
        with self.assertRaises(ValueError):
            valores_invalidos(df)
            
    def test_some_columns_with_nan(self):
        df = pd.DataFrame({'A': [1, 2, 'three', 4], 'B': [5.1, 6.2, None, 8.4]})
        with self.assertRaises(ValueError):
            valores_invalidos(df)
            
    def test_all_columns_with_only_nan(self):
        df = pd.DataFrame({'A': [None, None, None, None], 'B': [None, None, None, None]})
        with self.assertRaises(ValueError):
            valores_invalidos(df)
            
class TesteFiltrarColunasComTermos(un.TestCase):
    
    def test_filtered_dataframe_with_at_least_one_term(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        topicos = ['Taylor', 'AlgLin']
        expected_df = pd.DataFrame({'Textos': ['August: melhor da Taylor', 'I Love AlgLin']})
    
        result_df = filtrar_coluna_com_termos(df, 'Textos', topicos)
        result_df = result_df.reset_index(drop=True)
    
        assert result_df.equals(expected_df)

    def test_empty_dataframe_if_no_matches_found(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        topicos = ['Python', 'Java']
        expected_df = pd.DataFrame(columns=['Textos'])
    
        result_df = filtrar_coluna_com_termos(df, 'Textos', topicos)
    
        assert result_df.equals(expected_df)
        
    def test_original_dataframe_if_topicos_desejados_is_empty(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        with self.assertRaises(ValueError):
            filtrar_coluna_com_termos(df, 'Textos', [])

    def test_raises_TypeError_if_topicos_desejados_not_list(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        topicos = 'Python'
    
        with self.assertRaises(TypeError):
            filtrar_coluna_com_termos(df, 'Textos', topicos)
            
    def test_raises_TypeError_if_df_not_valid_DataFrame(self):
        df = 'Isso não é um DataFrame'
        topicos = ['Taylor', 'AlgLin']
    
        with self.assertRaises(TypeError):
            filtrar_coluna_com_termos(df, 'Textos', topicos)
            
    def test_raises_KeyError_if_coluna_a_ser_filtrada_not_column_in_df(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        topicos = ['Taylor', 'AlgLin']
    
        with self.assertRaises(KeyError):
            filtrar_coluna_com_termos(df, 'Conteudo', topicos)
            
if __name__ == "__main__":
    un.main()