# Educação, Empregabilidade e Raça: O Que Os Dados Revelam.


**Álvaro Felix da Silva, alvaro.silva@sga.pucminas.br**

**Ana Cecília Souza Lorens, acslorens@sga.pucminas.br**

**Beatriz Azevedo dos Santos, beatriz.santos.1595043@sga.pucminas.br**

**Mariana Andrade Silva, mariana.andrade.1566766@sga.pucminas.br**

**Sarah Mariana Guedes de Almeida  sarah.almeida.1582677@sga.pucminas.br**

---

Professores:

**Prof. Hugo Bastos de Paula**
**Prof. Hayala Nepomuceno Curto.**

---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

_**Resumo**. Escrever aqui o resumo. O resumo deve contextualizar rapidamente o trabalho, descrever seu objetivo e, ao final, 
mostrar algum resultado relevante do trabalho (até 10 linhas)._

---


## Introdução

É nítido que o mercado de trabalho tecnológico brasileiro tem se destacado e evoluído de forma exponencial nos últimos anos. Diversas empresas têm adotado métodos e políticas de contratação inclusivas, mas, apesar disso, ainda existem muitos desafios enfrentados por pessoas não brancas em processos seletivos e no avanço de suas carreiras profissionais.

Nesse projeto, utilizamos dados que permitem entender quais fatores influenciam a contratação de profissionais negros, pardos e indígenas, e se existe uma diferença nos critérios de exigência, quando comparados aos candidatos brancos.

O estudo é importante para compreender padrões de contratação dentro do mercado de trabalho tecnológico, e identificar possíveis desigualdades raciais existentes nesse meio. Entender tais padrões pode auxiliar tanto os candidatos a compreenderem o estado atual do mercado, bem como empresas a proporem melhorias mais abrangentes em seus processos seletivos, fomentando a diversidade nesse campo profissional.

###    Contextualização

O setor de tecnologia no Brasil ocupa um papel central no desenvolvimento econômico e na geração de oportunidades. No entanto, esse crescimento não se distribui de forma equitativa. A presença reduzida de pessoas não brancas em cargos estratégicos ou de alta remuneração aponta para barreiras estruturais que limitam o acesso a essas posições.

Dentre os principais entraves está o acesso desigual à formação superior de qualidade. Mesmo com a expansão das vagas, muitos grupos raciais continuam sub-representados em áreas técnicas e de liderança. Para entender essa dinâmica, o projeto utilizará bases de dados como o CAGED (Ministério do Trabalho) e a pesquisa State of Data 2023, com o intuito de *classificar grupos e perfis a partir de seus atributos demográficos e profissionais*.

A base do CAGED, por sua natureza abrangente e oficial, possibilita análises mais detalhadas de vínculos formais de trabalho — como salário, setor (CNAE), cargo (CBO), tipo de admissão, entre outros. Já a base State of Data traz variáveis autorreportadas, complementando o cenário com dados sobre trajetória, experiência e percepção de mercado.

A proposta, portanto, é *treinar modelos que classifiquem os indivíduos em diferentes categorias de inserção ou progressão profissional*, com base nos dados disponíveis. Essa classificação permitirá revelar padrões ocultos e estruturar debates mais objetivos sobre a equidade racial no setor.


###    Problema

O propósito do projeto é responder o seguinte problema orientado a dados: “Com base em atributos de formação e experiência profissional, quais fatores estão associados à maior presença de pessoas pretas, pardas, amarelas ou indígenas em posições formais com melhores condições no mercado de trabalho, em comparação aos candidatos brancos?” 


###    Objetivo geral

O objetivo do projeto é analisar e comparar possíveis padrões presentes na formação superior que diferem entre pessoas brancas e pessoas pretas, pardas, amarelas ou indígenas, ao serem inseridas no mercado de trabalho tecnológico.

####    Objetivos específicos

- Desenvolver um sistema capaz de comparar e analisar padrões nos atributos selecionados das bases de dados do CAGED e do State of Data 2023, e avaliar possíveis desigualdades presentes no mercado de trabalho, comparando a jornada de trabalho e a educação superior de pessoas brancas e não brancas, disponibilizando estatísticas por meio de gráficos e tabelas;
- Possibilitar que o leitor consiga ler e entender quais são os fatores que podem impactar sua inserção profissional;
- Além disso, fazer com que o sistema proporcione sugestões que auxiliem profissionais, empresas e gestores a tomar decisões relacionadas ao mercado de trabalho tecnológico, melhorando a diversidade em tal âmbito profissional.

###    Justificativas

A inserção de populações racializadas no mercado de trabalho ainda é marcada por desigualdades. Estudos apontam que os mesmos enfrentam barreiras como menores salários, sub-representação em cargos de liderança e maior informalidade. Além disso, a relação entre educação e mercado de trabalho não se dá de maneira homogênea entre diferentes grupos raciais, o que reforça a necessidade de uma análise aprofundada sobre o tema.

