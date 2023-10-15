import matplotlib.pyplot as plt
import pandas as pd 
import graficos as graf
import analiseexporatoria as ae
import datacleaning as dt 
import boxplot as bx 

#para minha análise, vou começar teorizando que em anos eleitorais os gastos em geral foram maiores, nosso grupo coletou dados do governo do portal de
#transparência, com gastos do governo nos anos de 2014 a 2023
#nesse caso, os anos eleitorais foram: 2014, 2018 e 2022, ou seja, nesses anos os gastos devem ser superiores aos demais gastos
df = pd.read_csv('df_final')

plt.hist(df['column'], bins=10)
plt.title('analise do orçamento(2014-2023)')
plt.xlabel('anos')
plt.ylabel('orçamento(R$)')
plt.show()
#TODO: grafico com os dados que eu preciso(colunas)


#TODO: linha para completar com os resultados(DESCREVER OS RESULTADOS)


#TODO gráfico com outliers(boxplot)

#na minha analise individual vou desconsiderar os outliers em certos casos(como esse primeiro por exemplo, pois são valores muito fora da escala normal do resto dos valores, 
# o que de certa forma corrompe para a análise geral, grande parte dos outliers são muito altos )


# minha segunda hipótese, é de que, no período pandêmico(2020 e 2021) os investimentos em educação foram super baixos, visto que o mundo estava passando por um 
# completo caos na saúde, no qual grande parte dos investimentos são direcionados foram direcionados ao setor da saúde, a tecnologia para produção de vacinas 
# mais rápidas(no caso para a compra de vacinas que foram produzidas) e meio que a educação foi mais "deixada de lado" nessa época

#TODO: análise com outliers, e análise sem outliers (para ver os pequenos investimentos e os grandes investimentos)

#analisar quais áreas  mais foram investidas ao longo do tempo no nosso intervalo

#TODO: gráfico de linhas para confirmar minhas hipóteses


#hipótese, a tendência dos investimentos em educação ao longo dos anos é de sempre aumentar, para satisfazer as demandas(fazer um gráfico de linhas com os gastos em educação no Brasil e comparar importando outro gráfico)