import pandas as pd 
import datacleaning as dtc
import boxplot as bx 


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

df_sem_outliers = bx.criar_dataframe_sem_outliers(df_final, 'ORÇAMENTO REALIZADO (R$)')

outliers = bx.separar_outliers_colunas_numericas(df, 'ORÇAMENTO REALIZADO (R$)')

#arquivo csv limpo
df_sem_outliers.to_csv('data/data_sem_outliers.csv', index="false")

# Ler o arquivo CSV para um DataFrame
dff = pd.read_csv('data/data_sem_outliers.csv')

# Salvar o DataFrame em um arquivo Excel
dff.to_excel('data/arquivolimpo.xlsx', index="false") 