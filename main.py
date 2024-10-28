import sys

# Função principal para capturar os inputs de argumentos
def main():
    if len(sys.argv) != 3:
        print("Uso: python ProjetoSO1.py <qtd_paginas> <sequencia_processo>")
        sys.exit(1)

    qtd_paginas = int(sys.argv[1])
    sequencia_processo = sys.argv[2]

    # Escolha qual algoritmo deseja rodar
    FIFO(qtd_paginas, sequencia_processo)
    # OPT(qtd_paginas, sequencia_processo)
    # LRU(qtd_paginas, sequencia_processo)


# Função FIFO com a indicação do número da operação em vez do valor da página
def FIFO(qtd_paginas, sequencia_processo):
    list_memoria = [-1] * qtd_paginas
    ordem_processos = []
    hit = 0
    miss = 0

    list_sequenciaProcesso = list(map(int, sequencia_processo.split(",")))

    for processo in list_sequenciaProcesso:
        print(f"page: {processo}")  # Exibe o número da página processada

        if processo in list_memoria:
            # Caso seja um hit
            hit += 1
            for pag in list_memoria:
                if pag == processo:
                    print(f"[{pag}] <- (hit)")
                else:
                    print(f"[{pag}]")
        else:
            # Caso seja um miss
            miss += 1
            if -1 in list_memoria:
                posicao = list_memoria.index(-1)
            else:
                posicao = list_memoria.index(ordem_processos.pop(0))

            list_memoria[posicao] = processo
            ordem_processos.append(processo)

            # Imprime o estado da memória com indicação de miss
            for pag in list_memoria:
                if pag == processo:
                    print(f"[{pag}] <- (miss)")
                else:
                    print(f"[{pag}]")

        print()  # Linha em branco para separar cada operação

    # Exibe as taxas de hit e miss ao final
    total_acessos = hit + miss
    print(f"Hit rate ({hit}/{total_acessos}):")
    print(f"Miss rate ({miss}/{total_acessos}):")


def LRU(qtd_paginas, sequencia_processo):
    list_memoria = [-1] * qtd_paginas
    ordem_processos = []
    hit = 0
    miss = 0
    list_sequenciaProcesso = list(map(int, sequencia_processo.split(",")))

    for processo in list_sequenciaProcesso:
        print(f"page: {processo}")  # Exibe o número da página processada

        if processo in list_memoria:
            # Caso seja um hit
            hit += 1
            ordem_processos.remove(processo)
            ordem_processos.append(processo)
            for pag in list_memoria:
                if pag == processo:
                    print(f"[{pag}] <- (hit)")
                else:
                    print(f"[{pag}]")
        else:
            # Caso seja um miss
            miss += 1
            if -1 in list_memoria:
                posicao = list_memoria.index(-1)
            else:
                posicao = list_memoria.index(ordem_processos.pop(0))
            list_memoria[posicao] = processo
            ordem_processos.append(processo)

            # Imprime o estado da memória com indicação de miss
            for pag in list_memoria:
                if pag == processo:
                    print(f"[{pag}] <- (miss)")
                else:
                    print(f"[{pag}]")

        print()  # Linha em branco para separar cada operação

    # Exibe as taxas de hit e miss ao final
    total_acessos = hit + miss
    print(f"Hit rate ({hit}/{total_acessos}):")
    print(f"Miss rate ({miss}/{total_acessos}):")


def OPT(qtd_paginas, sequencia_processo):
    list_memoria = [-1] * qtd_paginas
    hit = 0
    miss = 0
    list_sequenciaProcesso = list(map(int, sequencia_processo.split(",")))

    for i, processo in enumerate(list_sequenciaProcesso):
        print(f"page: {processo}")  # Exibe o número da página processada

        if processo in list_memoria:
            # Caso seja um hit
            hit += 1
            for pag in list_memoria:
                if pag == processo:
                    print(f"[{pag}] <- (hit)")
                else:
                    print(f"[{pag}]")
        else:
            # Caso seja um miss
            miss += 1
            if -1 in list_memoria:
                posicao = list_memoria.index(-1)
            else:
                # Calcula a posição da página que será usada o mais tarde possível
                futuras_ocorrencias = [
                    list_sequenciaProcesso[i + 1 :].index(p)
                    if p in list_sequenciaProcesso[i + 1 :]
                    else float("inf")
                    for p in list_memoria
                ]
                posicao = futuras_ocorrencias.index(max(futuras_ocorrencias))

            # Substitui a página na posição calculada
            list_memoria[posicao] = processo

            # Imprime o estado da memória com indicação de miss
            for pag in list_memoria:
                if pag == processo:
                    print(f"[{pag}] <- (miss)")
                else:
                    print(f"[{pag}]")

        print()  # Linha em branco para separar cada operação

    # Exibe as taxas de hit e miss ao final
    total_acessos = hit + miss
    print(f"Hit rate ({hit}/{total_acessos}):")
    print(f"Miss rate ({miss}/{total_acessos}):")


if __name__ == "__main__":
    main()
