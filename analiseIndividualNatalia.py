import boxplot as bx
import graficos as grf
import datacleaning as dtc 
import analiseexporatoria as ae
import pandas as pd
import matplotlib.pyplot as mp

#Analisando os outliers
bx.boxplot_coluna_de_dataframe(ae.df_final,'ORÇAMENTO REALIZADO (R$)')

# É perceptível que, na visualização do box plot do DataFrame limpo e organizado com os dados de orçamento do governo na educação,
# os outliers são consideravelmente poucos. Além disso, é notório um certo padrão
# de outliers a cada ano, e que tais outliers, em sua maioria, estão acima da média de gastos. Isso significa que todo ano o governo
# sempre vai fazer investimentos consideráveis em comparação com a maioria dos investimentos. O que pode indicar que esses
# orçamentos são "obrigatórios" a cada ano, independentemente de ser um ano de eleição ou não.
# São poucos outliers baixos, também padronizados a cada ano. Indicando que, independentemente
# de ser um ano de eleição ou não, sempre haverá ações recorrentes em todo ano por exemplo:

# - Apoio a projetos comunitários: Financiar projetos de voluntariado ou iniciativas que envolvam a comunidade na educação.
# - Programas de tutoria de curto prazo: Fornecer apoio educacional adicional a grupos específicos de alunos por um período limitado,
#   entre outras iniciativas. Esses são eventos que são triviais de acontecer em qualquer governo.

# Portanto, devido a essa padronização de
# outliers a cada ano, independentemente de ser um ano de eleição ou não, podemos ignorá-los e continuar analisando os orçamentos
# realizados na educação pelo governo a cada ano, para tirar conclusões.
#Não é apropriado analisar o orçamento realizado em educação do governo para o ano de 2023 neste momento, uma vez que o ano ainda não 
#chegou ao fim.


#Análise sem outliers
    #""""
    #colunas
    #"""
#É notório que nos anos [especificar anos] a soma dos orçamentos destinados à educação foi consideravelmente maior do que em outros anos.
#desconsiderar 20 e 21

#Análise de 2017 reforma do ensino médio (pode ser que aumentou o investimo em ens. básico)
#stacked bar com os setores


# , é interessante analisar inicio 2019 e fim 2022 nos principais setores investidos no início e no fim de um mandato. 
#"""
#stacked bar normalizada 
#"""






