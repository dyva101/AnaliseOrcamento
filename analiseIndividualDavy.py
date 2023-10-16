"""Análise Individual - Davy Albert Dutra de Andrade
Análise de dados de gastos do governo federal com educação, no período de 2014 a 2023.
"""
import pandas as pd
import matplotlib.pyplot as plt
from boxplot import boxplot as bx
from datacleaning import datacleaning as dtc
from graficos import graficos as grf

### LIMPEZA E FILTRAGEM DOS DADOS ###

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

df['ORÇAMENTO REALIZADO (R$)'] = df['ORÇAMENTO REALIZADO (R$)'].str.replace(',', '.').astype(float)

df_final = pd.DataFrame()
df_orcamentos_negativos = pd.DataFrame()
df_orcamentos_positivos = pd.DataFrame()
df_final = dtc.coletar_colunas(df, ["EXERCÍCIO", "NOME FUNÇÃO", 'NOME SUBFUNÇÃO','ORÇAMENTO REALIZADO (R$)'])
df_final = dtc.filtrar_coluna_com_termo(df_final, "NOME FUNÇÃO", "educação")

### Boxplot E Estatísticas para análise dos outliers ###

# Plot BoxPlots of the Data
bx.boxplot_coluna_de_dataframe(df_final, 'ORÇAMENTO REALIZADO (R$)')
bx.boxplot_sem_outliers(df_final, 'ORÇAMENTO REALIZADO (R$)', 'sem_outliers')

# Remove the outliers
df_sem_outliers = bx.excluir_outliers(df_final, 'ORÇAMENTO REALIZADO (R$)')

# Print the statistics
print(df_final['ORÇAMENTO REALIZADO (R$)'].describe(include='all'))
print("#"*60, "\n")

print(df_sem_outliers['ORÇAMENTO REALIZADO (R$)'].describe(include='all'))
print("#"*60, "\n")

#Here, we're just been able to see that the outliers are not corrupted data. Instead, they're make, with the rest of the registers of
#expenditure, a sample with a distribution more close to a exponential distribution than a normal one. This is in concordance with the
#what we're looking for: the expenditure in education is focused in minor payments, every year. As bigger the payment, less frequent it is.
#Anyway, we can see that the data without the outliers is more close to a normal distribution, which is good for our analysis and avoid that
#big payments that are not related to the focus of our analysis distort the results.

print("#"*100, "\n\n")

### Análise de correlação entre o ano eleitoral e os outros anos ###

# Calculate the mean for the non-election years
orcamentos_anos_nao_eleitorais = []
for ano in [2015, 2016, 2017, 2019, 2020, 2021, 2023]:
    df_final_filtrado = dtc.filtrar_coluna_com_termo(df_sem_outliers, "EXERCÍCIO", ano)
    orcamentos_anos_nao_eleitorais.append(df_final_filtrado["ORÇAMENTO REALIZADO (R$)"].sum())

serie_orcamentos_anos__nao_eleitorais = pd.Series(orcamentos_anos_nao_eleitorais)
print("Year Expenditure for the election years(sem considerar os outliers): ", serie_orcamentos_anos__nao_eleitorais.mean())
print("#"*60, "\n")

# Calculate the mean for the election years
orcamentos_anos_eleitorais = []
for ano in [2014, 2018, 2022]:
    df_final_filtrado = dtc.filtrar_coluna_com_termo(df_sem_outliers, "EXERCÍCIO", ano)
    orcamentos_anos_eleitorais.append(df_final_filtrado["ORÇAMENTO REALIZADO (R$)"].sum())

serie_orcamentos_anos_eleitorais = pd.Series(orcamentos_anos_eleitorais)
print("Year Expenditure for the election years(sem considerar os outliers): ", serie_orcamentos_anos_eleitorais.mean())
print("#"*60, "\n")

#Notice that the difference between the means is not significant, which doesn't necessarily mean that our hypothesis is wrong: it does mean that
#the data provided is not sufficient to prove it right. I support this affirmation with the following: the data is not normalized and we're not
#considering the inflation rate, the different crisis the country has been through, etc. This could be a good starting point for a more in-depth
#analysis. Just to see a little bit of this analysis, following I'll present data for the pandemic years and about the growing of investiments
#in different subfunctions of Education, which already shows how the analysis is more complicated than just comparing the means.

