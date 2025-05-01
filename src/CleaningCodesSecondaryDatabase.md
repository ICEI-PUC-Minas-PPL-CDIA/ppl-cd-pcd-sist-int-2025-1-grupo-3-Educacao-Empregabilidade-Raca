# CÓDIGO DA LIMPEZA DA BASE CAGED

# Etapa 1: Instalar dependência
!pip install openpyxl

# Etapa 2: Importar bibliotecas
import pandas as pd
import numpy as np
from google.colab import files

# Etapa 3: Upload do arquivo CAGED
print("📁 Faça upload do arquivo 'panorama_anual_caged_2023.xlsx'")
uploaded = files.upload()

# Etapa 4: Carregar a base
import io
file_name = next(iter(uploaded))
df = pd.read_excel(io.BytesIO(uploaded[file_name]))

# Etapa 5: Renomear colunas e mapear valores
df.columns = df.columns.str.lower().str.strip()

mapas = {
    "sexo": {1: 0, 3: 1},  # masculino:0, feminino:1
    "raçacor": {
        1: 0,  # Branca
        2: 1,  # Preta
        3: 2,  # Parda
        4: 3,  # Amarela
        5: 4,  # Indígena
        6: 5,  # Não informado
        9: 6   # Ignorado
    },
    # Opcional: grau de instrução pode ser agrupado
    "graudeinstrução": {
        1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2,
        7: 3, 8: 4, 9: 5, 10: 5, 11: 6, 80: 7
    }
}

for col, mapping in mapas.items():
    if col in df.columns:
        df[col] = df[col].map(mapping)

# Etapa 6: Remover colunas desnecessárias
colunas_remover = ['subclasse', 'categoria', 'seção', 'unidadesaláriocódigo']
df.drop(columns=[col for col in colunas_remover if col in df.columns], inplace=True)

# Etapa 7: Tratar dados ausentes
limite_nulos = 0.4
df = df[df.columns[df.isnull().mean() < limite_nulos]]
df = df.dropna()

# Etapa 8: Remoção de outliers com IQR
def remover_outliers_iqr(data, col):
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    lim_inf = q1 - 1.5 * iqr
    lim_sup = q3 + 1.5 * iqr
    return data[(data[col] >= lim_inf) & (data[col] <= lim_sup)]

colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns

for col in colunas_numericas:
    df = remover_outliers_iqr(df, col)

# Etapa 9: Exportar
df.to_csv("panorama_caged_tratada.csv", index=False)
print("\n✅ Arquivo 'panorama_caged_tratada.csv' salvo com sucesso!")
