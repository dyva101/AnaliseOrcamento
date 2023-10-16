import unittest as un
import pandas as pd
import datacleaning as dtc
import boxplot as bx 
import graficos as grf

#datacleaning

class TesteColetarColunas(un.TestCase):
    
    def test_valid_dataframe_and_columns(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        result = dtc.coletar_colunas(df, ['A', 'B'])
        expected = pd.DataFrame({'A': [1, 999, 31], 'B': ['EMAp', 'força', 'ficar']})
        assert result.equals(expected)

    def test_empty_list_of_columns(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        result = dtc.coletar_colunas(df, [])
        expected = pd.DataFrame()
        assert result.equals(expected)
    
    def test_non_list_object_as_second_argument(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        with un.pytest.raises(TypeError):
            dtc.coletar_colunas(df, 2) 
    
    def test_non_dataframe_object_as_first_argument(self):
        with un.pytest.raises(TypeError):
            dtc.coletar_colunas("osmar", ['A','B'])   

    def test_column_not_belonging_to_dataframe(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        with un.pytest.raises(KeyError):
            dtc.coletar_colunascoletar_colunas(df, ['A','F'])

    def test_no_list_of_columns_passed(self):
        dataframe = {'A': [1,999,31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)
        result = dtc.coletar_colunas(df, ['A', 'B', 'C'])
        expected = pd.DataFrame({'A': [1, 999, 31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]})
        assert result.equals(expected)

class TesteFiltrarColunaComTermo(un.TestCase):
    
    def test_filtered_dataframe_with_desired_term(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        filtered_df = dtc.filtrar_coluna_com_termo(df, 'letras do alfabeto', 'a')
        assert filtered_df.equals(pd.DataFrame({'letras do alfabeto': ['a'], 'forma maiúscula': ['A']}))
        
    def test_empty_dataframe_if_no_rows_contain_desired_term(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        filtered_df = dtc.filtrar_coluna_com_termo(df, 'letras do alfabeto', 'z')
        assert filtered_df.empty
    
    def test_case_insensitive(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        filtered_df = dtc.filtrar_coluna_com_termo(df, 'letras do alfabeto', 'A')
        assert filtered_df.equals(pd.DataFrame({'letras do alfabeto': ['a'], 'forma maiúscula': ['A']}))       
    
    def test_input_dataframe_not_pandas_dataframe(self):
        with un.pytest.raises(TypeError):
            dtc.filtrar_coluna_com_termo("almir", 'forma maiúscula', 'c')
            
    def test_input_column_name_not_string(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        with un.pytest.raises(TypeError):
            dtc.filtrar_coluna_com_termo(df, 23, 'A')

    def test_input_column_name_not_exist(self):
        dataframe = {'letras do alfabeto': ['a', 'b','c', 'd' ], 'forma maiúscula': ['A', 'B', 'C', 'D']}
        df = pd.DataFrame(dataframe)
        with un.pytest.raises(KeyError):
            dtc.filtrar_coluna_com_termo(df, 'forma numérica', 'a')

class TesteFiltrarColunasNumericas:
    
    def test_filter_non_negative_integer_values(self):
            df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
            result = dtc.filtrar_colunas_numericas(df, 'A', 1)
            expected = pd.DataFrame({'A': [1, 3, 5], 'B': [0, -2, -4]}, index=[0, 2, 4])
            assert result.equals(expected)
    
    def test_filter_non_negative_float_values(self):
        df = pd.DataFrame({'A': [1.5, -2.5, 3.5, -4.5, 5.5], 'B': [0.5, 1.5, -2.5, 3.5, -4.5]})
        result = dtc.filtrar_colunas_numericas(df, 'A', 1)
        expected = pd.DataFrame({'A': [1.5, 3.5, 5.5], 'B': [0.5, -2.5, -4.5]}, index=[0, 2, 4])
        assert result.equals(expected)
        
    def test_filter_column_name_not_string(self):
        df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
        with un.pytest.raises(TypeError):
            dtc.filtrar_colunas_numericas(df, 23, 1)
            
    def test_filter_non_dataframe_object(self):
        with un.pytest.raises(TypeError):
            dtc.filtrar_colunas_numericas("almir", 'A', 1)
            
    def test_filter_invalid_integer_restriction(self):
        df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
        with un.pytest.raises(ValueError):
            dtc.filtrar_colunas_numericas(df, 'A', 2)
            
    def test_filter_non_float_restriction(self):
        df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
        with un.pytest.raises(TypeError):
            dtc.filtrar_colunas_numericas(df, 'A', 1.5)
    
    def test_filter_non_existing_column(self):
        df = pd.DataFrame({'A': [1, -2, 3, -4, 5], 'B': [0, 1, -2, 3, -4]})
        with un.pytest.raises(KeyError):
            dtc.filtrar_colunas_numericas(df, 'C', 1)
            
    def test_filter_empty_dataframe(self):
        df = pd.DataFrame()
        result = dtc.filtrar_colunas_numericas(df, 'A', 1)
        expected = pd.DataFrame()
        assert result.equals(expected)
    
class TesteValoresInvalidos(un.TestCase):
    
    def test_no_invalid_values(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5.1, 6.2, 7.3, 8.4]})
        assert dtc.valores_invalidos(df) == None

    def test_one_type_of_data(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5.1, 6.2, 7.3, 8.4]})
        assert dtc.valores_invalidos(df) == None

    def test_one_column(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4]})
        assert dtc.valores_invalidos(df) == None

    def test_all_columns_with_nan(self):
        df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5.1, 6.2, None, 8.4]})
        with un.pytest.raises(ValueError):
            dtc.valores_invalidos(df)
            
    def test_some_columns_with_nan(self):
        df = pd.DataFrame({'A': [1, 2, 'three', 4], 'B': [5.1, 6.2, None, 8.4]})
        with un.pytest.raises(ValueError):
            dtc.valores_invalidos(df)
            
    def test_all_columns_with_only_nan(self):
        df = pd.DataFrame({'A': [None, None, None, None], 'B': [None, None, None, None]})
        with un.pytest.raises(ValueError):
            dtc.valores_invalidos(df)
            
