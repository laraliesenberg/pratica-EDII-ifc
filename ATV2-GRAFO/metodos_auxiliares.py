class MetodosAuxiliares:
    @staticmethod
    def imprimeCaminho(pi, s, v):
            if s == v:
                print(s.id,)
                return True
            else:
                if pi[v] is None:      
                    print(f"Não existe caminho para esses vértices.")
                    return False
                else:
                    caminho = MetodosAuxiliares.imprimeCaminho(pi, s, pi[v])
                    if caminho:
                        print(v.id)
                    return caminho