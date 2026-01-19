from grafo_dirigido import GrafoDirigido
from grafo_nao_dirigido import GrafoNaoDirigido
from prim import Prim
from kruskal import Kruskal

if __name__ == "__main__":

    print("\n############### GRAFO NÃO DIRIGIDO ###############")

    g1 = GrafoNaoDirigido()

    v1 = g1.insereV("a")
    v2 = g1.insereV("b")
    v3 = g1.insereV("c")
    v4 = g1.insereV("d")
    v5 = g1.insereV("e")
    v6 = g1.insereV("f")
    v7 = g1.insereV("g")
    v8 = g1.insereV("h")
    v9 = g1.insereV("i")
  
    e1 = g1.insereA("e1", v1, v2, 4)
    e2 = g1.insereA("e3", v1, v8, 8)
    e3 = g1.insereA("e2", v2, v3, 8)  
    e4 = g1.insereA("e4", v2, v8, 11)
    e5 = g1.insereA("e4", v3, v9, 2)
    e6 = g1.insereA("e4", v3, v4, 7)
    e7 = g1.insereA("e4", v3, v6, 4)
    e8 = g1.insereA("e4", v4, v5, 9)
    e9 = g1.insereA("e4", v4, v6, 14)
    e10 = g1.insereA("e4", v5, v6, 10)
    e11 = g1.insereA("e4", v6, v7, 2)
    e12 = g1.insereA("e4", v7, v9, 6)
    e13 = g1.insereA("e4", v7, v8, 1)
    e14 = g1.insereA("e4", v8, v9, 7)

    prim = Prim(g1)
    prim.prim(v1)
    prim.imprimi_custo()

    kruskal = Kruskal(g1)
    kruskal.kruskal()
    kruskal.imprimir_custo()

