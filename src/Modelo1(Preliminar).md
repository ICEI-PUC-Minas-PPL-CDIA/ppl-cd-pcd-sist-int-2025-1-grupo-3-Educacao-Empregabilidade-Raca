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
from imblearn.over_sampling import SMOTE, ADASYN
from sklearn.decomposition import PCA
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

print("🎯 Distribuição antes do SMOTE:")
print(y.value_counts(normalize=True).rename({0: 'Não Formal', 1: 'Formal'}))

sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)
print("\n🎯 Distribuição após o SMOTE:")
print(y_res.value_counts(normalize=True).rename({0: 'Não Formal', 1: 'Formal'}))
pca = PCA(n_components=2, random_state=42)
X_vis = pca.fit_transform(X_res)
y_vis = y_res.reset_index(drop=True)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_vis[:, 0], y=X_vis[:, 1], hue=y_vis, palette='Set2', alpha=0.5)
plt.title("🔍 Visualização das Amostras após SMOTE (PCA)")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.legend(title='Classe', labels=['Não Formal', 'Formal'])
plt.tight_layout()
plt.show()

adasyn = ADASYN(random_state=42)
X_res_ada, y_res_ada = adasyn.fit_resample(X, y)
print("\n🔄 Balanceamento com ADASYN:")
print(y_res_ada.value_counts(normalize=True))

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

# Grade de hiperparâmetros
param_dist_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None],
    'bootstrap': [True, False]
}

# RandomizedSearchCV
random_search_rf = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist_rf,
    n_iter=10,
    cv=3,
    scoring='accuracy',
    random_state=42,
    n_jobs=1
)

# Treinando
random_search_rf.fit(X_train, y_train)
modelo = random_search_rf.best_estimator_

# Avaliação
y_pred_train = modelo.predict(X_train)
y_pred = modelo.predict(X_test)

train_acc = accuracy_score(y_train, y_pred_train)
test_acc = accuracy_score(y_test, y_pred)

print("\n🌲 Melhor modelo (Random Forest):")
print(random_search_rf.best_params_)

print(f"\n✅ Acurácia no treino: {train_acc:.2%}")
print(f"✅ Acurácia no teste: {test_acc:.2%}")

print("\n📊 Relatório de Classificação (conjunto de teste):")
print(classification_report(y_test, y_pred, target_names=['Não Formal', 'Formal']))

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Não Formal', 'Formal'], yticklabels=['Não Formal', 'Formal'])
plt.title("Matriz de Confusão (Heatmap)")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.tight_layout()
plt.show()

plt.figure(figsize=(40, 20))  # aumentar mais ainda o tamanho
plot_tree(
    modelo.estimators_[0],  # primeira árvore da floresta
    feature_names=X.columns,
    class_names=['Não Formal', 'Formal'],
    filled=True,
    rounded=True,
    fontsize=12
)


plt.title("Árvore de Decisão - Vínculo Formal")
plt.savefig("arvore_decisao_vinculo_formal.png", dpi=300)
plt.show()

from google.colab import files
files.download("arvore_decisao_vinculo_formal.png")

from sklearn.metrics import roc_curve, auc

y_proba = modelo.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC Curve (área = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('Falso Positivo (1 - Especificidade)')
plt.ylabel('Verdadeiro Positivo (Sensibilidade)')
plt.title('Curva ROC - Classificação de Vínculo Formal')
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()

```
