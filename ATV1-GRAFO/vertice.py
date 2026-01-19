class Vertice:
    def __init__(self, id_vertice):
        self.id = id_vertice
        self.arestas = []           #self.arestas não existe na classe, só existe em cada objeto criado(v1, v2, ...)

    def add_aresta(self, aresta):
        if aresta not in self.arestas:
            self.arestas.append(aresta)

    def imprimir_vertice(self):
        return f"Vértice: {self.id}"