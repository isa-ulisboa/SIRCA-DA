# Curso Sistemas Inteligentes e Robótica em Ciências Agrárias

## Módulo Análise de Dados


# 0. Introdução

O objectivo deste exercício é realizar um *workflow* de análise exploratória de dados
recorrendo a AI para gerar código python. Neste caso, será utilzada a AI 
Gemini integrada no notebook em Google Colab. Este exercício deve ser antecedido 
da realização do [Exercício 1](https://github.com/isa-ulisboa/SIRCA-DA/blob/main/sirca_DA_exec01.md).

Serão realizados os seguintes passos:

1. Gerar um novo notebook Colab;
2. Adicionar um ficheiro de dados;
3. Calcular estatísticas básicas;
4. Gerar gráficos para análise univariada das variáveis;
5. Gerar gráficos para análise bivariada das variáveis;
6. Calcular correlações entre as variáveis.
7. Calcular a Análise em Componentes Principais

Durante este exercício, é possível que surjam erros no código gerado pelo Gemini
que deve ser detectados e corrigidos.


## Instruções e convenções para este documento

Este documento está estruturado segundo uma sequência de prompts a fazer à chat AI,
que estão indicados por uma caixa de código. Exemplo:

```
In python, create a simulated dataframe containing three columns of text containing 
the name, address and phone number of people.
```
O acesso à ferramenta AI Gemini faz-se clicando no icon ![image](images/icon_gemini.png).


De seguida, o notebook contém a **bold** a indicação do que deve ser analisado 
nos resultados da execução do código gerado. Por exemplo:

**Q1. Compare o valor das médias entre os métodos.**

Note-se que é possível que o chat com o Gemini não seja arquivado. Por isso, em 
cada passo, recomenda-se que o texto da prompt seja adicionado a uma célula 
markdown, anterior à célula de código que foi gerada a partir desta, com uma nota
explicativa do que se pretende fazer. 

São também adicionados blocos de texto com explicação ou apontadores externos para mais documentação:

>Para saber mais sobre python, consulte [https://www.python.org/](https://www.python.org/).

# Exercício 2

Um solução para este exercício está disponível em [https://colab.research.google.com/drive/1ZBVbflWxAWJW9UBB6Y8IRr3vmNHVXCwX?usp=sharing](https://colab.research.google.com/drive/1ZBVbflWxAWJW9UBB6Y8IRr3vmNHVXCwX?usp=sharing).

## 1. Adicionar uma tabela de dados ao Colab

Aceda à pasta Google Drive onde pretende criar o novo notebook Colab. Nesta,
crie um novo Google Colab. Para melhor documentar o seu notebook:
- altere o nome do notebook para `Exerc_02.ipynb`
- adicione um título numa célula markdown no topo do notebook, por exemplo
`# Análise exploratória de dados - parte 2`

Para gerar o código que permite adicionar o ficheiro guardado seu computador 
local, use a seguinte prompt no Gemini:

```
Importar o csv chamado soil_simulated do disco local para um dataframe
``` 

A execução deste código cria um botão para fazer browse e selecionar o ficheiro
no seu disco local.

## 2. Analisar os dados

### 2.1. Calcular os parâmetros estatísticos básicos

Os parâmetros estatísticos básicos para variáveis contínuas incluem medidas de 
tendência central (média, mediana, moda) e medidas de dispersão (desvio padrão, 
variância, intervalo interquartil).

Para gerar o código que produz esta tabela, use, por exemplo, a seguinte prompt ao 
Gemini:

```
Calcular as estatísticas básicas das variáveis.
```
Copiar o código gerado para uma célula de código, e executar.

**Q1.Verificar se o código produzido calcula todas as as estatísticas desejadas.**

Pode ser necessário alterar a prompt, adicionando mais detalhe, por exemplo, pedindo
o intervalo interquartil.

### 2.2. Gerar gráficos para análise univariada dos dados

Crie uma prompt para criar o código que gera gráficos univariados:
```
Gerar três tipos de gráficos para analisar as variáveis. Para cada variável, agrupar 
os gráficos em linha.
```

**Q2. Pode alterar a prompt adicionar mais gráficos univariados, por exemplo,
a função densidade de probabilidade, o Swarn plot e o strip plot.**


### 2.3. Calcular diagramas de dispersão

Para gerar o código para crair diagramas de dispersão. Pretende-se identificar 
relações entre as variáveis. Além disso, pretendemos identificar amostras anómalas.
Use, por exemplo, a seguinte prompt em Gemini:

```
Explorar os pares de variáveis com diagramas de dispersão. Se houver outliers, 
assinalar com um símbolo diferente. Não incluir a variável Tempo. Adicionar uma 
linha da relação, e agrupar os gráficos em três.
```

**Q3. Os outliers identificados são de primeira ou segunda ordem?**

**Q4. Para que pares de variáveis é possível identificar uma relação?**

### 2.4. Cálculo da correlação entre variáveis

Para calcular a correlação entre as variáveis, pode-se gerar o código com a seguinte
prompt:
```
Calcular a correlação entre todas as variáveis. Assinalar as que são significativas.

```
**Q5. Analisar o código gerado, e o output gerado.**

**Q6. Verifique como foram identificadas as correlações significativas.**

### 2.5. Cálculo da Análise em Componentes Principais

Para gerar o código que calcula a Análise em Componentes Principais, pode usar a
seguinte prompt.
```
Calcular a Análise em Componentes Principais para o dataset.
```

**Q7. Avaliar os vários outputs gerados**

### 2.6. Representar os planos factoriais da PCA

Para gerar gráficos, podemos fazer o seguinte pedido: 

```
Representar o biplot da PCA para o primeiro e segundo planos factoriais.
```
**Q8. Analisar a qualidade do output, em relação a interpretação dos gráficos.**

### 2.7. Melhorar o output da PCA

O output do passo anterior não é satisfatório, pois não permite ver o nome 
das variáveis. Além disso, o código gerado apenas criou a representação do primeiro
plano factorial (factor 1 e 2), mas não do segundo plano factorial (factor 1 e 3).

Para gerar uma melhor visualização, pode-se usar a seguinte prompt:

```
No plot da PCA, evitar a sobreposição dos labels das variáveis para melhorar a 
visualização. Se for necessário, usar abreviaturas das variáveis.
```

> É possível que no código gerado seja incluída a utilização do package `adjustText`, 
que no entanto não vem já instalado ni ambiente virtual em uso. Por isso, a sua 
instalação pode ser feita adicionando a seguinte linha de código no cimo do 
bloco de código:
```pyhton
!pip install adjustText
```

**Q9. Criar o gráfico para o segundo plano factorial, copiando e adaptando o 
bloco de código.**

**Q10. As relações apresentadas fazem sentido?**


## Resumo

Neste exercício, utilizámos AI para 
- gerar código para carregar dados
- calcular estatísticas básicas
- criar gráficos de estatísticas univariadas e bivariadas
- calcular a ACP



