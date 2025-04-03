from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

def bfs(graph, start):
    num = [-1] * graph.V
    parent = [-1] * graph.V
    queue = deque()

    num[start] = 0
    parent[start] = start
    queue.append(start)
    cnt = 1

    while queue:
        v = queue.popleft()
        for neighbor in graph.adj[v]:
            if num[neighbor] == -1:
                num[neighbor] = cnt
                parent[neighbor] = v
                queue.append(neighbor)
                cnt += 1

    return num, parent

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

num, parent = bfs(g, 0)
print("Número de visita:", num)
print("Pais no caminho da BFS:", parent)
