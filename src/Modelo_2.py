# Instalar a versão mais recente do imbalanced-learn (caso necessário)
!pip install -U imbalanced-learn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from google.colab import files
import io
import numpy as np

# 1. Carregar a base
print("📁 Faça upload de 'base_final_combinada_kaggle_caged_corrigida_ok.csv'")
uploaded = files.upload()
file_name = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[file_name]))

# 2. Selecionar e limpar colunas relevantes
colunas = ['idade', 'cor_raca', 'nivel_ensino', 'vinculo_formal']
df = df[colunas].copy()
df = df.dropna()  # Remover linhas com NaN

# 3. Garantir consistência nos dados
df['idade'] = pd.to_numeric(df['idade'], errors='coerce')  # Converter idade para numérico
df['vinculo_formal'] = pd.to_numeric(df['vinculo_formal'], errors='coerce').astype(int)  # Converter para inteiro
df = df[df['vinculo_formal'].isin([0, 1])]  # Manter apenas 0 e 1
df = df.dropna()  # Remover linhas inválidas após conversão

# 4. Definir variáveis categóricas e numéricas
categorical_features = ['cor_raca', 'nivel_ensino']
numeric_features = ['idade']

# 5. Criar pré-processador
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), categorical_features)
    ])

# 6. Separar variáveis
X = df.drop('vinculo_formal', axis=1)
y = df['vinculo_formal'].values  # Converter para array 1D

# 7. Verificar dados
print("Shape de X:", X.shape)
print("Shape de y:", y.shape)
print("Valores únicos em y:", np.unique(y))

# 8. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# 9. Aplicar pré-processamento ao conjunto de treino
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# 10. Aplicar SMOTE apenas ao conjunto de treino
smote = SMOTE(sampling_strategy=0.5)  # Ajustado para 0.5 (1:2)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_processed, y_train)

