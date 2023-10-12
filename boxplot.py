import pandas as pd
import datacleaning as dtc
import analiseexporatoria as ae
import matplotlib.pyplot as plt

# Certifique-se de que as colunas que você deseja converter para numérico estão corretas
ae.df_final['NOME FUNÇÃO'] = pd.to_numeric(ae.df_final['NOME FUNÇÃO'], errors='coerce')
ae.df_final['NOME SUBFUNÇÃO'] = pd.to_numeric(ae.df_final['NOME SUBFUNÇÃO'], errors='coerce')
ae.df_final['EXERCÍCIO'] = pd.to_numeric(ae.df_final['EXERCÍCIO'], errors='coerce')

