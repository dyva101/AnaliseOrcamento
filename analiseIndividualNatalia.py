import boxplot as bx
import graficos as grf
import datacleaning as dtc 
import analiseexporatoria as ae
import pandas as pd
import matplotlib.pyplot as mp

# Analisando os outliers
bx.boxplot_coluna_de_dataframe(ae.df_final,'ORÇAMENTO REALIZADO (R$)')

# Noção da quantidade de outliers
numero_de_dados = ae.df_final.shape[0]

print(f"O DataFrame contém {numero_de_dados} elementos.")

numero_de_dados = ae.df_sem_outliers.shape[0]

print(f"O DataFrame sem outliers contém {numero_de_dados} elementos.")

# É perceptível que, na visualização do box plot do DataFrame (limpo e organizado com os dados de orçamento do governo na educação),
# os outliers são consideravelmente poucos. Além disso, é notório um certo padrão
# de outliers a cada ano, e que os mesmos, em sua maioria, estão acima da média de gastos. Isso significa que todo ano o governo
# sempre vai fazer investimentos consideráveis em comparação com a maioria dos investimentos. O que pode indicar que esses
# orçamentos são "obrigatórios" a cada ano.

# São poucos outliers baixos, também padronizados a cada ano. Indicando que, independentemente
# de ser um ano de eleição, sempre haverá ações de orçamentos baixos recorrentes em todo ano.

# Portanto, devido a essa padronização de outliers a cada ano, independentemente de ser um ano de eleição ou não,
# podemos ignorá-los e continuar analisando os orçamentos realizados na educação pelo governo a cada ano, 
# para tirar conclusões. Não é apropriado analisar o orçamento realizado em educação do governo para 
# o ano de 2023 neste momento, uma vez que o ano ainda não chegou ao fim.


#Análise sem outliers

# Definindo as quatro palavras-chave em uma lista
palavras_chave = ['Educação', 'educação', 'Ensino', 'ensino']

# Criando um filtro para selecionar as linhas que contêm as palavras-chave desejadas
filtro = ae.df_sem_outliers['NOME SUBFUNÇÃO'].str.contains('|'.join(palavras_chave), case=False, na=False)

# Criando um novo DataFrame contendo apenas as linhas que atendem ao filtro
novo_df = ae.df_sem_outliers[filtro].reset_index(drop=True)
grf.plotar_colunas_empilhadas(novo_df, 'NOME SUBFUNÇÃO', 'EXERCÍCIO', 'ORÇAMENTO REALIZADO (R$)', 'Orçamento anual')

#É notório que nos anos 2014, 2015, 2020 e 2021 a soma dos orçamentos destinados à educação foi maior 
# do que em outros anos. Logo, não se pode concluir que em anos de eleição (2014, 2018, 2022) os investimentos em educação
#são maiores. Bem como, fica evidente no gráfico de colunas, que nos anos 2016, 2017 e 2018 a soma dos orçamentos destinados
# à educação foi menor em relação aos outros anos, indicando que não se pode afirmar que em anos que não são de eleição
#o orçamento destinado à educação são menores.


#Análise de 2017 reforma do ensino médio (pode ser que aumentou o investimo em ens. básico)
#stacked bar com os setores


# , é interessante analisar inicio 2019 e fim 2022 nos principais setores investidos no início e no fim de um mandato. 
#"""
#stacked bar normalizada 
#"""






