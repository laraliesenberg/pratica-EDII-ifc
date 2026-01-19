from grafo_dirigido import GrafoDirigido
from grafo_nao_dirigido import GrafoNaoDirigido
from goodman import Goodman
from dfs import DFS 

if __name__ == "__main__":

    print("\n############### GRAFO NÃO DIRIGIDO ###############")
    g1 = GrafoNaoDirigido()

    a = g1.insereV("a")
    b = g1.insereV("b")
    c = g1.insereV("c")
    d = g1.insereV("d")
  
    e1 = g1.insereA("e1", a, b)
    e2 = g1.insereA("e2", a, c)
    e3 = g1.insereA("e2", a, d)
    e4 = g1.insereA("e2", b, d)
    e5 = g1.insereA("e2", c, d)

    print("\n-Implementação com DFS: ")

    dfs = DFS(g1)
    dfs.dfs()

    print("\n-Implementação com Goodman: ")

    goodman = Goodman(g1)
    goodman.goodman()

    print("\n################## GRAFO DIRIGIDO ##################")

    g2 = GrafoDirigido()

    a = g2.insereV("a")
    b = g2.insereV("b")
    c = g2.insereV("c")
    d = g2.insereV("d")

    #e1 = g2.insereA("e1", a, b)
    e2 = g2.insereA("e2", a, c)
    e3 = g2.insereA("e2", a, d)
    #e4 = g2.insereA("e2", b, d)
    e5 = g2.insereA("e2", c, d)

    print("\n-Implementação com DFS: ")

    dfs = DFS(g2)
    dfs.dfs()

    print("\n-Implementação com Goodman: ")

    goodman = Goodman(g2)
    goodman.goodman()
    