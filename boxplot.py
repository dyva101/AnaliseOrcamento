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
    data = df[coluna]
    fig, ax = plt.subplots()
    ax.set_title(titulo)  # Defina o título passado como argumento
    ax.boxplot(data, showfliers=False)  # Oculte os outliers no gráfico de caixa
    plt.show() 
    return fig, ax


def separar_outliers_colunas_numericas(df, coluna_numerica):
    
    data = df[coluna_numerica]
    boxplot = plt.boxplot(data)
    whiskers = [item.get_ydata() for item in boxplot['whiskers']]
    limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]
   # df_sem_outliers = df[(df[coluna_numerica] >= limite_inferior) &
   #                      (df[coluna_numerica] <= limite_superior)]

   # return df_sem_outliers 

   