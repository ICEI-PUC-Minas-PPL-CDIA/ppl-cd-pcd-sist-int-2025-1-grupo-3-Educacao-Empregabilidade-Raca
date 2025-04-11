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

O setor de tecnologia no Brasil, em constante expansão, representa um fator crucial para o desenvolvimento econômico e social do país. No entanto, esse crescimento não se traduz em oportunidades equitativas para todos. As desigualdades raciais, profundamente enraizadas na história brasileira, persistem e se manifestam de forma alarmante nessa área.

Uma das principais barreiras enfrentadas está no acesso à educação superior de qualidade. Apesar da crescente demanda por profissionais qualificados, a baixa representação de pessoas pretas, pardas, amarelas e indígenas em cargos de liderança e em áreas de alta remuneração é evidente. Tal desigualdade não apenas limita o potencial individual, mas também restringe a capacidade de inovação e a diversidade de perspectivas no setor tecnológico.

Para compreender essa disparidade, este projeto utilizará bases de dados secundárias, como o CAGED, administrado pelo Ministério do Trabalho e Emprego. Diferente de bancos de dados baseados em respostas voluntárias, como os do Kaggle, o CAGED fornece informações oficiais e sistematicamente coletadas sobre contratações e demissões formais em todo o país. Sua abrangência nacional e atualização mensal permitem acompanhar as tendências do mercado de trabalho com maior precisão. Além disso, a base contém informações detalhadas sobre vínculos empregatícios, incluindo salário individual, setor de atuação (CNAE), cargo e ocupação (CBO), jornada de trabalho e tipo de admissão ou desligamento, o que possibilita análises mais granulares sobre desigualdade racial e remuneração.

Nesse contexto, este projeto se insere na interseção entre educação, raça e empregabilidade. Para isso, serão utilizadas bases de dados como as do CAGED e do State of Data 2023, que fornecem informações sobre a trajetória educacional e profissional de indivíduos no Brasil. A análise desses dados permitirá identificar padrões, contribuindo para a formulação de políticas e práticas que promovam a equidade racial no mercado de trabalho tecnológico.


###    Problema

O propósito do projeto é responder o seguinte problema orientado a dados: “Existem fatores na formação superior que impactam na inserção e progressão profissional de pessoas pretas, pardas, amarelas ou indígenas no mercado de trabalho tecnológico brasileiro?” 


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

| Atributo | Tipo de Dado  | Subtipo de Dado    | Descrição                                                                 |
|----------|----------------|---------------------|---------------------------------------------------------------------------|
| P1_b     | Qualitativo     | Nominal             | Gênero da pessoa (masculino, feminino, não binário, etc.).               |
| P1_c     | Qualitativo     | Nominal             | Cor/raça/etnia da pessoa (branca, negra, parda, indígena, asiática, etc.).|
| P1_e     | Qualitativo     | Binário (Booleano)  | Indica se a experiência profissional foi prejudicada (sim ou não).       |
| P1_e_2   | Qualitativo     | Binário (Booleano)  | Indica se a experiência foi prejudicada devido à cor/raça/etnia (sim ou não). |
| P1_f     | Qualitativo     | Nominal             | Aspectos prejudicados na experiência profissional (promoção, networking, etc.). |
| P1_l     | Qualitativo     | Ordinal             | Nível de ensino da pessoa (Ensino Médio, Superior, Pós-graduação, etc.). |
| P1_m     | Qualitativo     | Nominal             | Área de formação da pessoa (Ciências da Computação, Engenharia, etc.).   |
| P2_a     | Qualitativo     | Nominal             | Situação atual de trabalho (empregado, desempregado, estagiário, etc.).  |
| P2_b     | Qualitativo     | Nominal             | Setor da empresa ou área de atuação (Tecnologia, Saúde, Educação, etc.). |
| P2_g     | Qualitativo     | Ordinal             | Nível do cargo atual (Pleno, Júnior, Sênior, etc.).                       |
| P2_h     | Quantitativo    | Contínuo            | Faixa salarial anual ou mensal (R$ 3.000, R$ 5.000, etc.).               |
| P2_i     | Quantitativo    | Contínuo            | Tempo de experiência na área de dados (2 anos, 5 anos, etc.).            |
| P2_j     | Quantitativo    | Contínuo            | Tempo de experiência em TI antes de dados (3 anos, 6 anos, etc.).        |

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

## Preparação dos dados
A definição do tema do projeto e a seleção de colunas foram realizadas com base em conjuntos de dados disponibilizados no Kaggle. Paralelamente, a busca por fontes secundárias levou à utilização inicial de dados fornecidos pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

Entretanto, a integração dessas informações revelou desafios significativos. A base de dados do INEP apresentava incompatibilidades estruturais em relação ao conjunto de dados principal, dificultando a conciliação das informações. Ademais, o elevado volume de dados dessa fonte comprometeu a viabilidade do processamento e da análise conjunta, exigindo uma reformulação na estratégia adotada para a construção do estudo.

Após a definição da base secundária CAGED-2023, a próxima etapa consistiu na seleção de atributos relevantes para enriquecimento, um processo essencial para ampliar a profundidade analítica dos dados. Esse enriquecimento permite a incorporação de informações detalhadas sobre vínculos empregatícios, proporcionando uma visão mais completa sobre o comportamento do mercado de trabalho. Além disso, foi definida a chave estrangeira, que consiste em um campo ou conjunto de campos utilizados para estabelecer a relação entre tabelas distintas, garantindo a integridade e coerência da fusão dos dados.  

Com a análise e a definição desses atributos, a próxima etapa envolveu a descrição dos dados por meio de gráficos que se relacionam entre si, considerando os atributos selecionados tanto da base principal quanto da base secundária. Essa abordagem possibilita uma análise aprofundada dos padrões salariais, das desigualdades no mercado de trabalho e da mobilidade profissional, utilizando estatísticas descritivas para quantificar e visualizar tendências.  

A base principal do Kaggle 2023 apresenta um conjunto abrangente de informações sociodemográficas e profissionais, incluindo percepção de discriminação, setor de atuação e experiência no mercado de trabalho. Complementarmente, o CAGED 2023 agrega dados formais sobre vínculos empregatícios, abrangendo aspectos como remuneração, carga horária, categoria profissional e localização. A fusão dessas bases proporciona uma análise mais robusta, ao combinar percepções individuais com registros administrativos, permitindo a investigação aprofundada de dinâmicas de desigualdade, mobilidade profissional e tendências do mercado de trabalho com maior precisão e confiabilidade.

## Indução de modelos

### Modelo 1: Algoritmo

Substitua o título pelo nome do algoritmo que será utilizado. P. ex. árvore de decisão, rede neural, SVM, etc.
Justifique a escolha do modelo.
Apresente o processo utilizado para amostragem de dados (particionamento, cross-validation).
Descreva os parâmetros utilizados. 
Apresente trechos do código utilizado comentados. Se utilizou alguma ferramenta gráfica, apresente imagens
com o fluxo de processamento.

### Modelo 2: Algoritmo

Repita os passos anteriores para o segundo modelo.


## Resultados

### Resultados obtidos com o modelo 1.

Apresente aqui os resultados obtidos com a indução do modelo 1. 
Apresente uma matriz de confusão quando pertinente. Apresente as medidas de performance
apropriadas para o seu problema. 
Por exemplo, no caso de classificação: precisão, revocação, F-measure, acurácia.

### Interpretação do modelo 1

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.


### Resultados obtidos com o modelo 2.

Repita o passo anterior com os resultados do modelo 2.

### Interpretação do modelo 2

Repita o passo anterior com os parâmetros do modelo 2.


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




