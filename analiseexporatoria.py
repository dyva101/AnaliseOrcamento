import pandas as pd 
import datacleaning as dtc

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

print(df.head())
print(df.tail())

print(df.columns.values)

df_final = dtc.coletar_colunas(df, ["EXERCÍCIO", "NOME FUNÇÃO", 'NOME SUBFUNÇÃO','ORÇAMENTO REALIZADO (R$)'])


