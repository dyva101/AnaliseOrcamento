"""Análise Individual - Natália Brandão de Souza
Análise de dados de gastos do governo federal com educação, no período de 2014 a 2023.
""" 
import sys
sys.path.append('..')

import main as ae
import pandas as pd
import matplotlib.pyplot as mp
from boxplot import boxplot as bx
from datacleaning import datacleaning as dtc
from graficos import graficos as grf

# Analisando os outliers
bx.boxplot_coluna_de_dataframe(ae.df_final,'ORÇAMENTO REALIZADO (R$)')

# Noção da quantidade de outliers
numero_de_dados = ae.df_final.shape[0]

print(f"O DataFrame contém {numero_de_dados} elementos.")

numero_de_dados = ae.df_sem_outliers.shape[0]

print(f"O DataFrame sem outliers contém {numero_de_dados} elementos.")

# No boxplot que utilizei, os outliers formam uma concentração na parte superior dos dados, 
# sugerindo que parte dos orçamentos governamentais está acima da média. A concentração dos
# outliers é mais proeminente no início da linha formada pelos pontinhos, indicando que há 
# mais investimentos acima da média, mas sem discrepâncias orçamentárias muito grandes. 
# Apenas alguns outliers se destacam com orçamentos notavelmente maiores em relação à média.
# Essa configuração de outliers se mantém consistente ao longo dos anos. Isso sugere a 
# repetição de outliers ligeiramente acima da média  - investimentos essenciais a cada ano.
# Enquanto para os poucos outliers discrepantes que se destacam com orçamentos significativamente 
# acima da média, mostra que investimentos consideravelmente maiores são feitos com menos
# frequência com um padrão anual constante. Devido à consistência desse padrão ao longo dos anos, é 
# vantajoso considerar a exclusão dos outliers a fim de realizar uma análise mais precisa nos dados.

# Análise sem outliers

# Não é apropriado analisar o orçamento realizado em educação do governo para 
# o ano de 2023 neste momento, uma vez que o ano ainda não chegou ao fim.

ano_a_remover = 2023

# Usando .loc para selecionar todas as linhas onde a coluna 'EXERCÍCIO' é diferente de 2023
ae.df_sem_outliers = ae.df_sem_outliers.loc[ae.df_sem_outliers['EXERCÍCIO'] != ano_a_remover]

# Apesar de já termos filtrados apenas os dados relacionados à educação, optei por conduzir uma análise
# ainda mais profunda, focando especificamente no orçamento governamental direto. Para esclarecer,
# considere por exemplo, os investimentos realizados pelo governo na presença de psicólogos em escolas, 
# também é ligado à saúde, portanto minha análise se concentra exclusivamente em orçamentos mais ligados 
# à educação em si. Logo tópicos ligados a outras áreas foram excluídos, para obter uma compreensão mais 
# precisa dos gastos governamentais na educação.

# Definindo as quatro palavras-chave em uma lista
palavras_chave = ['Educação', 'educação', 'Ensino', 'ensino']

# Criando um filtro para selecionar as linhas que contêm as palavras-chave desejadas
filtro = ae.df_sem_outliers['NOME SUBFUNÇÃO'].str.contains('|'.join(palavras_chave), case=False, na=False)

# Criando um novo DataFrame contendo apenas as linhas que atendem ao filtro
novo_df = ae.df_sem_outliers[filtro].reset_index(drop=True)
grf.plotar_colunas(novo_df, 'EXERCÍCIO', 'ORÇAMENTO REALIZADO (R$)', 'Orçamento anual')

# É notório que nos anos 2014, 2015, 2020 e 2021 a soma dos orçamentos destinados à educação foi maior 
# do que em outros anos. Logo, não se pode concluir ,nesse intervalo, que em anos de eleição 
# (2014, 2018, 2022) os investimentos em educação são maiores. Bem como, fica evidente no gráfico de 
# colunas, que nos anos 2016, 2017 e 2018 a soma dos orçamentos destinados à educação foi menor em 
# relação aos outros anos, indicando que não se pode afirmar, nesse intervalo, que em anos que não são
# de eleição o orçamento destinado à educação são menores. Todavia, é interessante anlisar mandato
# coniderando também certos acontecimentos que podem ter influenciado os orçamentos realizados pelo 
# governo na época.

# Analisando 2019 e 2022 quais setores mais investidos no início e no fim de um mandato. Mas para isso
# vamos considerar 2020 e 2021 também, para que não possamos tirar conclusões precipitadas apenas com 
# os extremos do mandato. Como minha análise é focada especificamente em orçamentos diretos, vamos considerar
# todas as subfunções ligadas diretamente à educação como um setor único. 

valores_a_manter = [2019, 2020, 2021, 2022]
condicao = ae.df_sem_outliers['EXERCÍCIO'].isin(valores_a_manter)
df_filtrado = ae.df_sem_outliers.loc[condicao]

df_filtrado.loc[df_filtrado['NOME SUBFUNÇÃO'].isin(['Educação básica', 'Educação de jovens e adultos', 'Educação especial', 
'Educação infantil', 'Ensino profissional', 'Ensino superior', 
'Transferências para a educação básica']), 'NOME SUBFUNÇÃO'] = 'EDUCAÇÃO'

grf.plotar_colunas_empilhadas_normalizado(df_filtrado,'NOME SUBFUNÇÃO', 'EXERCÍCIO', 'ORÇAMENTO REALIZADO (R$)', 
'Orçamentos por setores')

# Após selecionar os dados relativos a um período de quatro anos (um mandato) e analisar os orçamentos, com o propósito
# de agrupar subfunções intrinsecamente relacionadas à educação em um único grupo, tornou-se evidente que os investimentos 
# intimamente ligados à educação, são consistentemente um grupo com maior alocação de recursos, independentemente do ano. 
# Por outro lado, os investimentos em áreas menos diretamente relacionadas à educação são notavelmente menores. Agora, é de  
# interesse observar se a porcentagem dos orçamentos destinados a esse grupo intimamente ligados à educação apresentou variações 
# ao longo de cada ano.

#Para uma melhor visualização, vamos considerar os setores que não forem relacionados a educação como um só grupo -"outros".

anos_desejados = [2019, 2020, 2021, 2022]
df_filtrado.loc[~df_filtrado['NOME SUBFUNÇÃO'].isin(['EDUCAÇÃO']), 'NOME SUBFUNÇÃO'] = 'OUTROS'
for ano_desejado in anos_desejados:
    df_novo = df_filtrado[df_filtrado['EXERCÍCIO'] == ano_desejado]
    soma_orcamento = df_novo.groupby('NOME SUBFUNÇÃO')['ORÇAMENTO REALIZADO (R$)'].sum()
    labels = soma_orcamento.index
    valores = soma_orcamento.values
    
    mp.figure(figsize=(6, 6))  
    mp.pie(valores, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    mp.title(f'Gráfico de Pizza - Distribuição de Orçamento Realizado em {ano_desejado}')
    mp.show()

# Fica evidente que os orçamentos realizados pelo governo na educação nos anos de 2019, 2020, 2021 e 2022
# foram respectivamente de 71,5%, 72,6%, 71,9%, 74,5%. Ou seja no ano de eleição teve um gasto maior,
# enquanto o menor gasto foi localizado no primeiro ano de tal mandato, apesar de ser esperado que os 
# menores orçamentos sejam nos anos de 2020 e 2021 devido a pandemia. 


