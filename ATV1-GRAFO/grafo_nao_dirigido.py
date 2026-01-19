from grafo import Grafo

class GrafoNaoDirigido(Grafo):
    def getA(self, u, v):
        for aresta in self.lista_arestas:
            x, y = aresta.vertices

            if(x == u and y == v) or (y == u and x == v):
                return aresta
            
        return None
    
    def grau(self, v):
        return len(v.arestas)
    
    def adj(self, v):
        vertices_adjacentes = []

        for aresta in v.arestas:
            x, y = aresta.vertices

            if x == v and y not in vertices_adjacentes:
                vertices_adjacentes.append(y.id)
            elif y == v and x not in vertices_adjacentes:
                vertices_adjacentes.append(x.id)

        return vertices_adjacentes