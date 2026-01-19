import math 

class FloydWarshall:
    def __init__(self, G):
        self.G = G
        self.vertices = G.lista_vertices
        self.n = len(self.vertices)

        self.D = [[math.inf] * self.n for _ in range(self.n)]  
        self.P = [[None] * self.n for _ in range(self.n)]      
        self._prepara_matrizes()

    def _prepara_matrizes(self):
        for i, vi in enumerate(self.vertices):
            self.D[i][i] = 0

            for (vj, peso) in self.G.adj(vi): 
                j = self.vertices.index(vj)
                self.D[i][j] = peso
                self.P[i][j] = vi             

    def executar(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):

                    if self.D[i][k] + self.D[k][j] < self.D[i][j]:
                        self.D[i][j] = self.D[i][k] + self.D[k][j]
                        self.P[i][j] = self.P[k][j]

    def imprimir_caminho(self, s, t):
        i = self.vertices.index(s)
        j = self.vertices.index(t)

        if self.P[i][j] is None:
            print(f"Não existe caminho de {s.id} até {t.id}")
            return

        print(f"\nMenor caminho de {s.id} até {t.id}: ", end="")
        self._print_path(i, j)
        print()

    def _print_path(self, i, j):
        if i == j:
            print(self.vertices[i].id, end=" ")
        elif self.P[i][j] is None:
            print(" SEM CAMINHO ", end="")
        else:
            self._print_path(i, self.vertices.index(self.P[i][j]))
            print(self.vertices[j].id, end=" ")