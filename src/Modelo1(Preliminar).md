```

!pip install imbalanced-learn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from google.colab import files
import io

print("📁 Faça upload de 'base_final_combinada_kaggle_caged_corrigida_ok.csv'")
uploaded = files.upload()
file_name = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[file_name]))

df = df.fillna(-1)

X = df.drop(columns=['vinculo_formal', 'situacao_trabalho'])
y = df['vinculo_formal']

for col in X.select_dtypes(include='object').columns:
    X[col] = LabelEncoder().fit_transform(X[col].astype(str))

sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

modelo = DecisionTreeClassifier(max_depth=5, random_state=42)
modelo.fit(X_train, y_train)

y_pred_train = modelo.predict(X_train)
train_acc = accuracy_score(y_train, y_pred_train)

y_pred = modelo.predict(X_test)
test_acc = accuracy_score(y_test, y_pred)

print(f"\n✅ Acurácia no treino: {train_acc:.2%}")
print(f"✅ Acurácia no teste: {test_acc:.2%}")

print("\n📊 Relatório de Classificação (conjunto de teste):")
print(classification_report(y_test, y_pred, target_names=['Não Formal', 'Formal']))
