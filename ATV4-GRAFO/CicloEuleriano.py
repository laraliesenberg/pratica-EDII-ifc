from grafo import Grafo
from copy import deepcopy
from goodman import Goodman
from grafo_nao_dirigido import GrafoNaoDirigido

class CicloEuleriano:
    def __init__(self, G):
        self.G_original = G
        self.H = deepcopy(G)
        self.Vvisit = []
        self.s = self.H.lista_vertices[0]
        self.nVvisit = 1
        self.nextEdge = {}
        self.prevEdge = {}
        self.eulerEdge = {}

    def is_connected(self):
        goodman = Goodman(self.G_original)
        componentes = goodman.goodman()
        componentes = [c for c in componentes if len(c) > 0]
        return len(componentes) == 1

    def is_eulerian(self):
        euleriano = True
        if self.is_connected():
            print("O grafo é conexo.")
        else:
            print("O grafo não é conexo.")
            euleriano = False
        for v in self.H.lista_vertices:
            if self.H.grau(v) % 2 != 0:
                print(f"O vértice {v.id} tem grau ímpar ({self.H.grau(v)}).")
                euleriano = False
        return euleriano
    

    def Ciclo_euleriano(self): 
        self.Vvisit.append(self.s)
        k = 0
        
        while k < self.nVvisit:
            u = self.Vvisit[k]
            Iu = self.H.arestas_incidentes(u)

            while Iu:
                e0 = Iu[0]
                v = self.H.oposto(u, e0)
                self.H.removeA(e0)
                e1 = e0

                while v != u:
                    if v not in self.Vvisit:
                        self.nVvisit += 1
                        self.Vvisit.append(v)
                    
                    Iv = self.H.arestas_incidentes(v)
                    if not Iv:
                        break
                    e2 = Iv[0]
                    self.nextEdge[e1] = e2
                    self.prevEdge[e2] = e1

                    if v not in self.eulerEdge:
                        self.eulerEdge[v] = e2

                    e1 = e2
                    v = self.H.oposto(v, e1)
                    self.H.removeA(e1)
                
                self.prevEdge[e0] = e1
                self.nextEdge[e1] = e0

                if u not in self.eulerEdge:
                    self.eulerEdge[u] = e0
                else:
                    e1 = self.eulerEdge[u]
                    e2 = self.prevEdge[e1]
                    e3 = self.prevEdge[e0]
                    self.nextEdge[e2] = e0
                    self.nextEdge[e3] = e1
                
                Iu = self.H.arestas_incidentes(u)

            k += 1

    def imprime_ciclo(self):
        if not self.is_eulerian():
            print("O grafo não é euleriano.")
            return None
        
        print("\nCiclo euleriano encontrado:")

        e_inicial = self.eulerEdge[self.s]      
        e = e_inicial
        u = self.s                             
        ciclo_vertices = [u.id]  
        visitadas = set()              

        while e not in visitadas:
            visitadas.add(e)
            v = self.H.oposto(u, e)
            ciclo_vertices.append(v.id)
            e = self.nextEdge.get(e)
            if e is None:
                break
            u = v

        print(" → ".join(ciclo_vertices))