import pandas as pd 
from datacleaning import datacleaning as dtc
from boxplot import boxplot as bx
from graficos import graficos as grf

### Exploratory Analysis###

#In this file, we're going to do the exploratory analysis of the data, also generating
#csv and xlsx files with the data cleaned and without outliers, that might be useful
#for the use of the data in other projects. The individual analysis of the data is in
#the file analiseIndividual(NAME).py, where NAME is one of the members of the group.

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
dtc.valores_invalidos(df_final)

bx.boxplot_coluna_de_dataframe(df_final, 'ORÇAMENTO REALIZADO (R$)')
bx.boxplot_sem_outliers(df_final, 'ORÇAMENTO REALIZADO (R$)', 'sem_outliers')

df_sem_outliers = bx.excluir_outliers(df_final, 'ORÇAMENTO REALIZADO (R$)')

#arquivo csv sem outliers
df_sem_outliers.to_csv('data/data_sem_outliers.csv', index="false")

#converter o arquivo csv para xlsx
dff = pd.read_csv('data/data_sem_outliers.csv')
dff.to_excel('data/arquivolimpo.xlsx', index="false")