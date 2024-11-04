import sys

#Função principal para capturar os inputs de argumentos.
def main():
    if len(sys.argv) != 3:
        print("Uso: python ProjetoSO.py <qtd_paginas> <sequencia_processo>")
        sys.exit(1)

    qtd_paginas = int(sys.argv[1])
    sequencia_processo = sys.argv[2]

    #Roda os algoritmos.
    FIFO(qtd_paginas, sequencia_processo)
    OPT(qtd_paginas, sequencia_processo)
    LRU(qtd_paginas, sequencia_processo)

#Realiza a criação da lógica do LRU.
def FIFO(qtd_paginas, sequencia_processo):
    #Realiza o print da metodologia.
    print()
    print("FIFO:")

    #Instancia uma lista com a quantidade de index igual a quantidade de páginas.
    list_memoria = []
    contador = qtd_paginas
    while contador > 0:
        list_memoria.append(-1)
        contador = contador - 1
    
    #Fraciona a sequencia e add cada valor em um index de uma lista.
    list_sequenciaProcesso = list(map(int, sequencia_processo.split(",")))

    #Cria a lista com a ordem dos processos chamados.
    ordem_processos = []

    #Cria as variáveis hit e miss.
    hit = 0
    miss = 0

    #Informa se foi miss ou hit.
    hit_miss = None

    #Realiza a leitura de cada processo.
    for processo in list_sequenciaProcesso:
        #Verifica se o valor está presente na lista.
        if processo in list_memoria:
            #Incrementa na variavel hit.
            hit = hit + 1

            #Informa que foi um hit.
            hit_miss = '(hit)'
        
        else:
            #Informa que foi um miss.
            hit_miss = '(miss)'

            #Verifica se há um espaço na memória.
            if -1 in list_memoria:
                local_memoria = list_memoria.index(-1)
                #Aloca o processo na memória.
                list_memoria[local_memoria] = processo

                #Adiciona o processo na lista com a ordem dos processos.
                ordem_processos.append(processo)

                #Incrementa na variável miss.
                miss = miss + 1
            
            #Caso não tenha espaço, remove o primeiro processo alocado e adiciona o novo processo.
            else:
                local_memoria = list_memoria.index(ordem_processos[0])

                #Aloca o processo na memória.
                list_memoria[local_memoria] = processo

                #Remove o processo do index 0 e add o processo inserido 
                ordem_processos.pop(0)
                ordem_processos.append(processo)

                #Incrementa na variável miss.
                miss = miss + 1

        #Organiza o print.
        print()
        print('page: ', processo)
        for processo_print in list_memoria:
            if processo_print == processo:
                print('[',processo_print, '] <-', hit_miss)
            else:
                print('[',processo_print, ']')

    print()
    print("Hit rate (", hit, "/", len(list_sequenciaProcesso),"):")
    print("Miss rate (", miss, "/", len(list_sequenciaProcesso),"):")

