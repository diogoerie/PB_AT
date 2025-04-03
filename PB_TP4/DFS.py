class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.pre = [-1] * graph.V
        self.cnt = 0

    def search(self):
        for v in range(self.graph.V):
            if self.pre[v] == -1:
                self._dfs(v)

    def _dfs(self, v):
        self.pre[v] = self.cnt
        self.cnt += 1
        for w in self.graph.adj[v]:
            if self.pre[w] == -1:
                self._dfs(w)
