import heapq

class Grafo:
    def __init__(self, n):
        self.n = n
        self.adj = {i: [] for i in range(n)}

    def adicionar_aresta(self, u, v, peso):
        self.adj[u].append((v, peso))
        self.adj[v].append((u, peso))

    def prim_mst(self):
        n = self.n
        p = [-1] * n
        w = [float('inf')] * n
        cor = ["branco"] * n
        w[0] = 0
        fsize = 0
        fila = [(0, 0)]
        heapq.heapify(fila)
        r = 0

        while fila:
            peso, v = heapq.heappop(fila)
            if cor[v] == "preto":
                continue
            cor[v] = "preto"
            r += peso

            for vizinho, custo in self.adj[v]:
                if cor[vizinho] == "branco" and custo < w[vizinho]:
                    w[vizinho] = custo
                    p[vizinho] = v
                    heapq.heappush(fila, (custo, vizinho))

        return r, p