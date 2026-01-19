from abc import ABC, abstractmethod
from vertice import Vertice
from aresta import Aresta
    
class Grafo(ABC):  
    def __init__(self):
        self.lista_vertices = []
        self.lista_arestas = []
            
    def getOrdem(self):
        return len(self.lista_vertices) 

    def getTamanho(self):
        return len(self.lista_arestas)

    def vertices(self):
        return self.lista_vertices 

    def arestas(self):
        return self.lista_arestas

    def insereV(self, id_vertice):
        v = Vertice(id_vertice)
        self.lista_vertices.append(v)
        return v

    def removeV(self, v):
        if v in self.lista_vertices:
            for aresta in list(v.arestas):     
                self.removeA(aresta)
            self.lista_vertices.remove(v)
        else:
            None

    def insereA(self, id_aresta, u, v):
        a = Aresta(id_aresta, u, v)
        self.lista_arestas.append(a)
        return a

    def removeA(self, e):
        if e in self.lista_arestas:
            u, v = e.vertices
            if e in u.arestas:
                u.arestas.remove(e)
            if e in v.arestas:
                v.arestas.remove(e)
            self.lista_arestas.remove(e)
        else:
            None
            
    @abstractmethod
    def adj(self, v):
        pass

    def verticesA(self, e):
        lista_ids = []
        for v in e.vertices:
            lista_ids.append(v.id)
        return tuple(lista_ids)

    def oposto(self, v, e):
        x, y = e.vertices

        if x == v:
            return y
        elif y == v:
            return x
        else:
            return None
        
    def arestasE(self, v):
        lista_arestas_entrada = []
        
        for aresta in list(v.arestas):
            if aresta.vertices[1] == v:
                lista_arestas_entrada.append(aresta.id)

        return lista_arestas_entrada

    def arestasS(self, v):
        lista_arestas_saida = []

        for aresta in list(v.arestas):
            if aresta.vertices[0] == v:
                lista_arestas_saida.append(aresta.id)

        return lista_arestas_saida

    def grauE(self, v):
        return len(self.arestasE(v))

    def grauS(self, v):
        return len(self.arestasS(v))

    @abstractmethod
    def getA(self, u, v):
        pass

    def arestas_incidentes(self, v):
        arestas_incidentes = []

        for a in self.lista_arestas:
            v1, v2 = a.vertices

            if v1 == v or v2 == v:
                arestas_incidentes.append(a)

        return arestas_incidentes
