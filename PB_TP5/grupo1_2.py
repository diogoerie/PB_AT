import heapq

class Grafo:
    def __init__(self):
        self.adj = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append((v, peso))
        self.adj[v].append((u, peso))

    def prim_mst(self, origem):
        p = {}
        for v in self.adj:
            p[v] = None
        w = {}
        for v in self.adj:
            w[v] = float('inf')
        cor = {}
        for v in self.adj:
            cor[v] = "branco"

        w[origem] = 0
        r = 0
        fila = [(0, origem)]
        heapq.heapify(fila)

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

        return r, p, w

    def exibir_mst(self, origem):
        r, p, w = self.prim_mst(origem)
        for v in self.adj:
            if p[v] is not None:
                print(f"{p[v]} - {v} com peso {w[v]}")

grafo = Grafo()
grafo.adicionar_aresta("A", "B", 2)
grafo.adicionar_aresta("A", "C", 3)
grafo.adicionar_aresta("B", "C", 1)
grafo.adicionar_aresta("B", "D", 4)
grafo.adicionar_aresta("C", "D", 5)

grafo.exibir_mst("A")
