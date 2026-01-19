from grafo_dirigido import GrafoDirigido
from grafo_nao_dirigido import GrafoNaoDirigido
from CicloEuleriano import CicloEuleriano
from goodman import Goodman


if __name__ == "__main__":

    print("\n############### GRAFO NÃO DIRIGIDO ###############")
    g1 = GrafoNaoDirigido()

    v1 = g1.insereV("v1")
    v2 = g1.insereV("v2")
    v3 = g1.insereV("v3")
    v4 = g1.insereV("v4")
    v5 = g1.insereV("v5")
    v6 = g1.insereV("v6")

  
    e1 = g1.insereA("e1", v1, v4)
    e2 = g1.insereA("e2", v2, v5)
    e3 = g1.insereA("e3", v2, v5)
    e4 = g1.insereA("e4", v3, v6)
    e5 = g1.insereA("e5", v4, v5)
    e6 = g1.insereA("e6", v5, v6)
    e7 = g1.insereA("e7", v1, v2)
    e8 = g1.insereA("e8", v2, v3)

    ciclo = CicloEuleriano(g1)
    ciclo.Ciclo_euleriano()
    ciclo.imprime_ciclo()

