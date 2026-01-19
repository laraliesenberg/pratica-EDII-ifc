from copy import deepcopy

class Goodman:
    def __init__(self, G):
        self.H = deepcopy(G)
        self.conexidade = 0
        self.componentes = []

    def fusao(self, w, u):
        for vizinho in self.H.adj(u):
            if vizinho != w:
                if self.H.getA(w, vizinho) is None:
                    self.H.insereA(f"f_{w.id}_{vizinho.id}", w, vizinho)
        self.H.removeV(u)

    def goodman(self):
        while len(self.H.vertices()) > 0:
            w = self.H.vertices()[0]
            vizinhos = self.H.adj(w)
            comp_atual = [w.id]

            while vizinhos:
                u = vizinhos[0]
                comp_atual.append(u.id)
                self.fusao(w, u)
                vizinhos = self.H.adj(w)
            
            self.H.removeV(w) 
            self.conexidade += 1
            self.componentes.append(comp_atual)

        for i in range(len(self.componentes)):
            print("Componente", i + 1, ":", self.componentes[i])

        print("Número de componentes conexas: ", self.conexidade)

        if self.conexidade > 1:
            print("O grafo é NÃO conexo")
        else:
            print("O grafo é conexo")