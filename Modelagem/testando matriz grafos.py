import networkx as nx
import matplotlib.pyplot as plt


def Gera_Grafo(k):
    # k = int(input("Digite o número de caciques: "))

    lista_caciques = []

    cont = 0
    for j in range(1, k + 1):
        lista_caciques.append(j + cont)  # Cria lista com o número dos nodes dos caciques.
        cont = cont + j

    lista = []  # Cria uma nova lista para os caciques.
    for i in lista_caciques:
        lista.append(i)

    aux_lista = lista_caciques
    aux2_lista = lista_caciques

    print("O número dos nodes de cada cacique é", lista_caciques)

    G = nx.DiGraph()  # Cria um digrafo vazio.

    G.add_nodes_from(lista_caciques)  # Adiciona os nodes dos caciques.

    # Cria link entre os caciques.
    count = 0
    for i in aux2_lista:
        count = count + 1
        for p in aux2_lista[count:]:
            G.add_edge(i, p)
            G.add_edge(p, i)

    # Cria link entre os caciques e os índios respectivos.
    cont = 1
    while len(aux_lista) != 0:
        for t in aux_lista:
            # print(t,t+cont,cont)
            G.add_edge(t, t + cont)
            G.add_edge(t + cont, t)
        del aux_lista[0]
        cont = cont + 1

    nova_lista = []  # Vai conter os pares ordenados rearranjados.
    for i in G.edges():  # Percorre a lista com todas as conexões do grafo.
        x = list(i)  # x vai receber uma conexão do grafo como uma lista.
        if (x[0] and x[1]) in lista:  # Se os dois valores do par ordenado forem caciques, então não é feito nada.
            continue
        # Se o primeiro valor do par ordenado for cacique e o segundo valor do par ordenado não estiver na lista de rearranjo
        # Então a lista de rearranjo é appendada com o cacique na segunda posição do par ordenado (aqui há uma troca no par ordenado).
        if x[0] in lista and x[1] not in nova_lista:
            nova_lista.append([x[1], x[0]])
        # Se o segundo valor do par ordenado for cacique e o primeiro valor do par ordenado não estiver na lista de rearranjo
        # Então a lista de rearranjo é appendada com o cacique na segunda posição do par ordenado (aqui a ordem do par ordenado é mantida).
        if x[1] in lista and x[0] not in nova_lista:
            nova_lista.append([x[0], x[1]])

    # Percerre a lista de caciques.
    for i in lista:
        list2 = []  # Cria uma nova lista para separar todos as conexões de um só cacique.
        # Percorre a lista que contém os pares ordenados rearranjados
        # E verifica se o segundo valor do par ordenado é realmente o cacique procurado.
        # Se for, então o primeiro valor do par ordenado é appendado na lista de conexões do cacique.
        for x in nova_lista:
            if x[1] == i:
                list2.append(x[0])
        # Percorre a lista de conexões do cacique inteiramente e faz todas as "pontes" entre todas as conexões do cacique.
        for x in range(len(list2) - 1):
            for k in range(x, len(list2)):
                # Aqui não é precisa fazer duas pontes, fiz mas depois explico o por quê.
                G.add_edge(list2[x], list2[k])
                G.add_edge(list2[k], list2[x])

    print(nx.info(G))
    nx.draw(G, with_labels=1)

    print(G.edges())
    plt.show()

    ##########
    # lê a variavel global para poder modificar
    global N  # N = numeros de "pontos"
    N = nx.Graph.number_of_nodes(G)

    Grafo = []  # guarda as ligações antes em lista de tupla em uma lista de listas
    for k in G.edges():
        Grafo.append(list(k))
    return Grafo


def Gera_Matriz(Grafo):
    global N  # lê variavel global
    Matriz = [[0 for k in range(N)] for i in range(N)]  # monta matriz vazia

    for i in range(1, N + 1):
        for k in range(len(Grafo)):
            if Grafo[k][0] == i:
                # ligando primeiro (elemento-1) da tupla ao (segundo-1)
                # -1 por ser uma matriz que começa com indice 0
                Matriz[Grafo[k][1] - 1][i - 1] = 1

    # imprimir matriz de 1 linha por linha###########

    print("\n")
    for i in range(len(Matriz)):        
        for k in range(len(Matriz)):
            print(Matriz[i][k]," ", end ='')
        print("")


    for k in range(len(Matriz)):
        cont = 0
        for j in range(len(Matriz)):
            if Matriz[j][k] == 1:  # conta quantos 1 tem em cada coluna
                cont += 1
        for i in range(len(Matriz)):
            if Matriz[i][k] == 1:
                Matriz[i][k] = 1 / cont  # e substitui pelo peso

    ############################
    # Imprimir matriz com peso linha por linha

    print("\n")
    for i in range(len(Matriz)):        
        for k in range(len(Matriz)):
            print("%4.2f" %Matriz[i][k]," ", end ='')
        print("")

    return Matriz


N = 0  # define variavel pra ser usada como global nas funções

Grafo = Gera_Grafo(int(input("Digite o número de caciques: ")))
Matriz = Gera_Matriz(Grafo)
print(Matriz)