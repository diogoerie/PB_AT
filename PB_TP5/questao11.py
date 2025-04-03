class GrafoLog:
    def __init__(self):
        self.pontos = {}

    def adicionar_ponto(self, ponto):
        if ponto not in self.pontos:
            self.pontos[ponto] = {}

    def adicionar_caminho(self, pontoA, pontoB, distancia):
        if pontoA not in self.pontos:
            self.adicionar_ponto(pontoA)
        if pontoB not in self.pontos:
            self.adicionar_ponto(pontoB)

        self.pontos[pontoA][pontoB] = distancia
        self.pontos[pontoB][pontoA] = distancia

    def dijkstra(self, origem):
        nao_visitados = list(self.pontos.keys())
        distancias = {ponto: float("inf") for ponto in self.pontos}
        predecessores = {}

        distancias[origem] = 0

        while nao_visitados:
            ponto_atual = min(nao_visitados, key=lambda ponto: distancias[ponto])

            if distancias[ponto_atual] == float("inf"):
                break

            for vizinho, distancia in self.pontos[ponto_atual].items():
                nova_distancia = distancias[ponto_atual] + distancia
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = ponto_atual

            nao_visitados.remove(ponto_atual)

        return distancias, predecessores

    def rota_mais_curta(self, origem, destino, predecessores):
        caminho = []
        ponto_atual = destino
        while ponto_atual in predecessores:
            caminho.append(ponto_atual)
            ponto_atual = predecessores[ponto_atual]
        caminho.append(origem)
        caminho.reverse()
        return caminho

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

mapa_pontos = GrafoLog()

for ponto in grafo:
    mapa_pontos.adicionar_ponto(ponto)

for pontoA, vizinhos in grafo.items():
    for pontoB, distancia in vizinhos:
        mapa_pontos.adicionar_caminho(pontoA, pontoB, distancia)

origem = "A"
distancias, predecessores = mapa_pontos.dijkstra(origem)

for ponto, distancia in distancias.items():
    print(ponto,distancia)
