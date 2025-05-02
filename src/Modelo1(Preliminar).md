# Etapa 1: Instalar SMOTE
!pip install imbalanced-learn

# Etapa 2: Importações
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

# Etapa 3: Upload da base final corrigida
print("📁 Faça upload de 'base_final_combinada_kaggle_caged_corrigida_ok.csv'")
uploaded = files.upload()
file_name = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[file_name]))

# Etapa 4: Substituir valores ausentes
df = df.fillna(-1)

