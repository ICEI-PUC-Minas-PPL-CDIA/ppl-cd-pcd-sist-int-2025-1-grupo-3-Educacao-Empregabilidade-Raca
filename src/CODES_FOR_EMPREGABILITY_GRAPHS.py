 ## **CÓDIGO GRÁFICOS - State of Data 2023**
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo Excel (após fazer o upload no Colab)
df = pd.read_excel("State_of_data_BR_2023_Kaggle - df_survey_2023.xlsx")

# Selecionar colunas com os nomes exatos
df_emprego = df[[
    "('P1_c ', 'Cor/raca/etnia')", 
    "('P2_a ', 'Qual sua situação atual de trabalho?')", 
    "('P2_h ', 'Faixa salarial')"
]].copy()

# Renomear colunas
df_emprego.columns = ["raca_cor", "empregabilidade", "faixa_salarial"]

# Remover valores ausentes
df_emprego.dropna(subset=["raca_cor", "empregabilidade"], inplace=True)

# Gráfico: Empregabilidade por Raça/Cor
plt.figure(figsize=(12, 6))
sns.countplot(data=df_emprego, x="raca_cor", hue="empregabilidade", palette="Set2")
plt.title("Empregabilidade por Raça/Cor")
plt.xlabel("Raça/Cor")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.legend(title="Empregabilidade", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Código completo para gerar gráficos de Empregabilidade por Raça/Cor e Empregabilidade por Faixa Salarial
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo Excel (depois de fazer upload no Colab)
df = pd.read_excel("State_of_data_BR_2023_Kaggle - df_survey_2023.xlsx")

# Selecionar colunas com os nomes exatos
df_emprego = df[[
    "('P1_c ', 'Cor/raca/etnia')", 
    "('P2_a ', 'Qual sua situação atual de trabalho?')", 
    "('P2_h ', 'Faixa salarial')"
]].copy()

# Renomear colunas
df_emprego.columns = ["raca_cor", "empregabilidade", "faixa_salarial"]

# Remover valores ausentes
df_emprego.dropna(subset=["raca_cor", "empregabilidade", "faixa_salarial"], inplace=True)

# Gráfico 1: Empregabilidade por Raça/Cor
plt.figure(figsize=(12, 6))
sns.countplot(data=df_emprego, x="raca_cor", hue="empregabilidade", palette="Set2")
plt.title("Empregabilidade por Raça/Cor")
plt.xlabel("Raça/Cor")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.legend(title="Empregabilidade", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Gráfico 2: Empregabilidade por Faixa Salarial
plt.figure(figsize=(12, 6))
sns.countplot(data=df_emprego, x="faixa_salarial", hue="empregabilidade", palette="Set3")
plt.title("Empregabilidade por Faixa Salarial")
plt.xlabel("Faixa Salarial")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.legend(title="Empregabilidade", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
```
 ## **CÓDIGO GRÁFICOS - Cadastro Geral de Empregados e Desempregados**
``` 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📥 Carregar planilha (faça upload no Colab)
df = pd.read_excel("caged_set.xlsx")

# 🗺️ Mapear códigos de raça/cor para nomes
mapa_raca = {
    1: 'Branca',
    2: 'Preta',
    3: 'Parda',
    4: 'Amarela',
    5: 'Indígena',
    0: 'Não informado'
}
df['raçacor'] = df['raçacor'].map(mapa_raca)

# 🗺️ Mapear grau de instrução para nomes legíveis
mapa_instrucao = {
    1: 'Fund. Incompleto',
    2: 'Fund. Completo',
    3: 'Médio Incompleto',
    4: 'Médio Completo',
    5: 'Superior Incompleto',
    6: 'Superior Completo',
    7: 'Pós-graduação',
    9: 'Não informado'
}
df['graudeinstrução'] = df['graudeinstrução'].map(mapa_instrucao)

# 💰 Criar faixa salarial
def categorizar_salario(salario):
    if salario < 2000:
        return 'Até R$2000'
    elif salario < 4000:
        return 'R$2000–3999'
    elif salario < 6000:
        return 'R$4000–5999'
    else:
        return 'R$6000 ou mais'

df['faixa_salarial'] = df['salário'].apply(categorizar_salario)

# 🔍 Limpar valores nulos
df = df.dropna(subset=['raçacor', 'graudeinstrução', 'salário'])

# ========================== GRÁFICOS ==========================

# 📊 1 – Empregabilidade por Raça/Cor
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='raçacor', palette='Set2')
plt.title("Empregabilidade por Raça/Cor")
plt.xlabel("Raça/Cor")
plt.ylabel("Quantidade de Registros")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📘 2 – Empregabilidade por Grau de Instrução
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='graudeinstrução', palette='Set3')
plt.title("Empregabilidade por Grau de Instrução")
plt.xlabel("Grau de Instrução")
plt.ylabel("Quantidade de Registros")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 💸 3 – Empregabilidade por Faixa Salarial
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='faixa_salarial', order=['Até R$2000', 'R$2000–3999', 'R$4000–5999', 'R$6000 ou mais'], palette='pastel')
plt.title("Empregabilidade por Faixa Salarial")
plt.xlabel("Faixa Salarial")
plt.ylabel("Quantidade de Registros")
plt.tight_layout()
plt.show()

