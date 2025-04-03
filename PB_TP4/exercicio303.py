from collections import deque

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

def bfs(grafo, inicio):
    num = {no: -1 for no in grafo.adj}
    parent = {no: None for no in grafo.adj}
    queue = deque()

    num[inicio] = 0
    parent[inicio] = inicio
    queue.append(inicio)
    cnt = 1
    ordem_visita = []

    while queue:
        v = queue.popleft()
        ordem_visita.append(v)
        for vizinho in grafo.adj[v]:
            if num[vizinho] == -1:
                num[vizinho] = cnt
                parent[vizinho] = v
                queue.append(vizinho)
                cnt += 1

    return ordem_visita, num, parent

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
grafo = Grafo(orientado=False)
grafo.construir_grafo(arestas)

ordem_visita, num, parent = bfs(grafo, "A")

print("Ordem de visita:", ordem_visita)
print("Número de visita:", num)
print("Pais no caminho da BFS:", parent)
