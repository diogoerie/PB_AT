class Grafo:
    def __init__(self, orientado=False):
        self.adj = {}
        self.orientado = orientado

    def adicionar_aresta(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append(v)
        if not self.orientado:
            self.adj[v].append(u)

    def construir_grafo(self, arestas):
        for u, v in arestas:
            self.adicionar_aresta(u, v)

    def mostrar_lista_adjacencia(self):
        for no in self.adj:
            print(f"{no} -> {self.adj[no]}")

class DFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitados = set()
        self.ordem_visita = []

    def busca(self, inicio):
        self._dfs(inicio)
        return self.ordem_visita

    def _dfs(self, no):
        self.visitados.add(no)
        self.ordem_visita.append(no)
        for vizinho in self.grafo.adj.get(no, []):
            if vizinho not in self.visitados:
                self._dfs(vizinho)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
grafo = Grafo(orientado=False)
grafo.construir_grafo(arestas)

dfs = DFS(grafo)

ordem = dfs.busca("A")

print("Ordem de visita:", ordem)
