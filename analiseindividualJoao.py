import matplotlib.pyplot as plt
import pandas as pd 
import graficos as graf
import analiseexporatoria as ae
import datacleaning as dt 
import boxplot as bx 

#para minha análise, vou começar teorizando que em anos eleitorais os gastos em geral foram maiores, nosso grupo coletou dados do governo do portal de
#transparência, com gastos do governo nos anos de 2014 a 2023
#nesse caso, os anos eleitorais foram: 2014, 2018 e 2022, ou seja, nesses anos os gastos devem ser superiores aos demais gastos
df_sem_outliers = pd.read_csv('data/data_sem_outliers.csv')
#graf.plotar_histograma_com_filtro(ae.df_final, 'ORÇAMENTO REALIZADO (R$)', 'EXERCÍCIO', title="Histograma de gastos em educação")
#graf.plotar_histograma_com_filtro(ae.df_sem_outliers, 'ORÇAMENTO REALIZADO (R$)', title="Histograma de gastos em educação")

bx.boxplot_coluna_de_dataframe(ae.df_final, 'ORÇAMENTO REALIZADO (R$)')
bx.boxplot_sem_outliers(ae.df_final, 'ORÇAMENTO REALIZADO (R$)', 'sem_outliers')
#TODO gráfico com outliers(boxplot)[prévia acima]


#pela análise exemplificada nos códigos acima, temos "df_sem_outliers" mostrando o orçamento realizado ao longo dos anos de uma maneira mais normalizada, sem considerar os altos
#investimentos, pois no primeiro boxplot que é apresentado, podemos analisar, mesmo que seja dando um zoom muito longo, que é mais um motivo de eu desconsiderar outlier dessa análise em específico, 
#temos também que grande parte dos grandes investimentos em educação estão concentrados em um pequeno intervalo, o que indica que não são uma parte tão significativa que corrompa a análise geral, 
# portanto, para facilitar a visualização, e visto que tais outliers não corrompem a análise geral, vou desconsiderá-los 

#2na minha analise individual vou desconsiderar os outliers em certos casos(como esse primeiro por exemplo, pois são valores muito fora da escala normal do resto dos valores, 
# o que de certa forma corrompe para a análise geral, grande parte dos outliers são muito altos )


#3 minha segunda hipótese, é de que, no período pandêmico(2020 e 2021) os investimentos em educação foram super baixos, visto que o mundo estava passando por um 
# completo caos na saúde, no qual grande parte dos investimentos são direcionados foram direcionados ao setor da saúde, a tecnologia para produção de vacinas 
# mais rápidas(no caso para a compra de vacinas que foram produzidas) e meio que a educação foi mais "deixada de lado" nessa época

# minha segunda hipótese, é de que, no período pandêmico(2020 e 2021) os investimentos em educação foram super baixos, visto que o mundo estava passando por um 
# completo caos na saúde, no qual grande parte dos investimentos são direcionados foram direcionados ao setor da saúde, a tecnologia para produção de vacinas 
# mais rápidas(no caso para a compra de vacinas que foram produzidas) e meio que a educação foi mais "deixada de lado" nessa época

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



#TODO: análise com outliers, e análise sem outliers (para ver os pequenos investimentos e os grandes investimentos)

#4analisar quais áreas  mais foram investidas ao longo do tempo no nosso intervalo

#TODO: gráfico de linhas para confirmar minhas hipóteses


#5hipótese, a tendência dos investimentos em educação ao longo dos anos é de sempre aumentar, para satisfazer as demandas(fazer um gráfico de linhas com os gastos em educação no Brasil e comparar importando outro gráfico)