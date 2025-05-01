# CÓDIGO DA LIMPEZA DA BASE KAGLE

# Etapa 1: Instalar biblioteca para arquivos .xlsx
!pip install openpyxl

# Etapa 2: Importar bibliotecas
import pandas as pd
import numpy as np
from google.colab import files
import io

# Etapa 3: Upload do arquivo
print("📁 Faça upload do arquivo 'Base Kagle Limpa (colunas).xlsx'")
uploaded = files.upload()

# Etapa 4: Carregar o arquivo
file_name = next(iter(uploaded))
df = pd.read_excel(io.BytesIO(uploaded[file_name]))

# Etapa 5: Renomear colunas para facilitar a manipulação
df.rename(columns={
    "('P1_a ', 'Idade')": "idade",
    "('P1_b ', 'Genero')": "genero",
    "('P1_c ', 'Cor/raca/etnia')": "cor_raca",
    "('P1_l ', 'Nivel de Ensino')": "nivel_ensino",
    "('P2_h ', 'Faixa salarial')": "faixa_salarial",
    "('P1_e_2 ', 'Experiencia prejudicada devido a minha Cor Raça Etnia')": "experiencia_prejudicada",
    "('P2_a ', 'Qual sua situação atual de trabalho?')": "situacao_trabalho"
}, inplace=True)

# Etapa 6: Tratar valores ausentes
# ➤ Remove colunas com mais de 40% de nulos
limite_nulos = 0.4
df = df[df.columns[df.isnull().mean() < limite_nulos]]
# ➤ Remove todas as linhas com valores ausentes restantes
df = df.dropna()

# Etapa 7: Substituir categorias textuais por códigos numéricos
mapas = {
    "genero": {
        "Masculino": 0,
        "Feminino": 1,
        "Outro": 2,
        "Prefiro não informar": 3
    },
    "cor_raca": {
        "Branca": 0,
        "Preta": 1,
        "Parda": 2,
        "Amarela": 3,
        "Indígena": 4,
        "Outra": 5,
        "Prefiro não informar": 6
    },
    "nivel_ensino": {
        "Não tenho graduação formal": 0,
        "Estudante de Graduação": 1,
        "Graduação/Bacharelado": 2,
        "Pós-graduação": 3,
        "Mestrado": 4,
        "Doutorado ou Phd": 5,
        "Prefiro não informar": 6
    },
    "faixa_salarial": {
        "de R$ 1.001/mês a R$ 2.000/mês": 1,
        "de R$ 2.001/mês a R$ 3.000/mês": 2,
        "de R$ 3.001/mês a R$ 4.000/mês": 3,
        "de R$ 4.001/mês a R$ 6.000/mês": 4,
        "de R$ 6.001/mês a R$ 8.000/mês": 5,
        "de R$ 8.001/mês a R$ 12.000/mês": 6,
        "de R$ 12.001/mês a R$ 16.000/mês": 7,
        "de R$ 16.001/mês a R$ 20.000/mês": 8,
        "de R$ 20.001/mês a R$ 25.000/mês": 9,
        "Acima de R$ 40.001/mês": 10
    },
    "situacao_trabalho": {
        "Empregado (CLT)": 1,
        "Empreendedor ou Empregado (CNPJ)": 2,
        "Servidor Público": 3,
        "Estagiário": 4,
        "Freelancer": 5,
        "Vivo no Brasil e trabalho remoto para empresa de fora do Brasil": 6,
        "Vivo fora do Brasil e trabalho para empresa de fora do Brasil": 7,
        "Prefiro não informar": 0
    }
}

for coluna, mapa in mapas.items():
    if coluna in df.columns:
        df[coluna] = df[coluna].map(mapa)

# Etapa 8: Função para remover outliers com base no IQR
def remover_outliers_iqr(data, col):
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    lim_inf = q1 - 1.5 * iqr
    lim_sup = q3 + 1.5 * iqr
    return data[(data[col] >= lim_inf) & (data[col] <= lim_sup)]

# Etapa 9: Aplicar remoção de outliers a todas as colunas numéricas
colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns

for col in colunas_numericas:
    df = remover_outliers_iqr(df, col)

# Etapa 10: Exportar a base tratada
df.to_csv("base_kaggle_tratada_corrigida.csv", index=False)
print("✅ Arquivo 'base_kaggle_tratada_corrigida.csv' salvo com sucesso!")
