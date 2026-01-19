from goodman import Goodman
from copy import deepcopy

class Prim:
    def __init__(self, G):
        self.G = G
        self.chave = {}
        self.pi = {}
        self.executou = False
    
    def is_conexo(self):
        goodman = Goodman(deepcopy(self.G))
        componentes = goodman.goodman()
        componentes_filtradas = []

        for c in componentes:
            if len(c) > 0:
                componentes_filtradas.append(c)

        componentes = componentes_filtradas

        if len(componentes) != 1:
            print("O grafo não é conexo.")
            return False
        
        return True
    
    
    def remove_minimo(self, Q):
        minimo = Q[0]
        for v in Q:
            if self.chave[v] < self.chave[minimo]:
                minimo = v
            
        Q.remove(minimo)
        return minimo
    
    def relax(self, u, v, peso):
        if self.chave[v] > peso:   #atualiza sua chave se tiver uma aresta mais barata
            self.chave[v] = peso
            self.pi[v] = u

    def prim(self, r):
        if not self.is_conexo():
            print("Prim não pode ser executado em grafo desconexo.")
            return
        
        Q = list(self.G.lista_vertices)

        for u in Q:
            self.chave[u] = float("inf")
            self.pi[u] = None

        self.chave[r] = 0
        self.pi[r] = None

        while len(Q) > 0:
            u = self.remove_minimo(Q)

            for (v, peso) in self.G.adj(u):
                if v in Q and peso < self.chave[v]:
                    self.relax(u, v, peso)

        self.executou = True

    def imprimi_custo(self):
        if not self.executou:
            return 
        
        print("\nÁrvore Geradora Mínima (Prim):\n")
        custo_total = 0

        for v in self.G.lista_vertices:
            if self.pi[v] is not None:
                print(f"{self.pi[v].id} --({self.chave[v]})--> {v.id}")
                custo_total += self.chave[v]

        print(f"\nCusto total = {custo_total}")