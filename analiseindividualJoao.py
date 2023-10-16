"""Análise Individual - João Otávio Siqueira de Brito
Análise de dados de gastos do governo federal com educação, no período de 2014 a 2023.
""" 

import matplotlib.pyplot as plt
import pandas as pd 
import graficos as graf
import main as ae
import datacleaning as dt 
import boxplot as bx 

#para minha análise, vou começar teorizando que em anos eleitorais os gastos em geral foram maiores, nosso grupo coletou dados do governo do portal de
#transparência, com gastos do governo nos anos de 2014 a 2023
#nesse caso, os anos eleitorais foram: 2014, 2018 e 2022, ou seja, nesses anos os gastos devem ser superiores aos demais gastos


df_sem_outliers = pd.read_csv('data/data_sem_outliers.csv')
graf.plotar_histograma_com_filtro(ae.df_final, 'ORÇAMENTO REALIZADO (R$)', 'EXERCÍCIO', title="Histograma de gastos em educação")
graf.plotar_histograma_com_filtro(ae.df_sem_outliers, 'ORÇAMENTO REALIZADO (R$)', title="Histograma de gastos em educação")

bx.boxplot_coluna_de_dataframe(ae.df_final, 'ORÇAMENTO REALIZADO (R$)')
bx.boxplot_sem_outliers(ae.df_final, 'ORÇAMENTO REALIZADO (R$)', 'sem_outliers')


#pela análise exemplificada nos códigos acima, temos "df_sem_outliers" mostrando o orçamento realizado ao longo dos anos de uma maneira mais normalizada, sem considerar os altos
#investimentos, pois no primeiro boxplot que é apresentado, podemos analisar, mesmo que seja dando um zoom muito longo, que é mais um motivo de eu desconsiderar outlier dessa análise em específico, 
#temos também que grande parte dos grandes investimentos em educação estão concentrados em um pequeno intervalo, o que indica que não são uma parte tão significativa que corrompa a análise geral, 
# portanto, para facilitar a visualização, e visto que tais outliers não corrompem a análise geral, vou desconsiderá-los 


# minha segunda hipótese, é de que, no período pandêmico(2020 e 2021) os investimentos em educação foram super baixos, visto que o mundo estava passando por um 
# completo caos na saúde, no qual grande parte dos investimentos são direcionados foram direcionados ao setor da saúde, a tecnologia para produção de vacinas 
# mais rápidas(no caso para a compra de vacinas que foram produzidas) e meio que a educação foi mais "deixada de lado" nessa época

#gráfico de colunas que mostra como diminuiu na pandemia

df_final_colunas = pd.DataFrame({'EXERCÍCIO': df_final['EXERCÍCIO'], 'NOME SUBFUNÇÃO': df_final['NOME SUBFUNÇÃO'], 'ORÇAMENTO REALIZADO (R$)': df_final['ORÇAMENTO REALIZADO (R$)']})

df_final_colunas.groupby(['EXERCÍCIO', 'NOME SUBFUNÇÃO']).sum().unstack().plot(kind='line')

plt.xlabel('Anos')
plt.ylabel('Gastos em educação')
plt.title('Gastos em educação por ano')

plt.legend()
plt.show()


#através dos gráfico apresentado, pode-se ver que os anos que se seguem tendem a apenas diminuir os investimenotos em educação, mesmo que aos poucos no nosso intervalo, e que em 2020 foi um dos menores investimentos educacionais , o que confirma a nossa hipótese 


#analisar qual área foi mais investida ao longo do tempo no nosso intervalo

df_final = graf.substituir_coluna_por_lista_especificada(ae.df_final, "NOME SUBFUNÇÃO", 'OUTROS', ['Outros encargos especiais',
                                                                                                              'Difusão do conhecimento científico e tecnológico',
                                                                                                              'Difusão do conhecimento científico e tecnológico',
                                                                                                              'Transferências para a educação básica',
                                                                                                              'Comunicação social',
                                                                                                              'Educação especial',
                                                                                                              'Educação de jovens e adultos',
                                                                                                              'Desenvolvimento científico',
                                                                                                              'Educação infantil',
                                                                                                              'Alimentação e nutrição',
                                                                                                              'Administração financeira',
                                                                                                              'Serviços financeiros',
                                                                                                              'Suporte profilático e terapêutico',
                                                                                                              'Outras transferências',
                                                                                                            ])
