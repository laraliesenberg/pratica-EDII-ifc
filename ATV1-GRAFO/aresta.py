class Aresta:
    def __init__(self, id_aresta, u, v):
        self.id = id_aresta
        self.vertices = [u, v]

        u.add_aresta(self)
        v.add_aresta(self)

    def imprimir_aresta(self):
        return f"Aresta: {self.vertices[0].id}, {self.vertices[1].id}"