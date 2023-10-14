import pandas as pd 
import datacleaning as dtc
import boxplot as bx
import graficos as grf

df1 = pd.read_csv('data/2014_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')
df2 = pd.read_csv('data/2015_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')
df3 = pd.read_csv('data/2016_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')
df4 = pd.read_csv('data/2017_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')
df5 = pd.read_csv('data/2018_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')
df6 = pd.read_csv('data/2019_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')
df7 = pd.read_csv('data/2020_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')
df8 = pd.read_csv('data/2021_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')
df9 = pd.read_csv('data/2022_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')
df10 = pd.read_csv('data/2023_OrcamentoDespesa.csv', encoding='windows-1252', delimiter=';')

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=0)

df.reset_index(drop=True, inplace=True)

#conversão dos valores na coluna de orçamentos para float
df['ORÇAMENTO REALIZADO (R$)'] = df['ORÇAMENTO REALIZADO (R$)'].str.replace(',', '.').astype(float)

#limpeza dos dados
df_final = pd.DataFrame()
df_orcamentos_negativos = pd.DataFrame()
df_orcamentos_positivos = pd.DataFrame()

df_final = dtc.coletar_colunas(df, ["EXERCÍCIO", "NOME FUNÇÃO", 'NOME SUBFUNÇÃO','ORÇAMENTO REALIZADO (R$)'])
df_final = dtc.filtrar_coluna_com_termo(df_final, "NOME FUNÇÃO", "educação")
df_orcamentos_positivos = dtc.filtrar_colunas_numericas(df_final,"ORÇAMENTO REALIZADO (R$)", 1)
df_orcamentos_negativos = dtc.filtrar_colunas_numericas(df_final,"ORÇAMENTO REALIZADO (R$)", 0)
dtc.valores_invalidos(df_final)#TODO: definir o que são valores inválidos

bx.boxplot_coluna_de_dataframe(df_final, 'ORÇAMENTO REALIZADO (R$)')
bx.boxplot_sem_outliers(df_final, 'ORÇAMENTO REALIZADO (R$)', 'sem_outliers')

df_sem_outliers = bx.excluir_outliers(df_final, 'ORÇAMENTO REALIZADO (R$)')

#arquivo csv limpo
df_sem_outliers.to_csv('data/data_sem_outliers.csv', index="false")

#Ler o arquivo CSV para um DataFrame
dff = pd.read_csv('data/data_sem_outliers.csv')

#Salvar o DataFrame em um arquivo Excel
dff.to_excel('data/arquivolimpo.xlsx', index="false")

#testes com o gráfico.py
df_sem_outliers_com_colunas_substituidas = grf.substituir_coluna_por_lista_especificada(df_sem_outliers, 'NOME SUBFUNÇÃO', 'Outros' , ["Outros encargos especiais",
                                                                                            "Difusão do conhecimento científico e tecnológico",
                                                                                            "Educação infantil",
                                                                                            "Outras transferências",
                                                                                            "Transferências para a educação básica",
                                                                                            "Comunicação social",
                                                                                            "Educação especial",
                                                                                            "Educação de jovens e adultos",
                                                                                            "Desenvolvimento científico",
                                                                                            "Alimentação e nutrição",
                                                                                            "Suporte profilático e terapêutico",
                                                                                            "Administração financeira",
                                                                                            "Serviços financeiros"
                                                                                           ])

grf.plotar_colunas_empilhadas(df_sem_outliers_com_colunas_substituidas, 'NOME SUBFUNÇÃO', 'EXERCÍCIO', 'ORÇAMENTO REALIZADO (R$)', 'Orçamento Anual')

grf.plotar_colunas_empilhadas_normalizado(df_sem_outliers_com_colunas_substituidas, 'NOME SUBFUNÇÃO','EXERCÍCIO', 'ORÇAMENTO REALIZADO (R$)', 'Orçamento Anual')

#grf.plotar_histograma_com_filtro(df_sem_outliers, 'ORÇAMENTO REALIZADO (R$)', 'EXERCÍCIO', 2014, '2014 - gráfico')