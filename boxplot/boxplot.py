""" Módulo para a geração de gráficos de boxplot e tratamento de outliers.
Nesse módulo, são definidas as funções para a geração de gráficos de boxplot e tratamento de outliers e seus testcases.
Importante dizer que, apesar de em parte utilizar funções quase que já existentes, os pequenos detalhes que estão automatizados aqui fizeram bastante diferença no tempo de desenvolvimento da análise individual. 
Por isso a importância e existência do módulo
"""
import pandas as pd
import datacleaning as dtc
import matplotlib.pyplot as plt
import unittest as un

def boxplot_coluna_de_dataframe(df, coluna):
    """
    Cria um gráfico de boxplot para uma coluna específica de um DataFrame, sem nenhum tratamento diferente.

    Parameters:
        df (pandas.DataFrame): O DataFrame contendo os dados.
        coluna: O nome da coluna a ser visualizada no gráfico de boxplot.

    Returns:
        None
    """    
    try:   
        if not isinstance(df, pd.DataFrame):
            raise TypeError
        
        if coluna not in df.columns:
            raise KeyError
        
        if df[coluna].isnull().values.any():
            raise ValueError
        
        if df[coluna].dtype == 'object':
            raise ValueError
        
        if df.empty:
            return None
        
        data = df[coluna]

        plt.boxplot([data])

        plt.show()
        
    except TypeError:
        if not isinstance(df, pd.DataFrame):
            raise TypeError('O argumento df deve ser um DataFrame.')
    except KeyError:
        if coluna not in df.columns:
            raise KeyError('A coluna especificada não existe no DataFrame.')
    except ValueError:
        if df[coluna].isnull().values.any():
            raise ValueError('A coluna especificada contém valores nulos.')
        if df[coluna].dtype == 'object':
            raise ValueError('A coluna especificada contém valores não numéricos.')
        