Por meio do uso de dados quantitativos e técnicas de ciência de dados, este estudo fornece um embasamento empírico para a formulação de políticas públicas e estratégias empresariais voltadas à promoção da equidade racial. A integração de bases de dados da tabela do CAGED e State of Data 2023 com informações específicas sobre o mercado de trabalho permite um diagnóstico mais preciso das desigualdades, contribuindo para a construção de soluções eficazes.



##    Público alvo

Os resultados do projeto são de interesse para setores como:
- **Gestores Públicos ou de Educação**: Para embasar políticas de inclusão racial no mercado de trabalho e na educação.
- **Empresas e Setor Privado**: Para apoiar estratégias de diversidade e inclusão em ambientes corporativos.
- **Profissionais da área de Tecnologia**: Para aprofundar estudos sobre desigualdade racial e suas relações com a educação e o emprego.

O projeto fornece um panorama quantitativo e qualitativo sobre as disparidades raciais no mercado de trabalho tecnológico e sua relação com a formação educacional superior, destacando a importância de políticas e ações afirmativas que promovam oportunidades mais igualitárias para toda a diversidade racial do Brasil.

## Análise exploratórida dos dados

###    Dicionário de dados

`Base de dados principal Kaggle-2023`

| Atributo | Nome              | Tipo de Dado  | Subtipo de Dado    | Descrição                                                                 |
|----------|-------------------|----------------|---------------------|---------------------------------------------------------------------------|
| P1_a     | idade             | Quantitativo   | Contínuo            | Idade da pessoa (em anos).                                               |
| P1_b     | genero            | Qualitativo    | Nominal             | Gênero da pessoa (masculino, feminino, não binário, etc.).               |
| P1_c     | cor_raca          | Qualitativo    | Nominal             | Cor/raça/etnia da pessoa (branca, negra, parda, indígena, asiática, etc.).|
| P1_l     | nivel_ensino      | Qualitativo    | Ordinal             | Nível de ensino da pessoa (Ensino Médio, Superior, Pós-graduação, etc.). |
| P2_a     | situacao_trabalho | Qualitativo    | Nominal             | Situação atual de trabalho (empregado, desempregado, estagiário, etc.).  |
| P2_h     | faixa_salarial    | Quantitativo   | Contínuo            | Faixa salarial anual ou mensal (R$ 3.000, R$ 5.000, etc.).               |


A tabela da base principal apresenta atributos relacionados ao perfil sociodemográfico e profissional de indivíduos, incluindo gênero, cor/raça, nível de ensino e área de formação. Além disso, investiga a percepção de impacto da identidade na experiência profissional e traz informações sobre situação de trabalho, setor de atuação, senioridade, faixa salarial e tempo de experiência na área de dados e TI. Esses dados permitem uma análise sobre diversidade e desigualdade no mercado de trabalho.

`Base de dados segundária CAGED-2023`

| Atributo | Tipo de dado  | Subtipo de dado          | Descrição                                                                 |
|----------|----------------|---------------------------|---------------------------------------------------------------------------|
| A1       | Qualitativo     | Nominal                   | Região geográfica onde a pessoa reside ou trabalha.                      |
| B1       | Qualitativo     | Nominal                   | Sessão ou departamento vinculado ao indivíduo.                           |
| C1       | Qualitativo     | Nominal                   | Subclasse específica dentro de uma categoria maior.                      |
| D1       | Qualitativo     | Nominal                   | Categoria profissional ou ocupacional do indivíduo.                      |
| E1       | Qualitativo     | Ordinal                   | Nível de escolaridade atingido pelo indivíduo.                           |
| F1       | Quantitativo    | Discreto                  | Idade da pessoa, expressa em anos.                                       |
| G1       | Quantitativo    | Discreto                  | Quantidade de horas contratuais de trabalho por semana.                  |
| H1       | Qualitativo     | Nominal                   | Identificação de raça/cor com base em categorias pré-definidas.          |
| I1       | Qualitativo     | Nominal                   | Sexo do indivíduo (exemplo: Masculino, Feminino, Outro).                 |
| J1       | Quantitativo    | Contínuo                  | Valor do salário recebido pelo indivíduo.                                |
| K1       | Qualitativo     | Nominal                   | Código que representa a unidade do salário (exemplo: mensal, anual).     |
| L1       | Quantitativo    | Contínuo                  | Valor fixo do salário, sem incluir adicionais ou variáveis.              |


A tabela apresenta atributos relacionados ao perfil profissional e trabalhista de indivíduos, incluindo região, categoria profissional, grau de instrução e idade. Além disso, traz informações sobre carga horária contratual, raça/cor, sexo e salário, incluindo a unidade de pagamento e o valor fixo recebido. Esses dados permitem análises sobre padrões salariais, diversidade e condições de trabalho em diferentes setores. 


###    Descrição de dados

A integração das bases **Kaggle 2023** e **CAGED 2023**:  

**Análise Gráfica Kaggle**

