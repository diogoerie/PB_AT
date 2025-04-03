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
        self.caminho = []

    def encontrar_caminho(self, inicio, destino):
        if self._dfs(inicio, destino):
            return self.caminho
        else:
            return None

    def _dfs(self, no, destino):
        self.visitados.add(no)
        self.caminho.append(no)

        if no == destino:
            return True

        for vizinho in self.grafo.adj.get(no, []):
            if vizinho not in self.visitados:
                if self._dfs(vizinho, destino):
                    return True

        self.caminho.pop()
        return False

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
grafo = Grafo(orientado=False)
grafo.construir_grafo(arestas)

dfs = DFS(grafo)

caminho = dfs.encontrar_caminho("A", "E")

if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Não existe caminho entre os nós.")
