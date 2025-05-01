import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
caminho_arquivo = '/content/State_of_data_BR_2023_Kaggle - df_survey_2023 (2).csv'
dados = pd.read_csv(caminho_arquivo)

# Remover espaços extras nos nomes das colunas
dados.columns = dados.columns.str.strip()

# Selecionar somente as colunas de interesse
colunas_interesse = ["('P1_b ', 'Genero')", "('P1_c ', 'Cor/raca/etnia')", "('P1_l ', 'Nivel de Ensino')",
                     "('P1_m ', 'Área de Formação')", "('P2_a ', 'Qual sua situação atual de trabalho?')",
                     "('P2_b ', 'Setor')", "('P2_g ', 'Nivel')", "('P2_h ', 'Faixa salarial')"]
dados_selecionados = dados[colunas_interesse]

# Renomear colunas para facilitar o acesso
dados_selecionados.columns = ['Genero', 'Cor_raca', 'Nivel_Ensino', 'Area_Formacao',
                              'Situacao_Trabalho', 'Setor', 'Nivel_Cargo', 'Faixa_Salarial']

# 1. Número de Pessoas Pretas por Nível de Ensino
plt.figure(figsize=(14, 6))
sns.countplot(data=dados_selecionados[dados_selecionados['Cor_raca'] == 'Preta'], x='Nivel_Ensino')
plt.title('Número de Pessoas Negras por Nível de Ensino')
plt.xlabel('Nível de Ensino')
plt.ylabel('Contagem de Pessoas')
plt.xticks(rotation=0, ha='center')
plt.tight_layout(pad=2.0)
plt.show()

# 2. Distribuição de Pessoas com Doutorado ou Phd por Gênero e Cor/Raça
plt.figure(figsize=(12, 6))
sns.countplot(data=dados_selecionados[dados_selecionados['Nivel_Ensino'] == 'Doutorado ou Phd'],
              x='Genero', hue='Cor_raca')
plt.title('Distribuição de Pessoas com Doutorado por Gênero e Cor/Raça')
plt.xlabel('Gênero')
plt.ylabel('Contagem de Pessoas')
plt.legend(title='Cor/Raça')
plt.xticks(rotation=0, ha='center')
plt.tight_layout(pad=2.0)
plt.show()

# 3. Número de Pessoas com Pós-graduação por Área de Formação
plt.figure(figsize=(12, 6))
sns.countplot(data=dados_selecionados[dados_selecionados['Nivel_Ensino'] == 'Pós-graduação'],
              x='Area_Formacao')
plt.title('Número de Pessoas com Pós-graduação por Área de Formação')
plt.xlabel('Área de Formação')
plt.ylabel('Contagem de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 4. Pessoas com Graduação/Bacharelado e Seus Setores de Atuação
plt.figure(figsize=(12, 6))
sns.countplot(data=dados_selecionados[dados_selecionados['Nivel_Ensino'] == 'Graduação/Bacharelado'],
              x='Setor')
plt.title('Pessoas com Ensino Superior e Seus Setores de Atuação')
plt.xlabel('Setor')
plt.ylabel('Contagem de Pessoas')
plt.xticks(rotation=0, ha='center')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 5. Número de Pessoas com Graduação/Bacharelado em Tecnologia por Gênero e Cor/Raça
plt.figure(figsize=(12, 6))
sns.countplot(data=dados_selecionados[(dados_selecionados['Nivel_Ensino'] == 'Graduação/Bacharelado') &
                                      (dados_selecionados['Setor'] == 'Tecnologia/Fábrica de Software')],
              x='Genero', hue='Cor_raca')
plt.title('Número de Pessoas com Doutorado em Tecnologia por Gênero e Cor/Raça')
plt.xlabel('Gênero')
plt.ylabel('Contagem de Pessoas')
plt.legend(title='Cor/Raça')
plt.xticks(rotation=0, ha='center')
plt.tight_layout(pad=2.0)
plt.show()

# 6. Número de Pessoas Empregadas e Desempregadas na Área de Formação de Computação / Engenharia de Software / Sistemas de Informação/ TI
dados_ti = dados_selecionados[dados_selecionados['Area_Formacao'].str.contains("Computação / Engenharia de Software / Sistemas de Informação/ TI", case=False, na=False)]
plt.figure(figsize=(12, 6))
sns.countplot(data=dados_ti, x='Situacao_Trabalho')
plt.title('Número de Pessoas Empregadas e Desempregadas na Área de Formação de Computação / Engenharia de Software / Sistemas de Informação/ TI')
plt.xlabel('Situação de Trabalho')
plt.ylabel('Contagem de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 7. Nível de Ensino por Área de Formação
plt.figure(figsize=(14, 6))
sns.countplot(data=dados_selecionados, x='Nivel_Ensino', hue='Area_Formacao')
plt.title('Nível de Ensino por Área de Formação')
plt.xlabel('Nível de Ensino')
plt.ylabel('Contagem de Pessoas')
plt.legend(title='Área de Formação')
plt.xticks(rotation=0, ha='center')
plt.tight_layout(pad=2.0)
plt.show()