![Gráfico 1](imagens/state_grafico_1.png)

![Gráfico 2](imagens/state_grafico_2.png)

![Gráfico 3](imagens/state_grafico_3.png)

#### Relatório Exploratória - Educação
##### 1. Distribuição de Pessoas com Doutorado por Gênero e Cor/Raça
Analisa a representatividade de gênero e raça entre indivíduos com doutorado.

![Gráfico 1](https://drive.google.com/uc?export=view&id=1HB3HYRV7MrdjNHs7zrh1An4bgFyT9ne2)

##### 2. Nível de Ensino por Área de Formação
Mapeia a distribuição de profissionais em diferentes estágios educacionais (da graduação ao doutorado) por área do conhecimento.

![Gráfico 2](https://drive.google.com/uc?export=view&id=10F5vZqSEMlZl_qJAGmPGsyATYWpo_S53)

##### 3. Número de Pessoas com Doutorado em Tecnologia por Gênero e Cor/Raça
Avalia a diversidade em Tecnologia, focado no nível de doutorado.

![Gráfico 3](https://drive.google.com/uc?export=view&id=1KVzQf07dQ_ds5j6hhuAmcAlXuYrqMnBa)

##### 4. Número de Pessoas com Pós-Graduação por Área de Formação
Identifica quais áreas do conhecimento atraem mais especialistas.

![Gráfico 4](https://drive.google.com/uc?export=view&id=1ZSa3msbyJARB9M0rfxXtydHv62a4mDFS)

##### 5. Número de Pessoas Empregadas e Desempregadas na Área de Formação de Computação / Engenharia de Software / Sistemas de Informação/ TI
Mede a empregabilidade de formados em tecnologia e seus status profissionais.

![Gráfico 5](https://drive.google.com/uc?export=view&id=13imyTWcirlwSc8U1-VXKch9766f88hAJ)

##### 6. Número de Pessoas Pretas por Nível de Ensino
Avalia o acesso da população negra a cada etapa da educação formal.

![Gráfico 6](https://drive.google.com/uc?export=view&id=1NegHG6T4CxhfmoFR70n47Iarr_WrCS_m)

##### 7. Pessoas com Graduação/Bacharelado e Seus Setores de Atuação
Mapeia onde os graduados estão inseridos no mercado de trabalho.

![Gráfico 7](https://drive.google.com/uc?export=view&id=14Rdkofd0zqHbdNq7bA4lRWOFClywJKlC)



**Análise Gráfica CAGED**

![Gráfico 1](imagens/panorama_grafico_1.png)

![Gráfico 2](imagens/panorama_grafico_2.png)

![Gráfico 3](imagens/panorama_grafico_3.png)

![Gráfico 4](imagens/panorama_grafico_4.png)

(Importante mencionar que a partir do gráfico blot spot identificamos na nossa base de dados a existência de outliers que poderiam comprometer o comportamento do nosso modelo, motivo pelo qual, a partir desta percepção, restou necessária a realização de remoção dos outliers ainda existentes após a primeira limpeza da base de dados.)


#### Relatório Exploratória - Empregabilidade e Faixa Salarial (CAGED)
![Gráfico de empregabilidade por raça/cor](https://i.imgur.com/u6oixye.png)
![Gráfico de empregabilidade por grau](https://i.imgur.com/kcvTaDt.png)
![Gráfico de faixa salarial](https://i.imgur.com/uoyfwdu.png)
Mostra a quantidade de registros(pessoas) para determinada faixa salarial.
![Gráfico de empregabilidade por faixa salarial](https://i.imgur.com/KdlQqJ4.png)
![Gráfico de faixa salarial por grau de instrução](https://i.imgur.com/J5ZX9cF.png)
![Gráfico de faixa salarial por cor/raça](https://i.imgur.com/rlfALZA.png)
Mostra a quantidade de pessoas de determinada cor/raça para cada faixa salarial.
![Gráfico de Distribuição de salário por raça/cor](https://i.imgur.com/Vvx2eoP.png)

#### Relatório Exploratória - Empregabilidade e Faixa Salarial (STATE OF DATA 2023)
![Gráfico empregabilidade e faixa salarial](https://i.imgur.com/hOQCEAe.png)
Mostra a faixa salarial dos tipos de empregados analisados no projeto.
![Gráfico empregabilidade e raça/cor](https://i.imgur.com/qFnYLZO.png)
Mostra a distribuição de empregados(e o tipo) para cada cor/raça analisada no projeto.


## Preparação dos dados
### Definição do Tema e Seleção Inicial de Variáveis

A escolha do tema do projeto foi orientada por dados obtidos a partir de uma base do Kaggle, com foco em recortes sociodemográficos e trajetórias profissionais no contexto do mercado de trabalho. A seleção inicial de colunas relevantes foi fundamentada em atributos que permitissem examinar questões de desigualdade, inserção e mobilidade profissional, com ênfase na interseccionalidade entre raça/cor e características formativas.

Paralelamente, iniciou-se uma busca por fontes secundárias que possibilitassem o enriquecimento da base principal. Nesse momento, os dados do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) foram considerados como potencial base complementar. Essa base continha informações sobre matrículas, instituições e cursos de ensino superior.

### Desafios de Integração com o INEP

A tentativa de integração da base do INEP à base principal revelou limitações técnicas e estruturais. A principal dificuldade se deu devido à falta de chaves de junção compatíveis — os atributos do INEP não possuíam colunas diretamente associáveis a indivíduos ou agrupamentos presentes na base do Kaggle.

Além disso, o elevado volume de dados do INEP, associado ao seu formato extensivo e necessidade de tratamento adicional, comprometeu a viabilidade computacional de realizar análises integradas. Diante dessas barreiras, optou-se pela reformulação da estratégia de enriquecimento de dados.

### Escolha da Base CAGED-2023 como Fonte Complementar

Como alternativa, foi selecionada a base CAGED 2023, de responsabilidade do Ministério do Trabalho, por sua natureza oficial e abrangência nacional. Essa base oferece registros administrativos sobre vínculos empregatícios formais e contempla atributos como: salário, horas contratuais, grau de instrução, classificação ocupacional e localização geográfica.

A etapa seguinte consistiu na curadoria das variáveis que seriam extraídas da base CAGED com a finalidade de enriquecer a base principal. Essa seleção foi orientada pelo objetivo analítico de ampliar a profundidade do estudo, adicionando informações robustas sobre a realidade contratual dos indivíduos. Foram priorizados atributos que permitissem analisar padrão salarial, categoria profissional e características de jornada.

### Definição de Chave Estrangeira e Estratégia de Fusão

A fim de garantir integridade referencial na junção entre as bases, foi definida uma chave composta pelos seguintes campos: `idade`, `genero`, `cor_raca` e `nivel_ensino`. Essa chave estrangeira possibilitou realizar a fusão das bases via `left join`, com a base Kaggle assumida como principal.

A estratégia adotada priorizou a preservação de todos os registros da base principal, com a base CAGED atuando como complementar, contribuindo apenas quando havia correspondência nas chaves.

### Visualização e Descrição Exploratória dos Dados

Com as bases organizadas e fundidas, iniciou-se a etapa de análise exploratória com a geração de gráficos descritivos. A construção de visualizações envolveu a interrelação de variáveis-chave — como raça/cor, faixa salarial, grau de instrução e jornada contratual — por meio de histogramas, boxplots e gráficos de contagem.

Essas representações permitiram a identificação de padrões estruturais e disparidades raciais, além de fornecerem suporte visual à leitura crítica dos dados.

A análise gráfica também contribuiu para a formulação de hipóteses relacionadas à mobilidade profissional e à concentração de determinados grupos em faixas salariais específicas, indicando dinâmicas relevantes do mercado de trabalho e potenciais zonas de exclusão.

### Contraste entre Fontes e Contribuição Analítica

A base Kaggle se destacou por fornecer dados subjetivos, relacionados à percepção de discriminação, status profissional atual e experiência de trabalho. Já o CAGED agregou elementos objetivos e administrativos, permitindo o contraste entre discurso e realidade formal.

A fusão dessas fontes ampliou a capacidade interpretativa da pesquisa, ao permitir análises que vão além dos registros institucionais e contemplam também a dimensão vivencial dos respondentes.

Essa complementaridade entre percepções individuais e dados oficiais fortaleceu a abordagem metodológica do estudo, viabilizando uma análise mais confiável e multidimensional das desigualdades e oportunidades no mercado de trabalho brasileiro.

---

### Limpeza e Tratamento das Bases

#### 1.1 Kaggle

- A coluna `situacao_trabalho` havia sido transformada incorretamente, apresentando apenas um valor fixo.
- A base original foi reimportada para restaurar os valores textuais originais.
- Aplicou-se um mapeamento categórico associando valores numéricos às situações de trabalho.
- Colunas como `idade`, `genero`, `cor_raca` e `nivel_ensino` foram renomeadas e padronizadas.
- Valores ausentes foram substituídos por `-1` com `.fillna()`.
- Outliers foram removidos com base no método do intervalo interquartil (IQR).

#### 1.2 CAGED

- As colunas `graudeinstrução`, `raçacor` e `sexo` foram renomeadas para `nivel_ensino`, `cor_raca` e `genero`.
- As colunas de interesse foram reorganizadas e padronizadas.
- As variáveis para junção foram convertidas para o tipo `int` para garantir integridade nas chaves.

### Combinação das Bases

- A base Kaggle foi usada como principal.
- A junção com a base CAGED foi feita via `left join`, pelas chaves: `idade`, `genero`, `cor_raca`, `nivel_ensino`.
- Registros da Kaggle foram mantidos integralmente, enquanto o CAGED complementou as informações.

### Criação da Variável Alvo

- Criada a variável `vinculo_formal`, com valor **1** para "Empregado (CLT)" e "Servidor Público" (códigos 1 e 3), e **0** para os demais.
- Representa a inserção formal no mercado de trabalho.

### Modelagem

- Preparação dos dados:
  - A variável `situacao_trabalho` foi removida para evitar vazamento de informação.
  - Categóricas codificadas com `LabelEncoder`.
- Balanceamento com **SMOTE**.
- Divisão dos dados: **80% treino** e **20% teste**.
- Treinamento de modelo de **Árvore de Decisão** com profundidade máxima **5**.

### Avaliação do Modelo
- Visualização da matriz de confusão com `seaborn`.
- Exportação da árvore de decisão como imagem de alta resolução (40x20 polegadas, 300 DPI)

## Indução de modelos

### Modelo 1: Árvore de Decisão

Escolha do Algoritmo:
O algoritmo escolhido foi o de Árvore de Decisão (Decision Tree Classifier). Esta escolha se justifica por se tratar de um modelo interpretável e explicável, especialmente adequado para problemas de classificação binária como o proposto neste projeto: prever a existência ou não de vínculo formal de trabalho com base em atributos sociodemográficos e de formação profissional. Árvores de decisão permitem visualização clara das regras de decisão, tornando o modelo acessível até mesmo para públicos não técnicos.


Seleção de atributos e separação dos dados:
Na etapa de preparação dos dados, a variável-alvo definida foi vinculo_formal, representando a classificação binária entre vínculos formais e não formais de trabalho. As variáveis preditoras (X) foram obtidas a partir da exclusão de vinculo_formal e situacao_trabalho, sendo esta última removida para evitar data leakage, dado seu potencial de correlação direta com a variável-alvo.

As variáveis categóricas presentes em X foram identificadas automaticamente com base em seu tipo (object) e, em seguida, transformadas via codificação One-Hot Encoding utilizando o OneHotEncoder do sklearn, com os parâmetros sparse_output=False e handle_unknown='ignore'. Esse processo gerou colunas binárias para cada categoria observada nas variáveis categóricas, convertendo o conjunto de dados para um formato totalmente numérico, compatível com os algoritmos de machine learning.

Não foi realizada uma etapa explícita de seleção de atributos (feature selection) neste pipeline. Em vez disso, todos os atributos numéricos (originais e codificados) foram mantidos no modelo. A escolha do classificador Random Forest se justifica, em parte, por sua robustez diante de um grande número de variáveis, bem como sua capacidade de estimar automaticamente a importância relativa de cada atributo durante o processo de treinamento, utilizando critérios como a redução da impureza (Gini ou entropia) em cada nó da árvore.

Amostragem de Dados:
O conjunto de dados foi balanceado utilizando a técnica de oversampling SMOTE (Synthetic Minority Over-sampling Technique) para corrigir o desequilíbrio entre as classes "formal" e "não formal". Em seguida, os dados foram divididos em conjunto de treino (80%) e teste (20%) utilizando a função `train_test_split` da biblioteca scikit-learn. A base balanceada foi dividida em 80% para treino e 20% para teste, totalizando:
- 7.500 registros após o balanceamento com SMOTE
- 6.000 registros no conjunto de treino
- 1.500 registros no conjunto de teste

Parâmetros do Modelo:
- `max_depth=5` — limite de profundidade para evitar overfitting e facilitar interpretação visual.
- `random_state=42` — garante reprodutibilidade.
- Critério padrão de divisão: índice Gini (implícito no scikit-learn).

Trechos do Código Comentado:
```
python

# Aplicação do SMOTE para balanceamento
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Treinamento do modelo
modelo = DecisionTreeClassifier(max_depth=5, random_state=42)
modelo.fit(X_train, y_train)

# Predição
y_pred = modelo.predict(X_test)
```
Ferramentas Gráficas:
Foram utilizados:
- `plot_tree` para visualização gráfica da árvore de decisão
- `seaborn.heatmap` para a matriz de confusão
- `matplotlib` para ajuste de layout e exportação da imagem em alta resolução

# Modelo 1 – Random Forest (Versão Final)

Este relatório descreve detalhadamente a construção, otimização, análise e interpretação do primeiro modelo de classificação utilizado para prever o vínculo formal no mercado de trabalho com base em dados combinados da pesquisa (Kaggle) e do sistema CAGED 2023. A técnica de Random Forest foi adotada por sua robustez, interpretabilidade e bom desempenho preditivo.

---

## Etapa 1: Instalação da Biblioteca

Antes de começar a aplicação das técnicas de balanceamento, é necessário instalar bibliotecas adicionais que não fazem parte da instalação padrão do Python.

```bash
!pip install imbalanced-learn
```

Essa linha instala a biblioteca imbalanced-learn, que inclui ferramentas como SMOTE e ADASYN, utilizadas para balanceamento de classes desiguais na variável alvo.

## Etapa 2: Importações

Nesta etapa, são carregadas todas as bibliotecas necessárias para manipulação, visualização de dados, modelagem preditiva e avaliação de desempenho do modelo.

Importações principais:
- pandas, numpy: manipulação e estruturação de dados
- sklearn: ferramentas de modelagem, validação e métricas
- SMOTE, ADASYN: técnicas para balancear dados desbalanceados
- matplotlib, seaborn: bibliotecas de visualização gráfica
- io, files: suporte ao carregamento de arquivos no Google Colab

## Etapa 3: Upload da Base de Dados

Nesta etapa, a base final combinada e tratada foi carregada no ambiente.

**Arquivo utilizado:**
`base_final_combinada_kaggle_caged_corrigida_ok.csv`

Essa base contém dados de respondentes da pesquisa combinados com atributos do sistema CAGED, incluindo dados sociodemográficos, profissionais e histórico de vínculos empregatícios.

## Etapa 4: Tratamento de Valores Ausentes

Como parte da limpeza dos dados, os valores nulos foram substituídos por -1 para evitar falhas na execução do modelo.

```python
df = df.fillna(-1)
```

## Etapa 5: Separação das Variáveis X e y

A separação entre X e y define quais atributos serão usados como preditores e qual será a variável alvo.

```python
X = df.drop(columns=['vinculo_formal', 'situacao_trabalho'])
y = df['vinculo_formal']
```

X inclui todas as variáveis independentes (ex: idade, raça, escolaridade, faixa salarial, forma de contratação, entre outras variáveis sociodemográficas e profissionais).

y representa a variável que queremos prever: `vinculo_formal`, sendo:
- 1 para indivíduo com vínculo formal
- 0 para indivíduo sem vínculo formal

A variável `situacao_trabalho`, por ser derivada diretamente de `vinculo_formal`, foi removida para evitar vazamento de dados no modelo.

## Etapa 6: Codificação de Variáveis Categóricas

As colunas com valores textuais (como “sexo”, “escolaridade”, “região”) foram transformadas em valores numéricos por meio de LabelEncoder, garantindo compatibilidade com algoritmos de machine learning.

## Etapa 7: Balanceamento das Classes

Para evitar que o modelo aprenda de forma enviesada devido ao desbalanceamento entre as classes "com vínculo" e "sem vínculo", foram aplicadas técnicas de oversampling.

### 7.1 - Verificação da Distribuição Original

Antes de aplicar o SMOTE, foi verificada a proporção das classes. Observou-se um número significativamente maior de pessoas com vínculo formal.

### 7.2 - Aplicação do SMOTE

```python
X_res, y_res = sm.fit_resample(X, y)
```

O SMOTE (Synthetic Minority Oversampling Technique) cria novos exemplos sintéticos da classe minoritária para balancear a base, sem apenas replicar os existentes.

### 7.3 - Verificação da Distribuição Após SMOTE

Confirmou-se a uniformização das classes: 50% formal e 50% não formal.

### 7.4 - Alternativa com ADASYN

Foi também aplicada a técnica ADASYN, que gera dados sintéticos com foco em regiões de maior complexidade de decisão. Apesar disso, a versão final do modelo foi induzida com SMOTE, que apresentou melhor equilíbrio visual e desempenho.

## Modelo Final: Random Forest com Otimização

O modelo final foi construído com o algoritmo Random Forest, que combina várias árvores de decisão para melhorar a precisão e reduzir o risco de overfitting.

Foi utilizado o RandomizedSearchCV para otimização automática dos seguintes hiperparâmetros:
- n_estimators
- max_depth
- min_samples_split
- max_features
- bootstrap

Essa etapa garantiu que o modelo tivesse o melhor desempenho possível dentro das combinações testadas.

## Resultados do Modelo Final

Esta seção apresenta os resultados quantitativos do modelo treinado com SMOTE e Random Forest.

| Métrica              | Valor   |
|----------------------|---------|
| Acurácia (treino)    | 99,28%  |
| Acurácia (teste)     | 87,27%  |
| F1-score médio       | 0,87    |

Esses resultados demonstram um excelente desempenho do modelo. A diferença entre treino e teste indica que, embora o modelo memorize bem os dados de treino, ainda generaliza satisfatoriamente para dados novos.

## Métricas Detalhadas (Base de Teste)

A tabela a seguir apresenta as principais métricas de avaliação para as duas classes previstas:

| Classe       | Precisão | Revocação | F1-score | Suporte |
|--------------|----------|-----------|----------|---------|
| Não Formal   | 0.92     | 0.82      | 0.87     | 748     |
| Formal       | 0.84     | 0.93      | 0.88     | 752     |
| Acurácia     | -        | -         | 0.8727   | 1500    |

As métricas indicam que o modelo está bem balanceado entre as classes, com uma leve tendência a prever corretamente vínculos formais. Ambos os grupos têm valores de precisão e recall acima de 80%, o que mostra qualidade preditiva em diferentes perfis de trabalhadores.

## Matriz de Confusão

A matriz de confusão detalha os acertos e erros cometidos pelo modelo na base de teste.

|                       | Previsto: Não Formal | Previsto: Formal |
|-----------------------|----------------------|------------------|
| Real: Não Formal      | 6581                 | 1783             |
| Real: Formal          | 2335                 | 6391             |

- VP (Formal corretamente previsto): 6391
- VN (Não Formal corretamente previsto): 6581
- FP (Formal previsto incorretamente): 1783
- FN (Não Formal previsto incorretamente): 2335

## Interpretação do Modelo

### Atributos Mais Importantes

A partir da função `feature_importances_`, foram destacados os seguintes atributos como mais relevantes para a decisão do modelo:
- Faixa Salarial
- Idade
- Participação em Entrevistas
- Critérios para Escolher onde Trabalhar
- Grau de Insatisfação no Trabalho

Estes atributos têm alta correlação com vínculos empregatícios formais, refletindo aspectos econômicos, comportamentais e estruturais da realidade brasileira.

### Regras da Primeira Árvore

Exemplos de raciocínio extraído da primeira árvore da floresta:
- Se faixa salarial é baixa e idade jovem, o modelo tende a classificar como “Não Formal”.
- Se a faixa salarial é alta, a idade é média e houve participação recente em entrevistas, tende a prever como “Formal”.

## Conclusão

O modelo final, baseado em Random Forest e treinado com dados balanceados via SMOTE, demonstrou-se altamente eficaz para o propósito de prever a existência de vínculo formal com base em atributos sociodemográficos e profissionais.

A precisão e estabilidade do modelo o tornam aplicável em contextos reais, como diagnósticos institucionais, políticas públicas de empregabilidade ou ferramentas preditivas em processos seletivos. A utilização de técnicas como codificação de variáveis, otimização de hiperparâmetros e balanceamento supervisionado contribuiu significativamente para sua robustez.

Além de sua performance preditiva, o modelo oferece boa interpretabilidade, evidenciada pelas regras geradas pelas árvores e pelo destaque de variáveis coerentes com a realidade do mercado de trabalho. Isso o qualifica tanto para uso técnico quanto estratégico.

# Modelo 2 : Algoritmo
Nesta fase, foi utilizado o modelo SVM (Support Vector Machine) com kernel
RBF, escolhido pelas seguintes razões:
• É um modelo eficaz para problemas de classificação binária.
• Tem bom desempenho em bases com margens de separação entre as
classes.
• Suporta bem dados que não são linearmente separáveis, como os da
base em questão.

### Resultados obtidos com o modelo 2.
**Base de Treinamento**
O modelo foi treinado com dados balanceados via SMOTE, ajustando a proporção da classe minoritária ("sem vínculo") para 1:2 em relação à classe majoritária ("com vínculo"). Esse balanceamento foi essencial para evitar que o modelo aprendesse apenas os padrões da classe mais frequente.

- Acurácia no conjunto de treinamento: 68,08%
- Apesar de ter sido treinado em uma base balanceada, o modelo não atingiu uma acurácia extremamente alta, o que é esperado em SVMs com kernel RBF, já que o foco é minimizar erros de classificação próximos à margem de decisão. Isso também pode indicar que o modelo não está sofrendo overfitting.

**Base de Teste**
- O modelo foi avaliado em uma base original não balanceada, representando um cenário realista. Para melhorar a performance, foi feito um ajuste dinâmico do limiar de decisão, resultando no valor ideal de:
- Melhor limiar de decisão: 0.53
- Acurácia no conjunto de teste: 73,56%
- Esse ajuste permitiu que o modelo mantivesse uma acurácia estável dentro da faixa desejada (70%–80%), mesmo com desequilíbrio nas classes.

**Relatório de Classificação**
| Classe          | Precisão | Revocação | F1-score | Suporte |
|-----------------|----------|-----------|----------|---------|
| Sem vínculo (0) | 0.64     | 0.10      | 0.17     | 366     |
| Com vínculo (1) | 0.74     | 0.98      | 0.84     | 958     |

- Precisão média ponderada: 0.71
- F1-score médio ponderado: 0.66
- Média macro (mais equilibrada): F1 = 0.51

 Interpretação:
- O modelo teve excelente desempenho para a classe "com vínculo", com recall de 98%. Porém, teve baixa capacidade de identificar corretamente a classe "sem vínculo", com apenas 10% de recall. 
Isso revela que, mesmo com SMOTE e ajuste de limiar, a classe minoritária ainda é um desafio, o que é comum em problemas desbalanceados.

**Ajuste de Hiperparâmetros**
- O GridSearchCV foi aplicado para refinar os parâmetros do SVM, resultando na seguinte combinação ideal:
| C = 50 |
| Kernel = RBF |
- Essa configuração ajuda a equilibrar a flexibilidade do modelo e sua penalização para erros, reforçando sua capacidade de aprendizado não linear.

Matriz de Confusão:

A matriz de confusão obtida apresentou a seguinte distribuição entre as classes previstas e reais:
![Matriz de Confusao 2](https://drive.google.com/uc?export=view&id=1DHbdfUXd39IjKNNXVcpXR6UYp-c7shsc)

Medidas de Performance:
- Acurácia: 72,89%  
- Precisão: 73,71%  
- Revocação (Recall): 96,06%  
- F1-score: 83,47%

Os resultados demonstram que o modelo teve um bom desempenho geral, com alta revocação, o que indica que ele é eficiente em identificar os casos "Com vínculo". Porém, a baixa taxa de verdadeiros negativos (62 de 384) e o número grande de falsos positivos (322) sugerem que o modelo tem dificuldades em reconhecer corretamente os casos "Sem vínculo". Tal comportamento pode se dar por um desequilíbrio entre as classes na base de dados, favorecendo a classe majoritária.

**Conclusão Parcial:**
 O modelo SVM, com kernel RBF, apresentou desempenho estável e razoável, atingindo 73,56% de acurácia na base de teste. No entanto, sua performance para a classe minoritária ("sem vínculo") ainda foi limitada, mesmo após técnicas como SMOTE e ajuste de limiar.
Recomenda-se:
- Monitorar a estabilidade do modelo com múltiplas execuções
devido à ausência de random_state. 
- Explorar algoritmos alternativos (e.g., Random Forest ou XGBoost) para comparação. 
- Coletar mais dados ou features para melhorar a discriminação entre classes, caso necessário.


### Interpretação do modelo 2

Atributos mais importantes
Como o modelo SVM não fornece importância direta dos atributos como uma árvore de decisão, usamos a interpretação com base nas variáveis utilizadas e seus efeitos observados nos resultados:
- Idade
- Nível de Ensino
- Cor/Raça

**Tendências identificadas pelo modelo:**

- Idade mais alta e nível de ensino elevado → maior tendência a vínculo formal.
- Cor/Raça (pretos, pardos, indígenas e amarelos) apresenta influência, mas com possíveis desigualdades detectadas na revocação (modelo acerta mais para quem já tem vínculo). 
A classe com vínculo formal (1) foi muito melhor identificada que a classe sem vínculo (0), indicando tendência do modelo a prever vínculo formal na maioria dos casos.

**Comportamento do modelo:**

- Quando há perfil mais jovem com menor escolaridade, o modelo tem dificuldade em classificar como "sem vínculo", mesmo que isso seja verdadeiro.
- Quando o perfil tem escolaridade mais alta, a chance de previsão correta como "com vínculo" aumenta bastante.
- O modelo, mesmo com SMOTE, ainda tende a favorecer a classe majoritária (com vínculo), o que deve ser considerado em aplicações práticas.

## Análise comparativa dos modelos

Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.


### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.


## 8. Conclusão

Apresente aqui a conclusão do seu trabalho. Discussão dos resultados obtidos no trabalho, 
onde se verifica as observações pessoais de cada aluno.

Uma conclusão deve ter 3 partes:

   * Breve resumo do que foi desenvolvido
	 * Apresenação geral dos resultados obtidos com discussão das vantagens e desvantagens do sistema inteligente
	 * Limitações e possibilidades de melhoria


# REFERÊNCIAS

Como um projeto de sistema inteligente não requer revisão bibliográfica, 
a inclusão das referências não é obrigatória. No entanto, caso você 
tenha utilizado referências na introdução ou deseje 
incluir referências relacionadas às tecnologias, padrões, ou metodologias 
que serão usadas no seu trabalho, relacione-as de acordo com a ABNT.

Verifique no link abaixo como devem ser as referências no padrão ABNT:

http://www.pucminas.br/imagedb/documento/DOC\_DSC\_NOME\_ARQUI20160217102425.pdf

Por exemplo:

**[1]** - _ELMASRI, Ramez; NAVATHE, Sham. **Sistemas de banco de dados**. 7. ed. São Paulo: Pearson, c2019. E-book. ISBN 9788543025001._

**[2]** - _COPPIN, Ben. **Inteligência artificial**. Rio de Janeiro, RJ: LTC, c2010. E-book. ISBN 978-85-216-2936-8._

**[3]** - _CORMEN, Thomas H. et al. **Algoritmos: teoria e prática**. Rio de Janeiro, RJ: Elsevier, Campus, c2012. xvi, 926 p. ISBN 9788535236996._

**[4]** - _SUTHERLAND, Jeffrey Victor. **Scrum: a arte de fazer o dobro do trabalho na metade do tempo**. 2. ed. rev. São Paulo, SP: Leya, 2016. 236, [4] p. ISBN 9788544104514._

**[5]** - _RUSSELL, Stuart J.; NORVIG, Peter. **Inteligência artificial**. Rio de Janeiro: Elsevier, c2013. xxi, 988 p. ISBN 9788535237016._



# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