class TesteFiltrarColunasComTermos(un.TestCase):
    
    def test_filtered_dataframe_with_at_least_one_term(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        topicos = ['Taylor', 'AlgLin']
        expected_df = pd.DataFrame({'Textos': ['August: melhor da Taylor', 'I Love AlgLin']})
    
        result_df = dtc.filtrar_coluna_com_termos(df, 'Textos', topicos)
        result_df = result_df.reset_index(drop=True)
    
        assert result_df.equals(expected_df)

    def test_empty_dataframe_if_no_matches_found(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        topicos = ['Python', 'Java']
        expected_df = pd.DataFrame(columns=['Textos'])
    
        result_df = dtc.filtrar_coluna_com_termos(df, 'Textos', topicos)
    
        assert result_df.equals(expected_df)
        
    def test_original_dataframe_if_topicos_desejados_is_empty(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        with un.pytest.raises(ValueError):
            dtc.filtrar_coluna_com_termos(df, 'Textos', [])

    def test_raises_TypeError_if_topicos_desejados_not_list(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        topicos = 'Python'
    
        with un.pytest.raises(TypeError):
            dtc.filtrar_coluna_com_termos(df, 'Textos', topicos)
            
    def test_raises_TypeError_if_df_not_valid_DataFrame(self):
        df = 'Isso não é um DataFrame'
        topicos = ['Taylor', 'AlgLin']
    
        with un.pytest.raises(TypeError):
            dtc.filtrar_coluna_com_termos(df, 'Textos', topicos)
            
    def test_raises_KeyError_if_coluna_a_ser_filtrada_not_column_in_df(self):
        df = pd.DataFrame({'Textos': ['Halo: melhor da Beyonce', 'August: melhor da Taylor', 'Data Science', 'I Love AlgLin']})
        topicos = ['Taylor', 'AlgLin']
    
        with un.pytest.raises(KeyError):
            dtc.filtrar_coluna_com_termos(df, 'Conteudo', topicos)
            
