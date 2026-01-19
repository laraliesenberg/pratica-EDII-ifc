from goodman import Goodman
from copy import deepcopy

class Conjuntos:
    def __init__(self):
        self.p = {}
        self.rank = {}

    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y

            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

class Kruskal:
    def __init__(self, G):
        self.G = G
        self.sets = Conjuntos()
        self.A = []             #Lista das arestas para AGM
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
            print("\nO grafo não é conexo.")
            return False
        
        return True

    def kruskal(self):
        if not self.is_conexo():
            print("Kruskal não pode ser executado em grafo desconexo.")
            return
        
        self.A = []

        for v in self.G.lista_vertices:
            self.sets.make_set(v)   #cria um conjunto para cada vértice

        e_ordenada = sorted(self.G.lista_arestas, key=lambda e: e.peso)

        for e in e_ordenada:
            u = e.vertices[0]
            v = e.vertices[1]

            if self.sets.find_set(u) != self.sets.find_set(v):  #verifica se arestas conectam componentes diferentes 
                self.A.append(e)   #se sim, inclui a aresta na AGM
                self.sets.union(u, v)  #e uni as componentes 

        self.executou = True
        return self.A

    def imprimir_custo(self):
        if not self.executou:
            return 
        
        print("\nÁrvore Geradora Mínima (Kruskal):\n")

        total = 0
        for e in self.A:
            u, v = e.vertices
            print(f"{u.id} --({e.peso})--> {v.id}")
            total += e.peso

        print(f"\nCusto total = {total}")