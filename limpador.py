import pandas as pd
import numpy as np

def limpar_dados(df):
    idade_media = df['Idade'].mean()
    df["Idade"] = df['Idade'].fillna(idade_media)
    df = df.dropna(subset=['Resposta_1'])
    df["Resposta_1"] = df['Resposta_1'].str.capitalize()
    df["Valor_Gasto"] = df['Valor_Gasto'].fillna(df['Valor_Gasto'].median())
    return df


df = pd.DataFrame({"ID": [1, 2, 3, 4, 5, 6],
    "Idade": [25, 30, np.nan, 45, 22, 50],
    "Resposta_1": ['SIM', 'não', 'Sim', 'sim', 'NÃO', np.nan],
    "Valor_Gasto": [100.5, 50.0, 75.2, np.nan, 200.0, 10.0]})

print(df)
print("\n")
df = limpar_dados(df)
print(df)