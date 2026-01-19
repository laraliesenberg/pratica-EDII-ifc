from grafo_dirigido import GrafoDirigido
from grafo_nao_dirigido import GrafoNaoDirigido
from dijkstra import Dijkstra
from floyd_warshall import FloydWarshall


if __name__ == "__main__":

    print("\n############### GRAFO NÃO DIRIGIDO ###############")

    print("\nUtilizando DIJKSTRA:")

    g1 = GrafoNaoDirigido()

    v1 = g1.insereV("v1")
    v2 = g1.insereV("v2")
    v3 = g1.insereV("v3")
    v4 = g1.insereV("v4")

  
    e1 = g1.insereA("e1", v1, v2, 2)
    e2 = g1.insereA("e2", v2, v3, 3)   
    e3 = g1.insereA("e3", v1, v4, 10)
    e4 = g1.insereA("e4", v4, v3, 1)

    alg = Dijkstra(g1)
    alg.dijkstra(v1)
    alg.imprime_caminho(v1, v4)

    print("\nUtilizando FLOYD-WARSHALL:")

    fw = FloydWarshall(g1)
    fw.executar()

    fw.imprimir_caminho(v1, v4)
    fw.imprimir_caminho(v3, v1)

    print("\n############### GRAFO DIRIGIDO ###############")

    print("\nUtilizando DIJKSTRA:")

    g2 = GrafoDirigido()

    v1 = g2.insereV("v1")
    v2 = g2.insereV("v2")
    v3 = g2.insereV("v3")
    v4 = g2.insereV("v4")

  
    e1 = g2.insereA("e1", v1, v2, 2)
    e2 = g2.insereA("e2", v2, v3, 3)   
    e3 = g2.insereA("e3", v1, v4, 10)
    e4 = g2.insereA("e4", v3, v4, 1)

    alg = Dijkstra(g2)
    alg.dijkstra(v1)
    alg.imprime_caminho(v1, v4)

    print("\nUtilizando FLOYD-WARSHALL:")

    fw = FloydWarshall(g2)
    fw.executar()

    fw.imprimir_caminho(v1, v4)