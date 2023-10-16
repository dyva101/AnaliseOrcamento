import unittest as un
import pandas as pd
import datacleaning as dtc
import boxplot as bx 
import graficos as grf

#datacleaning

class TesteColetarColunas(un.TestCase):
    
    def test_colunas_desejadas_validas(self):
        dataframe = {'A': [1, 999, 31], 'B': ['EMAp', 'força', 'ficar'], 'C': [8.7, 7.5, 3.7]}
        df = pd.DataFrame(dataframe)

        # Teste para colunas 'A' e 'B'
        colunas_desejadas = ['A', 'B']
        resultado = dtc.coletar_colunas(df, colunas_desejadas)
        expected_df = pd.DataFrame({'A': [1, 999, 31], 'B': ['EMAp', 'força', 'ficar']})
        self.assertTrue(resultado.equals(expected_df))

        # Teste para colunas 'A' e 'C'
        colunas_desejadas = ['A', 'C']
        resultado = dtc.coletar_colunas(df, colunas_desejadas)
        expected_df = pd.DataFrame({'A': [1, 999, 31], 'C': [8.7, 7.5, 3.7]})
        self.assertTrue(resultado.equals(expected_df))


#class TestePlotarColunasEmpilhadas(un.TestCase):