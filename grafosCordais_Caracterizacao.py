import networkx as nx
import matplotlib.pyplot as plt
import time

"""Algorithm: Find perfect elimination order.
For i = n, . . . , 1
Let Gi be the graph induced by V vi+1,. . . ,vn.
Test whether Gi has a simplicial vertex v.
If no, then stop. Gi (and therefore G) has no perfect elimination order.
Else, set vi = v.
v1,. . . ,vn is a perfect elimination order."""

"""Um grafo G = (V,E) é cordal quando todo ciclo de comprimento maior ou igual a 4 possui uma
corda (i.e. uma aresta ligando dois vértices não consecutivos do ciclo). A cordalidade equivale à
existência de um EEP, conforme estabelecido no Teorema 1.

Teorema 1 (Golumbic(1980)). Um grafo é cordal se, e somente se, ele admite um esquema de
eliminação perfeita, que pode iniciar-se com qualquer vértice simplicial.

Lema 3. (Blair e Peyton(1993)). Num grafo G = (V, E) cordal, v ∈ V é simplicial se e somente se
v pertence somente a uma clique maximal.

Note that if G is chordal, then after deleting some vertices, the remaining graph is still chordal. So in
order to show that every chordal graph has a perfect elimination order, it suffices to show that every chordal
has a simplicial vertex; the above algorithm will then yield a perfect elimination order.

 """

"""
Referências:

DETERMINAÇÃO EFICIENTE DE VÉRTICES SIMPLICIAIS EM GRAFOS CORDAIS
Lilian Markenzon, Oswaldo Vernet, Paulo Renato da Costa Pereira

CSL 851: Algorithmic Graph Theory Fall 2013
Lecture 2: Chordal Graphs
Lecturer: Prof. Amit Kumar Scribes: Keshav Choudhary

Professor Knuth's 18th Annual Christmas Tree Lecture at Stanford
December 14, 2012 (https://www.youtube.com/watch?v=txaGsawljjA)

"""

def is_clique(G, vertices):# Verifica se o conjunto vertices forma uma clique em G.
    clique = True
    for v in vertices:
        for u in vertices:
            if u != v:
                if v not in G.neighbors(u):# Cada vértice precisa fazer parte da vizinhança de todos no conjunto vertices.
                    clique = False
                    break
    return clique

def simplicial(G):
    for v in G.nodes:
        if is_clique(G,G.neighbors(v)):# Um vertice v de G é simplicial se seus vizinhos formam uma clique em G.
            return v
    return None

def find_eep(G):
    print("Grafo a ser analisado:")
    nx.draw_circular(G, node_size=500, with_labels = True)
    plt.show()
    
    eep = [] # Esquema de eliminação perfeita.
    n = len(G.nodes())
    vertices = list(G.nodes)
    
    print("Eliminação de vértices simpliciais:")
    for i in range(n, 0, -1):
        H = G.subgraph(vertices) # Subgrafo induzido pelo conjunto vertices.
        print(list(H))
        v = simplicial(H) # Se v for simplicial, ele entra para o EEP e sai do conjunto de vértices
        if v == None: # Se v não for simplicial, então não existe um EEP para este grafo e ele não é cordal.
            print("O Grafo não é cordal, pois não existem vértices simpliciais no subgrafo abaixo:")
            nx.draw_circular(H, node_size=500, with_labels = True)
            plt.show()
            return None
        eep.append(v)
        vertices.remove(v)
    
    print("\nO Grafo é cordal, pois foi encontrado um EEP através da eliminação de vértices simpliciais.")
    print("EEP: {}".format(eep))
    return eep

G = nx.cycle_graph(8)
#G = nx.star_graph(8)
#G = nx.complete_graph(20)
#G = nx.Graph()
#G.add_nodes_from([1,2,3,4])
#G.add_edges_from([(1,3),(3,2),(4,2),(2,1),(4,9),(2,5),(2,9),(5,6),(5,9),
#                  (1,6),(1,9),(6,9),(6,8),(6,7),(8,9),(8,7),(7,9)])
inicio = time.time()
find_eep(G)
fim = time.time()

tempo =  fim - inicio
print("\nTempo de execução: {} segundos.".format(tempo))

