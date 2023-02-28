# Biblioteca Python para Data Augmentation em Português (Brasil)

Projeto realizado em conjunto com o grupo de pesquisa [GASPLN](https://wp.ufpel.edu.br/gaspln/) da Universidade Federal de Pelotas (UFPel) para criar uma biblioteca Python para Data Augmentation em Português (Brasil).

## Instalação

```bash
em construção
```
## Técnicas de Data Augmentation implementadas

- [x] Substituição de sinônimos
- [ ] <s>Word Embeddings</s>
- [ ] <s>Random Insertion</s>
- [ ] <s>Random Swap</s>
- [ ] <s>Random Deletion</s>
- [ ] <s>Back Translation</s>

### Substituição de sinônimos

Como o próprio nome implica, a técnica de substituição de sinônimos consiste em substituir uma palavra por um sinônimo.

Para a criação da lista de sinônimos utilizada no projeto, foi realizado web scraping no [Vocabulário Ortográfico da Língua Portuguesa](https://voc.cplp.org/index.php?action=vonbr) para gerar uma lista de palavras, a qual foi combinada com a [Lista de todas as palavras do português brasileiro](https://www.ime.usp.br/~pf/dicios/) disponibilizada pelo [IME-USP](https://www.ime.usp.br/). A partir da lista de palavras obtidas, foi utilizada a [Dicio API](https://github.com/felipemfp/dicio) criada pelo [Felipe Pontes](https://github.com/felipemfp) para obtenção dos sinônimos, gerando um arquivo parquet com as palavras e seus respectivos sinônimos.

#### Exemplo de uso

... (em construção)