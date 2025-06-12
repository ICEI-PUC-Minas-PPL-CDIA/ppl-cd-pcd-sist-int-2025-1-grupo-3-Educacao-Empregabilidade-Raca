# Educação, Empregabilidade e Raça: O Que Os Dados Revelam.

O projeto visa o desenvolvimento de um sistema inteligente para análise das disparidades raciais no mercado de trabalho e sua relação com a formação educacional. Esse sistema é capaz de processar e integrar dados provenientes do CAGED e de bases específicas do mercado de trabalho, aplicando técnicas de ciência de dados e inteligência artificial para identificar padrões de desigualdade racial. A plataforma utiliza algoritmos de aprendizado de máquina para correlacionar fatores como raça/cor, nível educacional, setor de atuação e renda, permitindo a geração de insights automatizados sobre a inserção e progressão profissional da população negra no Brasil.

Além da análise descritiva, o sistema conta com funcionalidades, como previsões de impacto da educação na empregabilidade, identificação de grupos mais vulneráveis e recomendações de políticas públicas e estratégias empresariais voltadas à equidade racial. A interface é desenvolvida para gestores públicos, empresas, pesquisadores e organizações sociais, proporcionando um ambiente para visualização de dados e suporte à tomada de decisão baseada em evidências.

## Integrantes

* Alváro Felix da Silva.
* Ana Cecília Souza Lorens.
* Beatriz Azevedo dos Santos.
* Mariana Andrade.
* Sarah Mariana Guedes de Almeida.
  
## Professor

* Hugo Bastos de Paula.
* Hayala Nepomuceno Curto.

## Instruções de Instalação e Execução do Modelo de Machine Learning

Este documento descreve como instalar dependências, preparar o ambiente e executar corretamente o modelo desenvolvido para classificar vínculos formais e informais no mercado de trabalho.

---

## 1. Requisitos do Sistema

Antes de iniciar, verifique os seguintes pré-requisitos:

- Python 3.9 ou superior instalado (ou uso do Google Colab)
- Acesso à internet para instalação de bibliotecas
- Permissão para upload de arquivos no ambiente escolhido

---

## 2. Instalação de Dependências

Caso esteja executando localmente (Jupyter Notebook):

```bash
pip install pandas numpy seaborn matplotlib scikit-learn imbalanced-learn
```

Se estiver no **Google Colab**, execute também:

```python
!pip install -U imbalanced-learn
```

---

## 3. Upload da Base de Dados

O modelo foi construído sobre a base `base_final_combinada_kaggle_caged_corrigida_ok.csv`.

>  **Atenção:** É fundamental que a base siga este formato:

- Colunas `cor_raca` e `nivel_ensino` sem inconsistências (letras minúsculas, sem espaços extras);
- Coluna `vinculo_formal` com valores binários: `1` (formal) e `0` (não formal);
- Ausência de valores nulos (`NaN`);
- Nomes das colunas preservados conforme o código.

---

## 4. Pré-processamento Obrigatório

Se estiver usando uma base nova, execute o seguinte:

```python
df['cor_raca'] = df['cor_raca'].astype(str).str.lower().str.strip()
df['nivel_ensino'] = df['nivel_ensino'].astype(str).str.lower().str.strip()
df = df.dropna()
df = df[df['vinculo_formal'].isin([0, 1])]
```

Esse tratamento garante que os dados estejam compatíveis com o pipeline do modelo.

---

## 5. Execução do Modelo

Siga a ordem dos blocos de código conforme estruturado no notebook/colab:

1. Importação das bibliotecas
2. Leitura da base
3. Separação de variáveis `X` e `y`
4. Pré-processamento com `ColumnTransformer`
5. Split entre treino e teste (`train_test_split`)
6. Balanceamento com SMOTE
7. Treinamento com SVM + GridSearchCV
8. Avaliação com ajuste de limiar (F1-score)
9. Geração de matriz de confusão e curva ROC
10. Validação cruzada estratificada (opcional)

---

## 6. Resultados Esperados

O pipeline completo fornece:

- Métricas: Acurácia, Precisão, Recall, F1-Score
- Curva ROC e AUC
- Matriz de Confusão visual
- Melhor estratégia de SMOTE testada
- Melhor limiar para maximização do F1-score

---

## 7. Possíveis Problemas e Soluções

| Problema | Causa Comum | Solução |
|---------|--------------|---------|
| `ValueError: could not convert string to float` | Variável categórica não convertida | Utilize `OneHotEncoder` no `ColumnTransformer` |
| `ValueError: y contains NaN` | Variável alvo com valores ausentes | Aplique `dropna()` antes de treinar |
| Baixa performance no teste | Variável alvo desbalanceada ou dados ruidosos | Ajuste `sampling_strategy` no SMOTE e revise os atributos |

---

## 8. Salvamento do Modelo Treinado (Opcional)

Para reuso posterior do modelo já treinado:

```python
import joblib
joblib.dump(best_model, 'modelo_final_svm.pkl')
```

---

## Observações Finais

O código está correto e funcional, porém **a base original apresenta limitações estruturais** que impactam diretamente o desempenho do modelo. Recomendamos, sempre que possível, aprimorar a qualidade dos dados ou integrar novas fontes para melhorar a capacidade preditiva e a generalização do sistema.

---

**Desenvolvido para fins acadêmicos – PUC Minas – 2024.**

## Histórico de Versões

**0.3.0**  
CHANGE: Implementação e avaliação do segundo modelo — Support Vector Machine (SVM).  
- Aplicado balanceamento via SMOTE para tratar desbalanceamento.  
- Utilização de OneHotEncoder para variáveis categóricas.  
- Resultado: Acurácia de 73,56%.  

**0.2.1**  
CHANGE: Ajustes e melhorias no primeiro modelo — mudança para Random Forest Classifier.  
- Superou Decision Tree em AUC, alcançando 85,13%.  
- Realizada validação cruzada para garantir robustez.  

**0.1.1**  
CHANGE: Desenvolvimento inicial com Decision Tree Classifier.  
- Modelo baseline para análise exploratória.  
- Resultados limitados devido a alta variabilidade e desequilíbrio dos dados.  
- Identificado necessidade de tratamento de dados (balanceamento e codificação).

**0.1.0**  
FEATURE: Preparação dos dados.  
- Junção das bases CAGED 2023 e State of Data BR 2023.  
- Tratamento inicial: limpeza, padronização e definição das variáveis preditoras.  
- Mapeamento das categorias raciais e faixas salariais para análise segmentada.

**0.0.2**  
INIT: Coleta e inspeção das bases de dados.  
- Análise exploratória inicial para identificação de problemas
- Definição dos objetivos do projeto focados em empregabilidade e desigualdades raciais.

**0.0.1**
- Trabalhando na preparação dos dados.
