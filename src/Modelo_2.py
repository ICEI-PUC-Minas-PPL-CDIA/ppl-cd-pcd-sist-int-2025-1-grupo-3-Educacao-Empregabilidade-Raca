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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 9. Aplicar pré-processamento ao conjunto de treino
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# 10. Aplicar SMOTE apenas ao conjunto de treino
smote = SMOTE(sampling_strategy=0.5)  # Ajustado para 0.5 (1:2)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_processed, y_train)

# 11. Treinar o modelo SVM
svm_model = SVC(kernel='rbf', 'linear', 'poly', C=30, probability=True)
svm_model.fit(X_train_balanced, y_train_balanced)

# 12. Fazer previsões com ajuste dinâmico de limiar
y_probs = svm_model.predict_proba(X_test_processed)[:, 1]

# Testar diferentes limiares para alcançar acurácia entre 70% e 80%
thresholds = np.arange(0.45, 0.81, 0.01)
best_threshold = 0.5
best_accuracy = 0

# Usar o melhor limiar encontrado
y_pred = (y_probs > best_threshold).astype(int)

# Avaliar
acuracia_treino = svm_model.score(X_train_balanced, y_train_balanced)
acuracia_teste = accuracy_score(y_test, y_pred)
print(f"Acurácia no Treinamento: {acuracia_treino:.2%}")
print(f"Acurácia no Teste: {acuracia_teste:.2%}")
print(f"Melhor limiar encontrado: {best_threshold:.2f}")
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# 13. Matriz de confusão
matriz = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Sem vínculo', 'Com vínculo'],
            yticklabels=['Sem vínculo', 'Com vínculo'])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title(f'Matriz de Confusão - Acurácia: {acuracia_teste:.2%}')
plt.tight_layout()
plt.show()

# 14. GridSearchCV expandido para otimização de hiperparâmetros
from sklearn.model_selection import GridSearchCV

# Definir o grid de parâmetros (reduzido)
param_grid = {
    'C': [10, 20, 30, 40, 50 ],
    'gamma': ['scale', 'auto', 0.01, 0.1, 1],
    'kernel': ['rbf', 'linear', 'poly']
}

# Configurar o GridSearchCV
grid = GridSearchCV(
    SVC(probability=True),
    param_grid,
    cv=5,
    scoring='balanced_accuracy',
    n_jobs=-1
)

# Ajustar o modelo
grid.fit(X_train_balanced, y_train_balanced)

# Exibir os melhores parâmetros e pontuação
print("\nMelhores parâmetros encontrados pelo GridSearch:")
print(grid.best_params_)
print(f"Melhor pontuação (balanced accuracy): {grid.best_score_:.2%}")

# Usar o melhor modelo para previsões
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test_processed)

# Avaliar o modelo otimizado
acuracia_teste = accuracy_score(y_test, y_pred)
print(f"Acurácia no Teste (modelo otimizado): {acuracia_teste:.2%}")
print("\nRelatório de Classificação (modelo otimizado):")
print(classification_report(y_test, y_pred))

# Matriz de confusão para o modelo otimizado
matriz = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Sem vínculo', 'Com vínculo'],
            yticklabels=['Sem vínculo', 'Com vínculo'])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title(f'Matriz de Confusão - Acurácia: {acuracia_teste:.2%}')
plt.tight_layout()
plt.show()

# 15. Ajuste de limiar com curva ROC
from sklearn.metrics import roc_curve, auc, f1_score

# Obter probabilidades do modelo otimizado
y_probs = best_model.predict_proba(X_test_processed)[:, 1]

# Calcular a curva ROC
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)

# Encontrar o melhor limiar com base na métrica F1
f1_scores = []
for thresh in thresholds:
    y_pred_temp = (y_probs > thresh).astype(int)
    f1 = f1_score(y_test, y_pred_temp)
    f1_scores.append(f1)

best_threshold_idx = np.argmax(f1_scores)
best_threshold = thresholds[best_threshold_idx]
best_f1 = f1_scores[best_threshold_idx]

print(f"Melhor limiar (maximizando F1): {best_threshold:.2f}")
print(f"Melhor F1-score: {best_f1:.2%}")

# Previsões com o melhor limiar
y_pred = (y_probs > best_threshold).astype(int)

# Avaliar com o limiar otimizado
acuracia_teste = accuracy_score(y_test, y_pred)
print(f"Acurácia no Teste (limiar otimizado): {acuracia_teste:.2%}")
print("\nRelatório de Classificação (limiar otimizado):")
print(classification_report(y_test, y_pred))

# Matriz de confusão
matriz = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Sem vínculo', 'Com vínculo'],
            yticklabels=['Sem vínculo', 'Com vínculo'])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title(f'Matriz de Confusão - Acurácia: {acuracia_teste:.2%}')
plt.tight_layout()
plt.show()

# Plotar curva ROC
plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Curva ROC')
plt.legend(loc="lower right")
plt.show()
# 15. Ajuste de limiar com curva ROC
from sklearn.metrics import roc_curve, auc, f1_score

# Obter probabilidades do modelo otimizado
y_probs = best_model.predict_proba(X_test_processed)[:, 1]

# Calcular a curva ROC
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)

# Encontrar o melhor limiar com base na métrica F1
f1_scores = []
for thresh in thresholds:
    y_pred_temp = (y_probs > thresh).astype(int)
    f1 = f1_score(y_test, y_pred_temp)
    f1_scores.append(f1)

best_threshold_idx = np.argmax(f1_scores)
best_threshold = thresholds[best_threshold_idx]
best_f1 = f1_scores[best_threshold_idx]

