import unittest as un
import pandas as pd
import datacleaning as dtc
import boxplot as bx 
import graficos as grf

#datacleaning

#class TesteColetarColunas(un.TestCase):

#Verifica se a função retorna o DataFrame esperado quando as colunas desejadas são válidas.
def test_sucesso(self):
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}) 
    colunas = ['A', 'B']
    resultado = dtc.coletar_colunas(df, colunas) 
    self.assertTrue(isinstance(resultado, pd.DataFrame))
    self.assertEqual(list(resultado.columns), colunas)

#Verifica se a função lida corretamente com casos em que o DataFrame não é do tipo pd.DataFrame.
def test_tipo_de_entrada_invalido(self):
    with self.assertRaises(TypeError):
        dtc.coletar_colunas("Não é um DataFrame válido", ["A"])

#Verifica se a função lida corretamente com casos de colunas inexistentes de um DataFrame. 
def test_coluna_inexistente(self):
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
    with self.assertRaises(KeyError):
        dtc.coletar_colunas(df, ['A', 'D'])

#Verifica se a função gera exceções, quando passado uma lista não válida. 
def test_excecao(self):
    with self.assertRaises(TypeError):
        dtc.coletar_colunas(pd.DataFrame({'A': [1, 2], 'B': [3, 4]}), "Não é uma lista válida")

#class TesteFiltrarColunaComTermo(un.TestCase):

#verifica se a função filtrar_coluna_com_termo funciona corretamente
def test_sucesso_filtragem_texto(self):
    df = pd.DataFrame({'coluna a ser filtrada': ['tópico 1', 'tópico 2', 'tópico 3']})
    resultado = dtc.filtrar_coluna_com_termo(df, 'coluna a ser filtrada', 'tópico 1')
    self.assertTrue(isinstance(resultado, pd.DataFrame))
    self.assertEqual(len(resultado), 1)

#verificar se a função filtrar_coluna_com_termo lida corretamente com a filtragem de números em um DataFrame.
def test_sucesso_filtragem_numero(self):
    df = pd.DataFrame({'Número': [1, 2, 3, 4, 5]})
    resultado = dtc.filtrar_coluna_com_termo(df, 'Número', 2)
    self.assertTrue(isinstance(resultado, pd.DataFrame))
    self.assertEqual(len(resultado), 1)

def test_tipo_de_entrada_invalido(self):
    with self.assertRaises(TypeError):
        dtc.filtrar_coluna_com_termo("Não é um DataFrame válido", 'Texto', 'Python')

def test_coluna_inexistente(self):
    df = pd.DataFrame({'Texto': ['Python é ótimo', 'Java é bom', 'C++ é poderoso']})
    with self.assertRaises(KeyError):
        dtc.filtrar_coluna_com_termo(df, 'ColunaInexistente', 'Python')

def test_excecao(self):
    with self.assertRaises(TypeError):
        dtc.filtrar_coluna_com_termo(pd.DataFrame({'Texto': ['Python é ótimo', 'Java é bom', 'C++ é poderoso']}), 'Texto', 42)

def test_case_insensitivo(self):
    df = pd.DataFrame({'Texto': ['Python é ótimo', 'java é bom', 'C++ é poderoso']})
    resultado = dtc.filtrar_coluna_com_termo(df, 'Texto', 'python', case_insensitive=True)
    self.assertTrue(isinstance(resultado, pd.DataFrame))
    self.assertEqual(len(resultado), 2)

#class TestePlotarColunasEmpilhadas(un.TestCase):

# Test case 1: Test with valid input
df = pd.DataFrame({'x': ['A', 'A', 'B', 'B'], 'y': [1, 2, 3, 4], 'z': ['P', 'Q', 'P', 'Q']})
import pandas as pd
import graficos as grf

# Test case 1: Test with valid input
df = pd.DataFrame({'x': ['A', 'A', 'B', 'B'], 'y': [1, 2, 3, 4], 'z': ['P', 'Q', 'P', 'Q']})
grf.plotar_colunas_empilhadas(df, 'z', 'x', 'y', 'Test Case 1')

# Test case 2: Test with invalid DataFrame
df = 'invalid_df'
try:
    grf.plotar_colunas_empilhadas(df, 'z', 'x', 'y', 'Test Case 2')
except TypeError as e:
    print(e)

# Test case 3: Test with missing columns
df = pd.DataFrame({'x': ['A', 'A', 'B', 'B'], 'y': [1, 2, 3, 4], 'z': ['P', 'Q', 'P', 'Q']})
try:
    grf.plotar_colunas_empilhadas(df, 'missing_col', 'x', 'y', 'Test Case 3')
except ValueError as e:
    print(e)