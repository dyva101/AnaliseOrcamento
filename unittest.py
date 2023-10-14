import unittest as un
import pandas as pd
import datacleaning as dtc
import boxplot as bx 
import graficos as gr 

#datacleaning

class TesteColetarColunas(un.TestCase):

#Verifica se a função retorna o DataFrame esperado quando as colunas desejadas são válidas.
    def test_sucesso(self):
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}) 
        colunas = ['A', 'B']
        resultado = coletar_colunas(df, colunas) 
        self.assertTrue(isinstance(resultado, pd.DataFrame))
        self.assertEqual(list(resultado.columns), colunas)

#Verifica se a função lida corretamente com casos em que o DataFrame não é do tipo pd.DataFrame.
    def test_tipo_de_entrada_invalido(self):
        with self.assertRaises(TypeError):
            coletar_colunas("Não é um DataFrame válido", ["A"])

#Verifica se a função lida corretamente com casos de colunas inexistentes de um DataFrame. 
    def test_coluna_inexistente(self):
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        with self.assertRaises(KeyError):
            coletar_colunas(df, ['A', 'D'])

#Verifica se a função gera exceções, quando passado uma lista não válida. 
    def test_excecao(self):
        with self.assertRaises(TypeError):
            coletar_colunas(pd.DataFrame({'A': [1, 2], 'B': [3, 4]}), "Não é uma lista válida")


