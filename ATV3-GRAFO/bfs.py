from collections import deque

class BFS:
    def __init__(self, G, s):
        self.G = G
        self.s = s
        self.d = {}
        self.pi = {}
        self.cor = {}

    def bfs(self):
        for v in self.G.vertices():
            self.cor[v] = "BRANCO"
            self.pi[v] = None
            self.d[v] = float("inf")
        
        self.d[self.s] = 0
        self.cor[self.s] = "CINZA"
        Q = deque()
        Q.append(self.s)

        while Q:
            u = Q.popleft()
            for v in self.G.adj(u):
                if self.cor[v] == "BRANCO":
                    Q.append(v)
                    self.cor[v] = "CINZA"
                    self.pi[v] = u
                    self.d[v] = self.d[u] + 1
            self.cor[u] = "PRETO"

    def imprimeTabela(self):
        print("\nTabela com as informações de cada vértice: ")
        print("--------------------------------------")
        print("| Vértice  | Predecessor | Distância |")
        print("--------------------------------------")

        for v in self.G.vertices():
            if self.pi[v] is not None:   
                predecessor = self.pi[v].id
            else: 
                predecessor = "Null"

            if self.d[v] != float("inf"):
                distancia = self.d[v]
            else:
                distancia = "∞"

            if v == self.s:
                print(f"| \033[33m{v.id:<8}\033[0m | {predecessor:^11} | {distancia:^10}|")
            else:
                print(f"| {v.id:<8} | {predecessor:^11} | {distancia:^10}|")

        print("--------------------------------------")
            