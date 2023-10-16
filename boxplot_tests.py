import unittest as un
import pandas as pd
import datacleaning as dtc
import boxplot as bx 
import graficos as grf

class TesteBoxPlotColunaDeDataFrame(un.TestCase):
    def test_valid_dataframe_and_column(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        coluna = 'col1'

        bx.boxplot_coluna_de_dataframe(df, coluna)
        
    # Test with a DataFrame containing only one row.
    def test_one_row_dataframe(self):
        df = pd.DataFrame({'col1': [1]})
        coluna = 'col1'

        bx.boxplot_coluna_de_dataframe(df, coluna)
        
    # Test with a DataFrame containing only one column.
    def test_one_column_dataframe(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        coluna = 'col1'

        bx.boxplot_coluna_de_dataframe(df, coluna)
        
    # Test with a non-existent column name.
    def test_non_existent_column(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
        coluna = 'col2'
    
        with un.pytest.raises(Exception):
            bx.boxplot_coluna_de_dataframe(df, coluna)

    # Test with a column containing null values.
    def test_column_with_null_values(self):
        df = pd.DataFrame({'col1': [1, 2, None, 4, 5]})
        coluna = 'col1'
    
        with un.pytest.raises(Exception):
            bx.boxplot_coluna_de_dataframe(df, coluna)
            
    # Test with a column containing non-numeric values.
    def test_column_with_non_numeric_values(self):
        df = pd.DataFrame({'col1': [1, 2, 'a', 4, 5]})
        coluna = 'col1'
    
        with un.pytest.raises(Exception):
            bx.boxplot_coluna_de_dataframe(df, coluna)