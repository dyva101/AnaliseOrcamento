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
        with un.ytest.raises(TypeError):
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

class Teste
#class TestePlotarColunasEmpilhadas(un.TestCase):