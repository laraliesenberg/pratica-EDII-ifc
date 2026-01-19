from grafo_dirigido import GrafoDirigido
from grafo_nao_dirigido import GrafoNaoDirigido

if __name__ == "__main__":

    print("\n---------GRAFO NÃO DIRIGIDO---------")
    g = GrafoNaoDirigido()

    v1 = g.insereV("v1")
    v2 = g.insereV("v2")
    v3 = g.insereV("v3")

    e1 = g.insereA("e1", v1, v2)
    e2 = g.insereA("e2", v1, v3)
    e3 = g.insereA("e3", v2, v3)

    print("\nOrdem (quantidade de vértices):", g.getOrdem())
    print("Tamanho (quantidade de arestas):", g.getTamanho())

    print("\nAdjacentes de v1:", g.adj(v1))
    print("Adjacentes de v2:", g.adj(v2))
    print("Adjacentes de v3:", g.adj(v3))

    print("\nGraus:")
    print("Grau(v1):", g.grau(v1))
    print("Grau(v2):", g.grau(v2))
    print("Grau(v3):", g.grau(v3))

    print("\nTestando getA:")
    print("getA(v1, v2):", g.getA(v1, v2).imprimir_aresta())
    print("getA(v2, v1):", g.getA(v2, v1).imprimir_aresta())

    print("\nVértices opostos:")
    print("Oposto de v1:", g.oposto(v1, e1))
    print("Oposto de v2:", g.oposto(v2, e3))

    print("\nVértices que ligam a aresta e2:", g.verticesA(e2))

    print("\n-----------GRAFO DIRIGIDO-----------")
    g = GrafoDirigido()

    v1 = g.insereV("v1")
    v2 = g.insereV("v2")
    v3 = g.insereV("v3")

    e1 = g.insereA("e1", v1, v2)  
    e2 = g.insereA("e2", v2, v3)  
    e3 = g.insereA("e3", v1, v3)  

    print("\nOrdem (quantidade de vértices):", g.getOrdem())
    print("Tamanho (quantidade de arestas):", g.getTamanho())

    print("\nGraus de entrada e saída:")
    for v in g.vertices():
        print(f"{v.id}: grauE = {g.grauE(v)}, grauS = {g.grauS(v)}")

    print("\nArestas de entrada e saída:")
    print("Arestas de entrada de v3:", g.arestasE(v3))
    print("Arestas de saída de v1:", g.arestasS(v1))

    print("\nTestando getA:")
    print("getA(v1, v2):", g.getA(v1, v2).imprimir_aresta())
    print("getA(v2, v1):", g.getA(v2, v1))

    print("\nVértices opostos:")
    print("Oposto de v1:", g.oposto(v1, e3))
    print("Oposto de v2:", g.oposto(v2, e2))
    print("Oposto de v2:", g.oposto(v2, e3))

    print("\nAdjacentes de v1:", g.adj(v1))
    print("Adjacentes de v2:", g.adj(v2))
    print("Adjacentes de v3:", g.adj(v3))

    print("\nVértices que ligam a aresta e2:", g.verticesA(e2))
    
