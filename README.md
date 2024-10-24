# Como executar o programa

Execute o seguinte comando no terminal:

```
python main.py <algoritmo> <tamanho_memoria> <sequencia_paginas>

    <algoritmo>: Selecione entre fifo, lru, ou optimal.
    <tamanho_memoria>: Defina o número de quadros de página.
    <sequencia_paginas>: Sequência de páginas separadas por vírgulas (sem espaços).
```

Exemplo de uso:

```bash
python main.py fifo 3 1,3,5,4,2,4,2,3,2
python main.py lru 3 1,3,5,4,2,4,2,3,2
python main.py optimal 3 1,3,5,4,2,4,2,3,2
bash
