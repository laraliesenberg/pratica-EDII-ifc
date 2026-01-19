class DFS:
    def __init__(self, G):
        self. G = G
        self.cor = {}
        self.pi = {}
        self.d = {}
        self.f = {}
        self.tempo = 0

    def dfs(self):
        for v in self.G.vertices():
            self.cor[v] = "BRANCO"
            self.pi[v] = None

        self.tempo = 0

        for u in self.G.vertices():
            if self.cor[u] == "BRANCO":
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.cor[u] = "CINZA"
        self.tempo += 1
        self.d[u] = self.tempo

        for v in self.G.adj(u):
            if self.cor[v] == "BRANCO":
                self.pi[v] = u
                self.dfs_visit(v)
        
        self.cor[u] = "PRETO"
        self.tempo += 1
        self.f[u] = self.tempo

    def imprimeTabela(self):
        print("\nTabela com as informações de cada vértice: ")
        print("---------------------------------------------------")
        print("| Vértice  | Predecessor | Descoberta | Fechamento |")
        print("---------------------------------------------------")

        for v in self.G.vertices():
            if self.pi[v] is not None:   
                predecessor = self.pi[v].id
            else: 
                predecessor = "Null"

            descoberta = self.d[v]
            fechamento = self.f[v]

            if self.d[v] == 1:
                print(f"| \033[33m{v.id:<8}\033[0m | {predecessor:^11} | {descoberta:^10} | {fechamento:^11}|")
            else:
                print(f"| {v.id:<8} | {predecessor:^11} | {descoberta:^10} | {fechamento:^11}|")

        print("---------------------------------------------------")