print("#"*100, "\n\n")

### Análise do investimento no período pandêmico (2019-2021) ###

# Calculate the mean for the pre-pandemic years
orcamentos_anos_pre_pandemia = []
for ano in [2014, 2015, 2016, 2017, 2018, 2019]:
    df_final_filtrado = dtc.filtrar_coluna_com_termo(df_sem_outliers, "EXERCÍCIO", ano)
    orcamentos_anos_pre_pandemia.append(df_final_filtrado["ORÇAMENTO REALIZADO (R$)"].sum())

serie_orcamentos_anos_pre_pandemia = pd.Series(orcamentos_anos_pre_pandemia)
print("Year Expenditure for the pre-pandemic years (sem considerar os outliers): ", serie_orcamentos_anos_pre_pandemia.mean())
print("#"*60, "\n")

# Calculate the mean for the pandemic years
orcamentos_anos_pos_pandemia = []
for ano in [2020, 2021]:
    df_final_filtrado = dtc.filtrar_coluna_com_termo(df_sem_outliers, "EXERCÍCIO", ano)
    orcamentos_anos_pos_pandemia.append(df_final_filtrado["ORÇAMENTO REALIZADO (R$)"].sum())

serie_orcamentos_anos_pos_pandemia = pd.Series(orcamentos_anos_pos_pandemia)
print("Year Expenditure for the pandemic years (sem considerar os outliers): ", serie_orcamentos_anos_pos_pandemia.mean())
print("#"*60, "\n")

# Calculate the mean for the pre-pandemic years (with outliers)
orcamentos_anos_pre_pandemia = []
for ano in [2014, 2015, 2016, 2017, 2018, 2019]:
    df_final_filtrado = dtc.filtrar_coluna_com_termo(df_final, "EXERCÍCIO", ano)
    orcamentos_anos_pre_pandemia.append(df_final_filtrado["ORÇAMENTO REALIZADO (R$)"].sum())

serie_orcamentos_anos_pre_pandemia = pd.Series(orcamentos_anos_pre_pandemia)
print("Year Expenditure for the pre-pandemic years (considerar os outliers): ", serie_orcamentos_anos_pre_pandemia.mean())
print("#"*60, "\n")

# Calculate the mean for the pandemic years (with outliers)
orcamentos_anos_pos_pandemia = []
for ano in [2020, 2021]:
    df_final_filtrado = dtc.filtrar_coluna_com_termo(df_final, "EXERCÍCIO", ano)
    orcamentos_anos_pos_pandemia.append(df_final_filtrado["ORÇAMENTO REALIZADO (R$)"].sum())

serie_orcamentos_anos_pos_pandemia = pd.Series(orcamentos_anos_pos_pandemia)
print("Year Expenditure for the pandemic years (considerar os outliers): ", serie_orcamentos_anos_pos_pandemia.mean())
print("#"*60, "\n")
    
# Hypothesis: the expenditure in education diminished in the pandemic years, for all sectors of education, due to the economic crisis

# Plot a stacked bar chart of the 10 year period 2014-2023
df_final_com_colunas_substituidas = grf.substituir_coluna_por_lista_especificada(df_final, "NOME SUBFUNÇÃO", 'OUTROS', ['Outros encargos especiais',
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
plt.clf()
grf.plotar_colunas(df_final_com_colunas_substituidas, "EXERCÍCIO", "ORÇAMENTO REALIZADO (R$)", "Orçamento Anual & Gastos por função")

#We can see that the hypothesis is partially true: in the pandemic years, we had lower mean expenditure in education and lower total expenditure. 
#But it wasn't so abrupt as we could expect. That's where the hypothesis is wrong: the expenditure in education had to increase
#so the schools could adapt to the new reality of online classes, for example. That says that, in this sector, the government admistrated
#the crisis well, and the expenditure in education was not so affected by the economic crisis.

print("#"*100, "\n\n")

### Análise da distribuição dos investimentos em cada Ano ###

for ano in [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]:
    grf.plotar_histograma_com_filtro(df_sem_outliers, "ORÇAMENTO REALIZADO (R$)", 'EXERCÍCIO', ano, f'Gastos em {ano}')

#Here, we confirm that every year, the expenditure has followed a exponential distribution, with the majority of the expenditure being in minor
#payments. 

print("END OF THE ANALYSIS")