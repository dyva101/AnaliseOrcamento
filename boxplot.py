import pandas as pd
import datacleaning as dtc
import matplotlib.pyplot as plt 

def boxplot_coluna_de_dataframe(df, coluna):
    """
    Cria um gráfico de boxplot para uma coluna específica de um DataFrame.

    Parameters:
        df (pandas.DataFrame): O DataFrame contendo os dados.
        coluna (str): O nome da coluna a ser visualizada no gráfico de boxplot.

    Returns:
        None
    """
    data = df[coluna]

    plt.boxplot([data])

    plt.show()   


def boxplot_sem_outliers(df, coluna, titulo):
    """
    Gera um gráfico de caixa sem outliers a partir de um DataFrame.

    Parameters:
    df (DataFrame): O DataFrame contendo os dados a serem plotados.
    coluna (str): O nome da coluna no DataFrame a ser usado para criar o gráfico de caixa.
    titulo (str): O título a ser exibido no gráfico.

    Retorna:
    fig (Figure): A figura do gráfico de caixa sem outliers.
    ax (Axes): O eixo do gráfico de caixa.
    """
    data = df[coluna]
    fig, ax = plt.subplots()
    ax.set_title(titulo)  
    ax.boxplot(data, showfliers=False)  # Oculte os outliers no gráfico de caixa
    plt.show() 

    return fig, ax
    
def separar_outliers_colunas_numericas(df, coluna_numerica):
    """
    Separa valores discrepantes (outliers) de uma coluna numérica em um DataFrame.

    Parameters:
    df (DataFrame): O DataFrame contendo os dados a serem analisados.
    coluna_numerica (str): O nome da coluna numérica a ser analisada quanto a outliers.

    Retorna:
    df_sem_outliers (DataFrame): Um novo DataFrame que contém apenas as observações que não são outliers na coluna especificada.

    """
    data = df[coluna_numerica]
    boxplot = plt.boxplot(data)
    whiskers = [item.get_ydata() for item in boxplot['whiskers']]
    limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]
    df_sem_outliers = df[(df[coluna_numerica] >= limite_inferior) &
    (df[coluna_numerica] <= limite_superior)]

    return df_sem_outliers 

   