def boxplot_sem_outliers(df, coluna, titulo='Boxplot Sem Outliers'):
    """Gera um boxplot sem seus outliers a partir de um DataFrame.

    Parameters:
    df (DataFrame): O DataFrame contendo os dados a serem plotados.
    coluna: O nome da coluna no DataFrame a ser usado para criar o gráfico de caixa.
    titulo (str): O título a ser exibido no gráfico (OPCIONAL).

    Returns:
    fig (Figure): A figura do gráfico de caixa sem outliers.
    ax (Axes): O eixo do gráfico de caixa.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise TypeError
        
        if coluna not in df.columns:
            raise KeyError
        
        if df[coluna].isnull().values.any():
            raise ValueError
        
        if df[coluna].dtype == 'object':
            raise ValueError
        
        if df.empty:
            return None
        
        data = df[coluna]
        
        fig, ax = plt.subplots()
        
        ax.set_title(titulo)  
        ax.boxplot(data, showfliers=False)
        
        plt.show() 

        return fig, ax
    except TypeError:
        if not isinstance(df, pd.DataFrame):
            raise TypeError('O argumento df deve ser um DataFrame.')
        if coluna not in df.columns:
            raise KeyError('A coluna especificada não existe no DataFrame.')
    except KeyError:
        if coluna not in df.columns:
            raise KeyError('A coluna especificada não existe no DataFrame.')
    except ValueError:
        if df[coluna].isnull().values.any():
            raise ValueError('A coluna especificada contém valores nulos.')
        if df[coluna].dtype == 'object':
            raise ValueError('A coluna especificada contém valores não numéricos.')
        
def excluir_outliers(df, coluna_numerica):
    """
    Exclui as linhas com valores discrepantes (outliers) encontrados em uma dada coluna do dataframe.

    Parameters:
    df (DataFrame): O DataFrame contendo os dados a serem analisados.
    coluna_numerica: O nome da coluna de valores a ser filtrada.

    Returns:
    df_sem_outliers (DataFrame): Um novo DataFrame que contém apenas as observações que não são outliers na coluna especificada.

    """
    
    try:
        
        if not isinstance(df, pd.DataFrame):
            raise TypeError
        
        if df.empty:
            return None

        if coluna_numerica not in df.columns:
            raise KeyError
        
        if df[coluna_numerica].isnull().values.all():
            return None

        if df[coluna_numerica].dtype == 'object':
            raise ValueError
        
        if df[coluna_numerica].isnull().values.any():
            raise ValueError
        
        data = df[coluna_numerica]
        
        boxplot = plt.boxplot(data)
        
        whiskers = [item.get_ydata() for item in boxplot['whiskers']]
        limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]
        
        df_sem_outliers = df[(df[coluna_numerica] > limite_inferior) &
                        (df[coluna_numerica] < limite_superior)]

        return df_sem_outliers
    except TypeError:
        if not isinstance(df, pd.DataFrame):
            raise TypeError('O argumento df deve ser um DataFrame.')
    except KeyError:
        if coluna_numerica not in df.columns:
            raise KeyError('A coluna especificada não existe no DataFrame.')
    except ValueError:
        if df[coluna_numerica].isna().values.any():
            raise ValueError('A coluna especificada contém valores inválidos (NaN).')
        if df[coluna_numerica].dtype == 'object':
            raise ValueError('A coluna especificada contém valores não numéricos.')
    
### TESTES UNITÁRIOS ###
class TesteBoxPlotColunaDeDataFrame(un.TestCase):
    def test_valid_dataframe_and_column(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        coluna = 'col1'

        boxplot_coluna_de_dataframe(df, coluna)
        
    # Teste com o dataframe contendo uma linha
    def test_one_row_dataframe(self):
        df = pd.DataFrame({'col1': [1]})
        coluna = 'col1'

        boxplot_coluna_de_dataframe(df, coluna)
        
    # Teste com o dtaframe cotendo uma coluna de múltiplas linhas
    def test_one_column_dataframe(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        coluna = 'col1'

        boxplot_coluna_de_dataframe(df, coluna)
        
    # Teste com coluna inexistente
    def test_non_existent_column(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        coluna = 'col2'
    
        with self.assertRaises(Exception):
            boxplot_coluna_de_dataframe(df, coluna)

    # Teste com coluna contendo valores nulos
    def test_column_with_null_values(self):
        df = pd.DataFrame({'col1': [1, 2, None, 4, 5]})
        coluna = 'col1'
    
        with self.assertRaises(Exception):
            boxplot_coluna_de_dataframe(df, coluna)
            
    # Teste com coluna contendo valores não numéricos
    def test_column_with_non_numeric_values(self):
        df = pd.DataFrame({'col1': [1, 2, 'a', 4, 5]})
        coluna = 'col1'
    
        with self.assertRaises(Exception):
            boxplot_coluna_de_dataframe(df, coluna)

class TesteBoxPlotSemOutliers(un.TestCase):
    def test_valid_dataframe_and_column(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        coluna = 'col1'

        boxplot_sem_outliers(df, coluna)
        
    # Teste com o dataframe contendo uma linha
    def test_one_row_dataframe(self):
        df = pd.DataFrame({'col1': [1]})
        coluna = 'col1'

        boxplot_sem_outliers(df, coluna)
        
    # Teste com o dtaframe cotendo uma coluna de múltiplas linhas
    def test_one_column_dataframe(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        coluna = 'col1'

        boxplot_sem_outliers(df, coluna)
        
    # Teste com coluna inexistente
    def test_non_existent_column(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        coluna = 'col2'
    
        with self.assertRaises(Exception):
            boxplot_sem_outliers(df, coluna)

    # Teste com coluna contendo valores nulos
    def test_column_with_null_values(self):
        df = pd.DataFrame({'col1': [1, 2, None, 4, 5]})
        coluna = 'col1'
    
        with self.assertRaises(Exception):
            boxplot_sem_outliers(df, coluna)
            
    # Teste com coluna contendo valores não numéricos
    def test_column_with_non_numeric_values(self):
        df = pd.DataFrame({'col1': [1, 2, 'a', 4, 5]})
        coluna = 'col1'
    
        with self.assertRaises(Exception):
            boxplot_sem_outliers(df, coluna)

class TesteExcluirOutliers(un.TestCase):
    
    # Teste com dataframe válido e coluna válida
    def test_valid_dataframe_valid_column(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    
        result = excluir_outliers(df, 'col1')
    
        assert isinstance(result, pd.DataFrame)
    
        assert result['col1'].max() <= df['col1'].quantile(0.75) + 1.5 * (df['col1'].quantile(0.75) - df['col1'].quantile(0.25))
        assert result['col1'].min() >= df['col1'].quantile(0.25) - 1.5 * (df['col1'].quantile(0.75) - df['col1'].quantile(0.25))
       
    # Teste com dataframe contendo uma linha 
    def test_valid_dataframe_all_null_values(self):
        df = pd.DataFrame({'col1': [None, None, None]})
    
        result = excluir_outliers(df, 'col1')
    
        assert result is None
     
    # Teste com dataframe contendo uma linha   
    def test_empty_dataframe(self):
        df = pd.DataFrame()
    
        result = excluir_outliers(df, 'col1')
    
        assert result is None
    
    # Teste com dataframe contendo uma coluna de múltiplas linhas  
    def test_non_dataframe_object(self):
        df = 'not a DataFrame'
    
        with self.assertRaises(TypeError):
            excluir_outliers(df, 'col1')
    
    # Teste com dataframe contendo uma coluna de múltiplas linhas     
    def test_invalid_column_name(self):
        df = pd.DataFrame({'col1': [1, 2, 3]})
    
        with self.assertRaises(KeyError):
            excluir_outliers(df, 'col2')
    
    # Teste com dataframe contendo uma coluna de múltiplas linhas       
    def test_non_numeric_column(self):
        df = pd.DataFrame({'col1': ['a', 'b', 'c']})
    
        with self.assertRaises(ValueError):
            excluir_outliers(df, 'col1')    
if __name__ == "__main__":
    un.main()
    
    
   