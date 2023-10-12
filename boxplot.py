import pandas as pd
import datacleaning as dtc
import matplotlib.pyplot as plt 

def boxplot_coluna_de_dataframe(df, coluna):
    data = df[coluna]

    plt.boxplot([data])

    plt.show()

def separar_outliers_colunas_numericas(df, coluna_numerica):
    
    data = df[coluna_numerica]
    boxplot = plt.boxplot(data)
    whiskers = [item.get_ydata() for item in boxplot['whiskers']]
    limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]

    df_com_outliers = df[(df[coluna_numerica] < limite_inferior) | (df[coluna_numerica] > limite_superior)]

    return df_com_outliers

def criar_dataframe_sem_outliers(df, coluna_numerica):
    data = df[coluna_numerica]
    boxplot = plt.boxplot(data)
    whiskers = [item.get_ydata() for item in boxplot['whiskers']]
    limite_inferior, limite_superior = whiskers[0][0], whiskers[1][0]
    df_sem_outliers = df[
    (df[coluna_numerica] >= limite_inferior) &
    (df[coluna_numerica] <= limite_superior)
    ]

    return df_sem_outliers 