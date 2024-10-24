import sys

# Função para o algoritmo FIFO
def substituicao_pagina_fifo(tamanho_memoria, sequencia_paginas):
    memoria = [-1] * tamanho_memoria  # Inicializa a memória com -1 (vazia)
    contador_miss = 0
    contador_hit = 0
    ponteiro = 0

    for pagina in sequencia_paginas:
        print(f"Página: {pagina}")
        if pagina in memoria:
            imprimir_memoria(memoria)
            print(" <- (acerto)")
            contador_hit += 1
        else:
            memoria[ponteiro] = pagina
            imprimir_memoria(memoria)
            print(" <- (erro)")
            ponteiro = (ponteiro + 1) % tamanho_memoria
            contador_miss += 1

    total_solicitacoes = len(sequencia_paginas)
    print(f"\nTaxa de acertos ({contador_hit}/{total_solicitacoes}):")
    print(f"Taxa de erros ({contador_miss}/{total_solicitacoes}):")

# Função para o algoritmo LRU
def lru(paginas, capacidade):
    quadros = []
    erros = 0
    historico_quadros = []

    for pagina in paginas:
        hit_ou_miss = "erro"  # Assume erro por padrão
        if pagina in quadros:
            hit_ou_miss = "acerto"
            historico_quadros.remove(pagina)  # Atualiza a ordem se for acerto
        else:
            erros += 1
            if len(quadros) == capacidade:
                quadro_lru = historico_quadros.pop(0)
                quadros.remove(quadro_lru)
            quadros.append(pagina)

        historico_quadros.append(pagina)

        print(f"Página: {pagina} ({hit_ou_miss})")
        imprimir_memoria(quadros)

    # Calcula e exibe a Taxa de Acertos e Taxa de Erros
    contador_acertos = len(paginas) - erros
    total_solicitacoes = len(paginas)
    print(f"\nTaxa de acertos ({contador_acertos}/{total_solicitacoes}):")
    print(f"Taxa de erros ({erros}/{total_solicitacoes}):")

# Função para o algoritmo Ótimo (Optimal)
def substituicao_pagina_otima(tamanho_memoria, sequencia_paginas):
    memoria = [-1] * tamanho_memoria  # Inicializa a memória com -1 (vazia)
    contador_miss = 0
    contador_hit = 0

    for i, pagina in enumerate(sequencia_paginas):
        print(f"Página: {pagina}")
        if pagina in memoria:
            imprimir_memoria(memoria)
            print(" <- (acerto)")
            contador_hit += 1
        else:
            if -1 in memoria:
                memoria[memoria.index(-1)] = pagina  # Coloca na primeira posição vazia
            else:
                # Encontrar a página que será usada o mais tarde possível
                indice_mais_distante = encontrar_pagina_mais_distante(memoria, sequencia_paginas, i + 1)
                memoria[indice_mais_distante] = pagina

            imprimir_memoria(memoria)
            print(" <- (erro)")
            contador_miss += 1

    total_solicitacoes = len(sequencia_paginas)
    print(f"\nTaxa de acertos ({contador_hit}/{total_solicitacoes}):")
    print(f"Taxa de erros ({contador_miss}/{total_solicitacoes}):")

def encontrar_pagina_mais_distante(memoria, sequencia_paginas, indice_futuro):
    distancia_mais_distante = -1
    indice_mais_distante = -1

    for i, pagina in enumerate(memoria):
        if pagina not in sequencia_paginas[indice_futuro:]:
            return i  # Página não será usada novamente, pode ser substituída
        else:
            # Encontrar a página que será usada mais tarde
            distancia = sequencia_paginas[indice_futuro:].index(pagina)
            if distancia > distancia_mais_distante:
                distancia_mais_distante = distancia
                indice_mais_distante = i

    return indice_mais_distante

# Função auxiliar para imprimir o estado da memória
def imprimir_memoria(memoria):
    for pagina in memoria:
        print(f"[ {pagina}]", end=" ")
    print(end="")  # Mantém a linha para adicionar o "acerto" ou "erro"
    print()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python main.py <algoritmo> <tamanho_memoria> <sequencia_paginas>")
        print("Algoritmos: fifo, lru, optimal")
        sys.exit(1)

    algoritmo = sys.argv[1].lower()
    tamanho_memoria = int(sys.argv[2])
    sequencia_paginas = list(map(int, sys.argv[3].split(',')))

    if algoritmo == "fifo":
        substituicao_pagina_fifo(tamanho_memoria, sequencia_paginas)
    elif algoritmo == "lru":
        lru(sequencia_paginas, tamanho_memoria)
    elif algoritmo == "otimo":
        substituicao_pagina_otima(tamanho_memoria, sequencia_paginas)
    else:
        print("Algoritmo inválido! Escolha entre: fifo, lru, optimal.")
        sys.exit(1)