#Realiza a criação da lógica do OPT
def OPT(qtd_paginas, sequencia_processo):
    #Realiza o print da metodologia
    print()
    print("OPT:")

    #Instancia uma lista com a quantidade de index igual a quantidade de páginas.
    list_memoria = []
    contador = qtd_paginas
    while contador > 0:
        list_memoria.append(-1)
        contador = contador - 1
    
    #Fraciona a sequencia e add cada valor em um index de uma lista.
    list_sequenciaProcesso = list(map(int, sequencia_processo.split(",")))

    #Cria as variáveis hit e miss.
    hit = 0
    miss = 0

    #Cria o contador com o valor do index do processo que está em análise.
    contador_index = 0

    #Informa se foi miss ou hit.
    hit_miss = None

    #Realiza a leitura de cada processo.
    for processo in list_sequenciaProcesso:
        #Verifica se o valor está presente na lista.
        if processo in list_memoria:
            #Incrementa na variavel hit.
            hit = hit + 1

            #Informa que foi um hit.
            hit_miss = '(hit)'

        else:
            #Informa que foi um miss.
            hit_miss = '(miss)'

            #Verifica se há um espaço na memória.
            if -1 in list_memoria:
                local_memoria = list_memoria.index(-1)
                #Aloca o processo na memória.
                list_memoria[local_memoria] = processo

                #Incrementa na variável miss.
                miss = miss + 1
            
            #Caso não tenha espaço, remove o processo que mais vai demorar para entrar novamente.
            else:

                #Filtra a lista com os valores do index para frente.
                list_sequenciaFutura = list_sequenciaProcesso[contador_index+1:]
                
                #Verifica qual valor na memória mais vai demorar para ser chamado.
                list_localProcessoTotal = []
                for processo_memoria in list_memoria:
                    list_localProcesso = []
                    if processo_memoria in list_sequenciaFutura:
                        list_localProcesso.append([processo_memoria, list_sequenciaFutura.index(processo_memoria)])
                    else:
                        list_localProcesso.append([processo_memoria, -1])
                    list_localProcessoTotal.append(list_localProcesso)

                #Procura pelo primeiro processo com valor -1
                processo_selecionado = next((sublista[0][0] for sublista in list_localProcessoTotal if sublista[0][1] == -1), None)

                #Se nenhum -1 foi encontrado, procura o maior valor.
                if processo_selecionado is None:
                    maior_valor = max(list_localProcessoTotal, key=lambda x: x[0][1])
                    processo_selecionado = maior_valor[0][0]

                #Aloca o processo na memória.
                local_memoria = list_memoria.index(processo_selecionado)
                list_memoria[local_memoria] = processo

                #Incrementa na variável miss.
                miss = miss + 1
        
        #Atualiza a variável contador_index.
        contador_index = contador_index + 1

        #Organiza o print.
        print()
        print('page: ', processo)
        for processo_print in list_memoria:
            if processo_print == processo:
                print('[',processo_print, '] <-', hit_miss)
            else:
                print('[',processo_print, ']')
        
    print()
    print("Hit rate (", hit, "/", len(list_sequenciaProcesso),"):")
    print("Miss rate (", miss, "/", len(list_sequenciaProcesso),"):")

#Realiza a criação da lógica do LRU.
def LRU(qtd_paginas, sequencia_processo):
    #Realiza o print da metodologia
    print()
    print("LRU:")

    #Instancia uma lista com a quantidade de index igual a quantidade de páginas.
    list_memoria = []
    contador = qtd_paginas
    while contador > 0:
        list_memoria.append(-1)
        contador = contador - 1
    
    #Fraciona a sequencia e add cada valor em um index de uma lista.
    list_sequenciaProcesso = list(map(int, sequencia_processo.split(",")))

    #Cria a lista com a ordem dos processos chamados.
    ordem_processos = []

    #Cria as variáveis hit e miss.
    hit = 0
    miss = 0

    #Informa se foi miss ou hit.
    hit_miss = None

    #Realiza a leitura de cada processo.
    for processo in list_sequenciaProcesso:
        #Verifica se o valor está presente na lista.
        if processo in list_memoria:
            #Atualiza a posição na lista de ordem.
            ordem_processos.remove(processo)
            ordem_processos.append(processo)

            #Incrementa na variavel hit.
            hit = hit + 1

            #Informa que foi um hit.
            hit_miss = '(hit)'
        
        else:
            #Informa que foi um miss.
            hit_miss = '(miss)'
            
            #Verifica se há um espaço na memória.
            if -1 in list_memoria:
                local_memoria = list_memoria.index(-1)
                #Aloca o processo na memória.
                list_memoria[local_memoria] = processo

                #Adiciona o processo na lista com a ordem dos processos.
                ordem_processos.append(processo)

                #Incrementa na variável miss.
                miss = miss + 1
            
            #Caso não tenha espaço, remove o primeiro processo alocado e adiciona o novo processo.
            else:
                local_memoria = list_memoria.index(ordem_processos[0])

                #Aloca o processo na memória.
                list_memoria[local_memoria] = processo

                #Remove o processo do index 0 e add o processo inserido 
                ordem_processos.pop(0)
                ordem_processos.append(processo)

                #Incrementa na variável miss.
                miss = miss + 1

        #Organiza o print.
        print()
        print('page: ', processo)
        for processo_print in list_memoria:
            if processo_print == processo:
                print('[',processo_print, '] <-', hit_miss)
            else:
                print('[',processo_print, ']')

    print()
    print("Hit rate (", hit, "/", len(list_sequenciaProcesso),"):")
    print("Miss rate (", miss, "/", len(list_sequenciaProcesso),"):")

main()