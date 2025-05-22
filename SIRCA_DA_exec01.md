# Curso Sistemas Inteligentes e Robótica em Ciências Agrárias

## Módulo Análise de Dados


# 0. Introdução

O objectivo deste exercício é realizar um *workflow* de análise exploratória de dados
recorrendo a AI para gerar código python. Neste caso, será utilzada a AI 
Gemini integrada no notebook em Google Colab.

Serão realizados os seguintes passos:

1. Gerar um novo notebook Colab;
2. Gerar uma tabela de dados simulada;
3. Analisar os dados com estatísticas de sumário;
4. Resolver problemas de lacunas de dados;
5. Realizar análise exploratória com os dados corrigidos.

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

# Exercício 1

Um solução para este exercício está disponível em [https://colab.research.google.com/drive/1lJZQISkD0FF1LMm3BrLTiVy06EXEm_qC?usp=sharing](https://colab.research.google.com/drive/1lJZQISkD0FF1LMm3BrLTiVy06EXEm_qC?usp=sharing).

## 1. Gerar um novo notebook Colab

Aceda à pasta Google Drive onde pretende criar o novo notebook Colab. Nesta,
crie um novo Google Colab. Para melhor documentar o seu notebook:
- altere o nome do notebook para `Exerc_01.ipynb`
- adicione um título numa célula markdown no topo do notebook, por exemplo
`# Análise exploratória de dados - Parte 1`

> Sobre o **Markdown**: É uma linguagem de formatação simples que permite adicionar 
estilos a texto. Por exemplo, para formatar com itálico, é necessário apenas colocar
um asterisco antes e depois da palavra ou texto a formatar. As células de texto
em Jupyter usam Markdown para melhorar a leitura. <br><br>
> Para experimentar, pratique com o [seguinte exercício](https://github.com/isa-ulisboa/greends-fads-exercises/blob/main/fads_ex_05_markdown.md). 



## 2. Gerar e analisar uma tabela de dados simulada

### 2.1. Gerar uma tabela de dados simulados

Vamos gerar uma tabela que simula parâmetros do solo produzidos por sensores IoT.
Pretende-se obter dados de temperatura, água, humidade, nutrientes, pH e condutividade
eléctrica. Além disso, pretende-se que os dados reproduzam as relações e tendências
normalmente observadas nestes parâmetros. Pretende-se que os dados sejam organizados
num dataframe, normalmente usado para trabalhar dados tabulares.

Para gerar o código que produz esta tabela, use, por exemplo, a seguinte prompt ao 
Gemini:

```
Generate a new simulated dataset of IoT sensor data for soil parameters. Include 
temperature at several depths, moisture at several depths, water content at 
several depths, nitrogen, phosphorous, potassium, pH and EC.Include in the 
simulated data trends, variations and relationships between parameters that are 
normally observed in soil. The new dataset should be a dataframe named soil_simulated.
```

Copiar o código gerado para uma célula de código, e executar.

**Q1. Analisar o código gerado, e a célula de output gerada.**

### 2.2. Gerar uma tabela com simulação de ausência de dados

Iremos fazer uma cópia da tabela de dados gerada, e remover valores para simular
lacunas de dados. Pode fazer-se isso, por exemplo, com a seguinte prompt:
```
Create a copy of the soil_simulated dataframe and in the copy simulate missing data 
at rates between 5 and 15 percent.
```
Note que as tabelas têm nomes diferentes.

**Q2. Pode alterar a prompt para obter outros resultados, ou então editar 
o cógigo gerado.**


### 2.3. Calcular estatísticos básicos

Para gerar o código para calcular estatísticos básicos de cada uma das tabelas,
 use por exemplo, a seguinte prompt em Gemini:

```
Calculate summary statistics for the two dataframes, and compare them.
```

**Q3. Analisar o código gerado, e a célula de output gerada.**

### 2.4. Aplicar métodos de preenchimento de lacunas de dados

Podemos pedir ao Gemini para gerar código que aplique diferentes métodos de 
preenchimento de lacunas de dados. Na prompt seguinte, os métodos são propostos
pelo Gemini, mas em alternativa, pode definir-se na prompt quais são os que devem 
ser usados.
```
To a copy of the dataframe soil_simulated_missing, apply different methods to fill 
in missing data, from simple to more complex methods.

```
**Q4. Analisar o código gerado, e a célula de output gerada.**

### 2.5. Comparação entre os vários métodos de preenchimento de lacunas de dados

Para verificar qe melhor método resolve o problema de lacunas de dados, podemos 
pedir uma comparação da performance.
```
Compare the performance of the several methods to fill missing data.
```

**Q5. Consegue dizer que método tem melhor performance**


### 2.6. Gerar outputs gráficos para facilitar a comparação

Para geral gráficos, podemos fazer o seguinte pedido: 

```
Para a temperatura e para o pH, gerar um gráfico com os dados originais, e ao 
lado outro com os dados preenchidos, usando o método de melhor performance de 
cada parâmetro. Assinalar com cor vermelha os valores que foram preenchidos.
```
**Q6. Gerar os mesmos gráficos para a variável Temperature_50cm.**

### 2.7. Gravar o ficheiro de dados

O Google Colab corre sobre um ambiente virtual que é destruido quando se desliga 
do ambiente. Por isso, para poder reutilizar os dados para mais análises, é 
necessário gravá-lo, em Google Drive, ou no disco do computador local. Neste 
caso, iremos pedir ao Gemini o código para ser gravado no computador local, e 
instruções de como o carregar num novo notebook.

```
Gravar o dataset dos dados simulados inicialmente no disco local, para usar 
noutro colab. Explicar como abrir esse dataset no outro colab.
```
## Resumo

Neste exercício, utilizámos AI para 
- gerar dados simulados
- simular lacunas de dados
- testar métodos de preencimento de lacunas de dados
- representámos os dados através de graficos.



