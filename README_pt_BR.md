# Biblioteca de Data Augmentation para Português (Brasil)

**For a version of this README in English, click [here](README.md).**

Este é um projeto de pesquisa desenvolvido em colaboração com o grupo de pesquisa [GASPLN](https://wp.ufpel.edu.br/gaspln/) da Universidade Federal de Pelotas (UFPel) com o objetivo de criar uma biblioteca Python para Data Augmentation para textos em Português (Brasil).

## Sumário

- [Instalação](#instalação)
- [Uso](#uso)
    - [Substituição de Sinônimos](#substituição-de-sinônimos---synonyms_replacement)
    - [Tradução Reversa](#tradução-reversa---back_translation)
    - [Troca de Caracteres](#troca-de-caracteres---character_swap)
    - [Troca Aleatória](#troca-aleatória-de-palavras---random_swap)
    - [Adição de Ruído](#adição-de-ruído---add_noise)
    - [Augmentação de Texto](#augmentação-de-texto---text_augmentation)
- [Dataset de Sinônimos](#dataset-de-sinônimos)

# Instalação

O pacote está disponível no PyPI e pode ser facilmente instalado usando o pip:

```bash
pip install data_augmentation_GASPLN
```

Você também precisa baixar o modelo em Português para spaCy. Para fazer isso, execute o seguinte comando:

```bash
python -m spacy download pt_core_news_sm
```

# Uso

## Substituição de Sinônimos - **synonyms_replacement()**

Esta função é usada para substituir uma porcentagem de palavras em uma determinada string de texto pelos seus sinônimos. Ela recebe dois parâmetros: text e percentage.

***Para informações a respeito do dicionário de sinônimos utilizado na função, navegue até [Dataset de Sinônimos](#dataset-de-sinônimos).***

### Parâmetros

- `text` (str): O texto de entrada a ser processado. Isso pode ser qualquer string, mas idealmente deve ser uma frase completa ou parágrafo para melhores resultados.

- `percentage` (float, opcional): A porcentagem de palavras no text de entrada que devem ser substituídas pelos seus sinônimos. O valor padrão é 0,25, o que significa que 25% das palavras no texto de entrada serão substituídas.

### Examplo de Uso

Aqui está um exemplo de como usar a função `synonyms_replacement`:

```python
from data_augmentation_GASPLN import synonyms_replacement

# Chame a função com os seguintes parâmetros
text = "Texto a ser augmentado aqui."
augmented_text = synonyms_replacement(text, percentage=0.25)

# Print the result
print(augmented_text)
```

## Tradução Reversa - **back_translation()**

Esta função realiza a tradução reversa do texto fornecido, iterando sobre os idiomas fornecidos na lista.

### Argumentos

- `text` (str): O texto de entrada a ser traduzido.

- `languages` (List[str]): A lista de idiomas a ser usada para a tradução reversa.

- `translator` (str): O nome do tradutor a ser usado para a tradução reversa. Deve ser um dos disponíveis em https://pypi.org/project/translators/#supported-translation-services

### Exemplo de uso

```python
from data_augmentation_GASPLN import back_translation

# Chame a função com os seguintes parâmetros
text = "Texto a ser traduzido aqui."
languages = ['es', 'fr', 'pt']
translator = 'google'

augmented_text = back_translation(text, languages, translator)

# Imprima o resultado
print(augmented_text)
```

## Troca de Caracteres - **character_swap()**

Esta função é usada para trocar caracteres em palavras do texto de entrada com uma probabilidade determinada, exceto para palavras com três letras ou menos ou para sinais de pontuação, mantendo suas posições na palavra. Ela recebe dois argumentos: `text` e `prob`.

### Argumentos

- `text` (str): O texto de entrada para trocar os caracteres. Pode ser qualquer string, mas idealmente deve ser uma frase completa ou um parágrafo para melhores resultados.

- `prob` (float, opcional): A probabilidade de trocar caracteres em cada palavra elegível. O valor padrão é 0.25, o que significa que há uma chance de 25% de trocar caracteres em cada palavra elegível.

### Exemplo de uso:

Aqui está um exemplo de como usar a função `character_swap`:

```python
from data_augmentation_GASPLN import character_swap

# Chame a função com os seguintes parâmetros
text = "Texto a ser augmentado aqui aqui."
augmented_text = character_swap(text, prob=0.4)

# Imprima o resultado
print(augmented_text)
```

## Troca Aleatória de Palavras - **random_swap()**

Esta função troca aleatoriamente palavras em um texto. Você pode especificar a porcentagem de palavras a serem trocadas, ou o número de palavras a serem trocadas, ou a probabilidade de trocar cada palavra (com um padrão de 20%).

### Argumentos

- `text` (str): O texto de entrada para trocar as palavras. Isso pode ser qualquer string.

- `percentage` (float, opcional): A porcentagem de palavras a serem trocadas no texto de entrada. O valor padrão é None.

- `num_words` (int, opcional): O número de palavras a serem trocadas no texto de entrada. O valor padrão é None.

- `prob` (float, opcional): A probabilidade de trocar cada palavra no texto de entrada. O valor padrão é 0.15.

### Exemplo de uso

Aqui está um exemplo de como usar a função `random_swap`:

```python
from data_augmentation_GASPLN import random_swap

# Chame a função com os seguintes parâmetros
text = "Texto a ser augmentado aqui."
augmented_text = random_swap(text, percentage=0.25)

# Imprima o resultado
print(augmented_text)
```

## Adição de Ruído - **add_noise()**

Esta função é usada para adicionar ruído a uma porcentagem das palavras em uma string de texto dada, inserindo ou removendo letras e trocando pontuações com uma pequena probabilidade. Ela recebe três argumentos: texto, probabilidade_ruido_palavra e probabilidade_ruido_caractere.

### Argumentos

- `text` (str): O texto de entrada a ser processado. Isso pode ser qualquer string, mas idealmente deve ser uma frase completa ou parágrafo para obter melhores resultados.

- `prob_noise_word` (float, opcional): A probabilidade de adicionar ruído a uma palavra dada. O valor padrão é 0.2, o que significa que 20% das palavras no texto de entrada terão ruído adicionado a elas.

- `prob_noise_char` (float, opcional): A probabilidade de adicionar ou remover uma letra de uma palavra dada. O valor padrão é 0.2, o que significa que há 20% de chance de que uma letra seja adicionada ou removida de uma palavra.

### Exemplo de uso

Aqui está um exemplo de como usar a função `add_noise`:

```python
from data_augmentation_GASPLN import add_noise

# Chame a função com os seguintes parâmetros
text = "Texto a ser augmentado aqui."
augmented_text = add_noise(text, word_noise_prob=0.2, char_noise_prob=0.2)

# Print the result
print(augmented_text)
```

## Augmentação de Texto - **text_augmentation()**

Esta função aplica múltiplas técnicas de augmentação de texto ao texto de entrada. Ela recebe vários argumentos que determinam quais técnicas são utilizadas e com quais parâmetros.

### Argumentos

- `text` (str): O texto de entrada a ser processado.

- `use_synonyms` (bool, opcional): Se deve ou não utilizar substituição de sinônimos. O padrão é `True`.

- `synonyms_percentage` (float, opcional): A porcentagem de palavras no texto de entrada que devem ser substituídas por seus sinônimos. O padrão é 0.5.

- `use_back_translation` (bool, opcional): Se deve ou não utilizar tradução reversa. O padrão é `False`.

- `languages` (List[str], opcional): Uma lista de códigos de idiomas de dois caracteres representando os idiomas para traduzir o texto para e de volta. O padrão é `['en', 'es']`.

- `translator` (str, opcional): O nome do tradutor a ser usado para a tradução reversa. Atualmente, o único valor suportado é `'google'`. O padrão é `'google'`.

- `use_character_swap` (bool, opcional): Se deve ou não utilizar substituição de caracteres. O padrão é `False`.

- `char_swap_prob` (float, opcional): A probabilidade de trocar um caractere em uma palavra. O padrão é 0.25.

- `use_random_swap` (bool, opcional): Se deve ou não utilizar substituição aleatória de palavras. O padrão é `False`.

- `random_swap_percentage` (float, opcional): A porcentagem de palavras no texto de entrada que serão trocadas por outras palavras. Se `num_words` for especificado, este parâmetro é ignorado. O padrão é `None`.

- `num_words` (int, opcional): O número de palavras para trocar por outras palavras no texto de entrada. Se `num_words` for especificado, `random_swap_percentage` é ignorado. O padrão é `None`.

- `random_swap_prob` (float, opcional): A probabilidade de trocar uma palavra no texto. O padrão é 0.15.

- `use_add_noise` (bool, opcional): Se deve ou não adicionar ruído ao texto. O padrão é `True`.

- `word_noise_prob` (float, opcional): A probabilidade de adicionar ruído a uma palavra no texto. O padrão é 0.2.

- `char_noise_prob` (float, opcional): A probabilidade de adicionar ou remover um caractere em uma palavra no texto. O padrão é 0.2.

### Exemplo de Uso

Aqui está um exemplo de como usar a função `text_augmentation`:

```python
from data_augmentation_GASPLN import text_augmentation

# Chame a função com os seguintes parâmetros
text = "Texto a ser augmentado aqui."
augmented_text = text_augmentation(text, 
                                    use_synonyms=True, synonyms_percentage=0.4, 
                                    use_back_translation=True, languages=['en', 'fr'], translator='google', 
                                    use_character_swap=True, char_swap_prob=0.3, 
                                    use_random_swap=True, num_words=2, random_swap_prob=0.2, 
                                    use_add_noise=True, word_noise_prob=0.3, char_noise_prob=0.3)

# Print the result
print(augmented_text)
```

## Dataset de Sinônimos

Para a geração do dataset de sinônimos utilizado neste projeto, inicialmente foi feita uma coleta de palavras do vocabulário da língua portuguesa a partir do web scraping do [Vocabulário Ortográfico Comum da Língua Portuguesa](https://voc.cplp.org/index.php?action=simplesearch&query=a&sel=start) e da concatenação com a [lista de palavras do português brasileiro](https://www.ime.usp.br/~pf/dicios/br-utf8.txt) disponibilizada pelo [Instituto de Matemática e Estatística da Universidade de São Paulo (IME-USP)](https://www.ime.usp.br/). O resultado foi uma lista com 458437 palavras.

Em seguida, foi utilizada a [Dicio API](https://github.com/ThiagoNelsi/dicio-api), disponibilizada por [Thiago Nelsi do Couto](https://github.com/ThiagoNelsi) para gerar um dataset com as palavras e seus respectivos sinônimos. Com isso, o projeto oferece uma base de dados rica em palavras e sinônimos que pode ser utilizada em diversas aplicações.

A lista de palavras do vocabulário da língua portuguesa e o dicionário de sinônimos podem ser encontrados na pasta [data](data_augmentation_GASPLN/data) deste repositório.
Os notebooks utilizados para a coleta e geração do dicionário de sinônimos podem ser encontrados na pasta [web_scraping](web_scraping) deste repositório.