#gráfico de colunas que mostra como diminuiu na pandemia

df_final_colunas = pd.DataFrame({'EXERCÍCIO': df_final['EXERCÍCIO'], 'NOME SUBFUNÇÃO': df_final['NOME SUBFUNÇÃO'], 'ORÇAMENTO REALIZADO (R$)': df_final['ORÇAMENTO REALIZADO (R$)']})

df_final_colunas.groupby(['EXERCÍCIO', 'NOME SUBFUNÇÃO']).sum().unstack().plot(kind='line')

plt.xlabel('Anos')
plt.ylabel('Gastos em educação')
plt.title('Gastos em educação por ano')

plt.legend()

plt.show()

#com o gráfico que temos nessa situação apresentada, vemos que a  área mais investida ao longo dos anos, foi a de ensino superior, que cresceu em parte de 2014 a 2015, e a partir daí se manteve 
#constante, ou com poucas irregularidades até o período de pandemia, que teve uma queda brusca, e até o período de 2022/parte de 2023, que estava voltando aos poucos para como era antes. E os demais 
#seguiram a mesma tendência, exceto somente a área de administração geral e a de formação de recursos humanos. Por fim para encerrar esse tópico, veja que temos uma linha com o termo "outros", essa expressão 
#foi usada para juntar todas as outras categorias que eram mais pequenas, e que só poluiriam a visualização do gráfico, pois ambas seguem a mesma ideia de decrescerem na pandemia, apesar de não terem um 
#comportamento constante ao longo de 2014 a 2019, mas o comportamento nos extremos é definido com a mesma ideia, e ainda respondem a pergunta da mesma forma, que é a de que o ensino superior foi a área mais investida
#ao longo dos anos(2014-2023) analisados.

#hipótese, a tendência dos investimentos em educação ao longo dos anos é de sempre aumentar, para satisfazer as demandas(fazer um gráfico de linhas com os gastos em educação no Brasil e comparar importando outro gráfico)

df_final_educacao_geral = dt.coletar_colunas(ae.df_final, ['EXERCÍCIO', 'ORÇAMENTO REALIZADO (R$)', 'NOME FUNÇÃO'])
df_final_educacao_geral.groupby('EXERCÍCIO')['ORÇAMENTO REALIZADO (R$)'].sum().plot(kind='line')
df_final_educacao_geral.groupby('EXERCÍCIO')['ORÇAMENTO REALIZADO (R$)'].sum().plot(kind='bar')

plt.xlabel('Anos')
plt.ylabel('Gastos em educação')
plt.title('Gastos em educação por ano')

plt.legend()

plt.show()

#com o nosso gráfico de linhas, agora temos pela sua visuaização, que ao longo de 2014 a 2023, os investimentos no greal em áreas de educação estão cada vez mais decrescendo, fato que se complementa com o quesito pandemia, qua ajudou nesse grande impasse, logo a hipótese formulada
#se encontra errada, pela visualização direta do gráfico de linhas e de barras apresentado.


#GRÁFICO HISTOGRAMA 2017
graf.plotar_histograma_com_filtro(df_sem_outliers, 'ORÇAMENTO REALIZADO (R$)', 'EXERCÍCIO', 2017, title="Histograma de gastos em educação em 2017")
graf.plotar_histograma_com_filtro(df_sem_outliers, 'ORÇAMENTO REALIZADO (R$)', 'EXERCÍCIO', 2016, title="Histograma de gastos em educação em 2017")
graf.plotar_histograma_com_filtro(df_sem_outliers, 'ORÇAMENTO REALIZADO (R$)', 'EXERCÍCIO', 2015, title="Histograma de gastos em educação em 2017")
graf.plotar_histograma_com_filtro(df_sem_outliers, 'ORÇAMENTO REALIZADO (R$)', 'EXERCÍCIO', 2014, title="Histograma de gastos em educação em 2017")