# 🔄 4 – Grau de Instrução por Raça/Cor
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='graudeinstrução', hue='raçacor', palette='husl')
plt.title("Distribuição de Grau de Instrução por Raça/Cor")
plt.xlabel("Grau de Instrução")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.legend(title="Raça/Cor", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 💼 5 – Faixa Salarial por Grau de Instrução
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='graudeinstrução', hue='faixa_salarial', palette='coolwarm')
plt.title("Faixa Salarial por Grau de Instrução")
plt.xlabel("Grau de Instrução")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.legend(title="Faixa Salarial", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 📦 6 – Boxplot de Salário por Raça/Cor
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='raçacor', y='salário', palette='Set2')
plt.title("Distribuição dos Salários por Raça/Cor")
plt.xlabel("Raça/Cor")
plt.ylabel("Salário (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```
## Gerar e salvar os gráficos como imagens:
```
import os
from matplotlib import pyplot as plt

# Criar pasta para imagens
os.makedirs("graficos", exist_ok=True)

# Função para salvar gráficos com título
def salvar_grafico(fig, nome):
    caminho = f"graficos/{nome}.png"
    fig.savefig(caminho, bbox_inches='tight')
    plt.close(fig)

# 1 – Empregabilidade por Raça/Cor
fig1 = plt.figure(figsize=(10,6))
sns.countplot(data=df, x='raçacor', palette='Set2')
plt.title("Empregabilidade por Raça/Cor")
plt.xlabel("Raça/Cor")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
salvar_grafico(fig1, "empregabilidade_raca")

# 2 – Empregabilidade por Grau de Instrução
fig2 = plt.figure(figsize=(10,6))
sns.countplot(data=df, x='graudeinstrução', palette='Set3')
plt.title("Empregabilidade por Grau de Instrução")
plt.xlabel("Grau de Instrução")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
salvar_grafico(fig2, "empregabilidade_instrucao")

# 3 – Faixa Salarial
fig3 = plt.figure(figsize=(10,6))
sns.countplot(data=df, x='faixa_salarial', order=['Até R$2000', 'R$2000–3999', 'R$4000–5999', 'R$6000 ou mais'], palette='pastel')
plt.title("Faixa Salarial dos Empregados")
plt.xlabel("Faixa Salarial")
plt.ylabel("Quantidade")
salvar_grafico(fig3, "faixa_salarial")

# 4 – Instrução por Raça/Cor
fig4 = plt.figure(figsize=(12,6))
sns.countplot(data=df, x='graudeinstrução', hue='raçacor', palette='husl')
plt.title("Distribuição de Grau de Instrução por Raça/Cor")
plt.xlabel("Grau de Instrução")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
salvar_grafico(fig4, "instrucao_por_raca")

# 5 – Faixa Salarial por Instrução
fig5 = plt.figure(figsize=(12,6))
sns.countplot(data=df, x='graudeinstrução', hue='faixa_salarial', palette='coolwarm')
plt.title("Faixa Salarial por Grau de Instrução")
plt.xlabel("Grau de Instrução")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
salvar_grafico(fig5, "salario_por_instrucao")

# 6 – Boxplot de Salário por Raça
fig6 = plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='raçacor', y='salário', palette='Set2')
plt.title("Distribuição dos Salários por Raça/Cor")
plt.xlabel("Raça/Cor")
plt.ylabel("Salário (R$)")
plt.xticks(rotation=45)
salvar_grafico(fig6, "boxplot_salario_raca")
```

