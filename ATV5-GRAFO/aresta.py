class Aresta:
    def __init__(self, id_aresta, u, v, peso=1):
        self.id = id_aresta
        self.vertices = [u, v]
        self.peso = peso

        u.add_aresta(self)
        v.add_aresta(self)

    def imprimeAresta(self):
        return f"Aresta: {self.vertices[0].id}, {self.vertices[1].id}"
    
