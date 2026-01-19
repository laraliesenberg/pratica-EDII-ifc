from grafo_dirigido import GrafoDirigido
from grafo_nao_dirigido import GrafoNaoDirigido
from bfs import BFS 
from dfs import DFS 
from metodos_auxiliares import MetodosAuxiliares

if __name__ == "__main__":

    print("\n############### GRAFO NÃO DIRIGIDO ###############")
    g1 = GrafoNaoDirigido()

    v = g1.insereV("v")
    r = g1.insereV("r")
    s = g1.insereV("s")
    w = g1.insereV("w")
    t = g1.insereV("t")
    x = g1.insereV("x")
    u = g1.insereV("u")
    y = g1.insereV("y")

    e1 = g1.insereA("e1", v, r)
    e2 = g1.insereA("e2", r, s)
    e3 = g1.insereA("e3", s, w)
    e4 = g1.insereA("e3", w, t)
    e5 = g1.insereA("e3", w, x)
    e6 = g1.insereA("e3", x, t)
    e7 = g1.insereA("e3", x, u)
    e8 = g1.insereA("e3", x, y)
    e9 = g1.insereA("e3", t, u)
    e10 = g1.insereA("e3", y, u)

    print("\nTESTE COM BFS:")
    bfs1 = BFS(g1, s)
    bfs1.bfs()

    print("\nCaminho: ")
    MetodosAuxiliares.imprimeCaminho(bfs1.pi, s, u)

    bfs1.imprimeTabela()

    print("\nTESTE COM DFS:")
    dfs1 = DFS(g1)
    dfs1.dfs()

    print("\nCaminho:")
    MetodosAuxiliares.imprimeCaminho(dfs1.pi, s, u)

    dfs1.imprimeTabela()

    print("\n################## GRAFO DIRIGIDO ##################")
    g2 = GrafoDirigido()

    u = g2.insereV("u")
    v = g2.insereV("v")
    w = g2.insereV("w")
    x = g2.insereV("x")
    y = g2.insereV("y")
    z = g2.insereV("z")

    e1 = g2.insereA("e1", u, v)  
    e2 = g2.insereA("e2", u, x)  
    e3 = g2.insereA("e3", v, y)  
    e4 = g2.insereA("e4", x, v)  
    e5 = g2.insereA("e5", y, x)  
    e6 = g2.insereA("e6", w, y)  
    e7 = g2.insereA("e7", w, z)  
    e8 = g2.insereA("e8", z, z)  

    print("\nTESTE COM DFS:")
    dfs2 = DFS(g2)
    dfs2.dfs()

    print("\nCaminho: ")
    MetodosAuxiliares.imprimeCaminho(dfs2.pi, u, y)

    dfs2.imprimeTabela()

    print("\nTESTE COM BFS:")
    bfs2 = BFS(g2, u)
    bfs2.bfs()

    print("\nCaminho: ")
    MetodosAuxiliares.imprimeCaminho(bfs2.pi, u, y)

    bfs2.imprimeTabela()