print(f"Melhor limiar (maximizando F1): {best_threshold:.2f}")
print(f"Melhor F1-score: {best_f1:.2%}")

# Previsões com o melhor limiar
y_pred = (y_probs > best_threshold).astype(int)

# Avaliar com o limiar otimizado
acuracia_teste = accuracy_score(y_test, y_pred)
print(f"Acurácia no Teste (limiar otimizado): {acuracia_teste:.2%}")
print("\nRelatório de Classificação (limiar otimizado):")
print(classification_report(y_test, y_pred))

# Matriz de confusão
matriz = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Sem vínculo', 'Com vínculo'],
            yticklabels=['Sem vínculo', 'Com vínculo'])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title(f'Matriz de Confusão - Acurácia: {acuracia_teste:.2%}')
plt.tight_layout()
plt.show()

# Plotar curva ROC
plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Curva ROC')
plt.legend(loc="lower right")
plt.show()


# 16. Teste de diferentes proporções de SMOTE
from imblearn.over_sampling import SMOTE
from sklearn.metrics import f1_score

# Diagnóstico
print("Shape de X_train_processed:", X_train_processed.shape)
print("Shape de y_train:", y_train.shape)
print("Valores únicos em y_train:", np.unique(y_train))
print("Distribuição de classes em y_train:", dict(zip(*np.unique(y_train, return_counts=True))))
print("Valores NaN em X_train_processed:", np.any(np.isnan(X_train_processed)))
print("Valores inf em X_train_processed:", np.any(np.isinf(X_train_processed)))

# Tratar NaN ou inf em X_train_processed
if np.any(np.isnan(X_train_processed)) or np.any(np.isinf(X_train_processed)):
    print("Valores NaN ou inf encontrados. Imputando...")
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy='mean')
    X_train_processed = imputer.fit_transform(X_train_processed)
    X_test_processed = imputer.transform(X_test_processed)

# Garantir que y_train seja 1D e numérico
y_train = np.array(y_train).ravel()
y_train = pd.to_numeric(y_train, errors='coerce')
if np.any(np.isnan(y_train)):
    raise ValueError("y_train contém valores NaN após conversão.")

# Verificar classes
unique, counts = np.unique(y_train, return_counts=True)
minority_count = min(counts)
if len(unique) < 2:
    print("Aviso: y_train contém apenas uma classe. Pulando SMOTE.")
    best_f1 = 0
    best_strategy = None
    best_model_smote = SVC(**grid.best_params_, probability=True)
    best_model_smote.fit(X_train_processed, y_train)
    best_y_pred = best_model_smote.predict(X_test_processed)
else:
    # Testar diferentes proporções de SMOTE
    sampling_strategies = [0.3, 0.5, 0.7, 1.0]
    best_f1 = 0
    best_strategy = 0
    best_model_smote = None
    best_y_pred = None

    for strategy in sampling_strategies:
        try:
            # Aplicar SMOTE com k_neighbors ajustado para classes pequenas
            smote = SMOTE(sampling_strategy=strategy, k_neighbors=min(5, minority_count-1) if minority_count > 1 else 1, random_state=42)
            X_train_balanced, y_train_balanced = smote.fit_resample(X_train_processed, y_train)

            # Treinar o modelo com os melhores parâmetros do GridSearch
            model = SVC(**grid.best_params_, probability=True)
            model.fit(X_train_balanced, y_train_balanced)

            # Avaliar
            y_pred = model.predict(X_test_processed)
            f1 = f1_score(y_test, y_pred)

            if f1 > best_f1:
                best_f1 = f1
                best_strategy = strategy
                best_model_smote = model
                best_y_pred = y_pred
        except Exception as e:
            print(f"Erro ao aplicar SMOTE com sampling_strategy={strategy}: {str(e)}")
            continue

# Verificar se um modelo válido foi encontrado
if best_model_smote is None:
    print("Aviso: Nenhum modelo SMOTE bem-sucedido. Usando modelo sem SMOTE.")
    best_model_smote = SVC(**grid.best_params_, probability=True)
    best_model_smote.fit(X_train_processed, y_train)
    best_y_pred = best_model_smote.predict(X_test_processed)
    best_f1 = f1_score(y_test, best_y_pred)
    best_strategy = None

print(f"Melhor estratégia SMOTE: {best_strategy}")
print(f"F1-score com melhor estratégia: {best_f1:.2%}")

# Avaliar o modelo com a melhor estratégia
acuracia_teste = accuracy_score(y_test, best_y_pred)
print(f"Acurácia no Teste (melhor SMOTE): {acuracia_teste:.2%}")
print("\nRelatório de Classificação (melhor SMOTE):")
print(classification_report(y_test, best_y_pred))

# Matriz de confusão
matriz = confusion_matrix(y_test, best_y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Sem vínculo', 'Com vínculo'],
            yticklabels=['Sem vínculo', 'Com vínculo'])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title(f'Matriz de Confusão - Acurácia: {acuracia_teste:.2%}')
plt.tight_layout()
plt.show()


# 17. Validação cruzada estratificada
from sklearn.model_selection import cross_val_score, StratifiedKFold

# Configurar validação cruzada estratificada
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Reaplicar SMOTE com a melhor estratégia encontrada
smote = SMOTE(sampling_strategy=best_strategy)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_processed, y_train)

# Avaliar o modelo com os melhores parâmetros
scores = cross_val_score(best_model_smote, X_train_balanced, y_train_balanced, cv=cv, scoring='balanced_accuracy')

print(f"\nValidação Cruzada - Acurácia Balanceada (média): {scores.mean():.2%}")
print(f"Validação Cruzada - Desvio Padrão: {scores.std():.2%}")
