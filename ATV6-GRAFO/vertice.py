class Vertice:
    def __init__(self, id_vertice):
        self.id = id_vertice
        self.arestas = []           

    def add_aresta(self, aresta):
        if aresta not in self.arestas:
            self.arestas.append(aresta)

    def imprimeVertice(self):
        return f"Vértice: {self.id}"