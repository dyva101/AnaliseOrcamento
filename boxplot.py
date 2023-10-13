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

import matplotlib.pyplot as plt

def boxplot_sem_outliers(data, titulo):
    fig, ax = plt.subplots()
    ax.set_title('titulo')
    ax.boxplot(data, showfliers=False)
    return fig, ax

# Exemplo de uso da função:
meus_dados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
titulo_usuario = "Meu Gráfico de Caixa"
figura, eixo = criar_grafico(meus_dados, titulo_usuario)
plt.show()  # Mostra o gráfico na janela de plotagem





def boxplot_sem_outliers(df, coluna):
    fig4, ax4 = plt.subplots() 
    ax4.set_title('Hide Outlier Points') 
    ax4.boxplot(data, showfliers=False)

#def separar_outliers_colunas_numericas(df, coluna_numerica):
    """
    Separa os outliers de uma coluna numérica de um DataFrame com base em um boxplot.

    Parameters:
        df (pandas.DataFrame): O DataFrame contendo os dados.
        coluna_numerica (str): O nome da coluna numérica que deseja separar os outliers.

    Returns:
        pandas.DataFrame: Um novo DataFrame contendo apenas as linhas que correspondem aos outliers da coluna numérica.
    """
    
    #data = df[coluna_numerica]
    #boxplot = plt.boxplot(data)
    #whiskers = [item.get_ydata() for item in boxplot['whiskers']]
    #limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]

    #df_com_outliers = df[(df[coluna_numerica] < limite_inferior) | (df[coluna_numerica] > limite_superior)]

    #return df_com_outliers
   
#def criar_dataframe_sem_outliers(df, coluna_numerica):
    """
    Cria um novo DataFrame sem os outliers de uma coluna numérica com base em um boxplot.

    Parameters:
        df (pandas.DataFrame): O DataFrame contendo os dados.
        coluna_numerica (str): O nome da coluna numérica da qual deseja remover os outliers.

    Returns:
        pandas.DataFrame: Um novo DataFrame contendo apenas as linhas que não são outliers da coluna numérica.
    """
    
    #data = df[coluna_numerica]
    #boxplot = plt.boxplot(data)
    #whiskers = [item.get_ydata() for item in boxplot['whiskers']]
    #limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]
   # df_sem_outliers = df[(df[coluna_numerica] >= limite_inferior) &
   #                      (df[coluna_numerica] <= limite_superior)]

   # return df_sem_outliers 

   