class Dijkstra:
    def __init__(self, G):
        self.G = G
        self.distancia = {}
        self.pi = {}

    def relax(self, u, v, peso):
        if self.distancia[v] > self.distancia[u] + peso:  #se o caminho atual para v pasando por u for melhor
            self.distancia[v] = self.distancia[u] + peso
            self.pi[v] = u

    def dijkstra(self, s):
        for v in self.G.lista_vertices:
            self.distancia[v] = float("inf")
            self.pi[v] = None

        self.distancia[s] = 0

        Q = set(self.G.lista_vertices) 

        while Q:
            u = min(Q, key=lambda x: self.distancia[x])
            Q.remove(u)

            for (v, peso) in self.G.adj(u): #para cada viznho v de u, verifica melhor caminho
                self.relax(u, v, peso)

    def imprime_caminho(self, s, v):
        if self.distancia[v] == float("inf"):
            print(f"Não existe caminho de {s.id} até {v.id}")
            return

        caminho = []
        atual = v

        while atual is not None:
            caminho.append(atual.id)
            atual = self.pi[atual]

        caminho.reverse()

        print("\nMenor caminho encontrado:")
        print(" → ".join(caminho))
        print(f"Distância total = {self.distancia[v]}") 