class DFS:
    def __init__(self, G):
        self.G = G
        self.cor = {}
        self.pi = {}
        self.d = {}
        self.f = {}
        self.tempo = 0
        self.componentes = []

    def dfs(self):
        for v in self.G.vertices():
            self.cor[v] = "BRANCO"
            self.pi[v] = None

        self.tempo = 0
        self.conexidade = 0
        self.componentes = []
    
        for u in self.G.vertices():
            if self.cor[u] == "BRANCO":
                comp_atual = []
                self.dfs_visit(u, comp_atual)
                self.componentes.append(comp_atual)
                self.conexidade += 1

        for i in range(len(self.componentes)):
            nomes = [v.id for v in self.componentes[i]]
            print("Componente", i + 1, ":", nomes)

        print("Número de componentes conexas:", self.conexidade)

        if self.conexidade > 1:
            print("O grafo é NÃO conexo")
        else:
            print("O grafo é conexo")
            
        return self.conexidade

    def dfs_visit(self, u, comp_atual):
        self.cor[u] = "CINZA"
        self.tempo += 1
        self.d[u] = self.tempo
        comp_atual.append(u)

        for v in self.G.adj(u):
            if self.cor[v] == "BRANCO":
                self.pi[v] = u
                self.dfs_visit(v, comp_atual)
        
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