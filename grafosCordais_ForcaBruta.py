from itertools import permutations
import time
import networkx as nx
import matplotlib.pyplot as plt
    
def isChordal(G):
    
    print("Grafo a ser analisado:")
    nx.draw_circular(G, node_size=500, with_labels = True)
    plt.show()
    
    cordal = True
    vertices = list(G.nodes)
    l = [] #Lista de combinações de vértices.
    
    #Range de 4 até o tamanho do maior ciclo que possivelmente esteja no grafo (todos os vértices).
    for i in range(4, len(vertices) + 1):#Adição de 1, pois o range é de 0 a n-1 (com 1 a mais vai até n).  
        
        #Geração de todas as possíveis permutações sem repetir a mesma possibilidade com ordem trocada.
        for subset in permutations(vertices, i):#De 4 em 4, depois de 5 em 5, até o número total de vértices.
            if set(subset) not in l:        
                l.append(set(subset))
    #Para cada combinação de vértices gerada,
    #verifica-se se o grau de cada vértice no
    #subgrafo induzido pelos vértices é dois.
    #Se sim, existe um Cn como subgrafo de G,
    #o que invalida a cordalidade.
    for c in l:
        verifica = True
        H = G.subgraph(list(c))
        
        for v in list(H.nodes):
            if H.degree[v] != 2:
                verifica = False
        
        if verifica:
            print("\nO Grafo não é cordal, pois contém Cn, n >= 4, como subgrafo induzido:")
            nx.draw_circular(H, node_size=500, with_labels = True)
            plt.show()
            return False
    #Depois de analisadas todas as combinações, é possível afirmar a cordalidade de G.
    print("\nO Grafo é cordal, pois não contém Cn, n >= 4, como subgrafo induzido.")
    return True
        
            
G = nx.cycle_graph(8)
#G = nx.star_graph(8)
#G = nx.complete_graph(20)
#G = nx.Graph()
#G.add_nodes_from([1,2,3,4])
#G.add_edges_from([(1,3),(3,2),(4,2),(2,1),(4,9),(2,5),(2,9),(5,6),(5,9),
#                  (1,6),(1,9),(6,9),(6,8),(6,7),(8,9),(8,7),(7,9)])
inicio = time.time()
isChordal(G)
fim = time.time()

tempo =  fim - inicio
print("\nTempo de execução: {} segundos.".format(tempo))

