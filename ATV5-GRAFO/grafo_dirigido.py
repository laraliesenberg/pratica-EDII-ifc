from grafo import Grafo

class GrafoDirigido(Grafo):
    def getA(self, u, v):
        for aresta in self.lista_arestas:
            x, y = aresta.vertices
            if x == u and y == v:
                return aresta
        return None
    
    def adj(self, v):
        vertices_adjacentes = []

        for aresta in v.arestas:
            x, y = aresta.vertices

            if x == v and y not in vertices_adjacentes:
                vertices_adjacentes.append((y, aresta.peso))
            
        return vertices_adjacentes