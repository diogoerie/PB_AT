class GrafoLogistica:
    def __init__(self):
        self.bairros = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.bairros:
            self.bairros[bairro] = {}

    def adicionar_rua(self, bairro1, bairro2, distancia):
        self.bairros[bairro1][bairro2] = distancia
        self.bairros[bairro2][bairro1] = distancia

    def dijkstra(self, origem):
        nao_visitados = list(self.bairros.keys())
        distancias = {}
        for bairro in self.bairros:
            distancias[bairro] = float("inf")

        distancias[origem] = 0
        predecessores = {}

        while nao_visitados:
            bairro_atual = min(nao_visitados, key=lambda bairro: distancias[bairro])
            if distancias[bairro_atual] == float("inf"):
                break

            for vizinho, distancia in self.bairros[bairro_atual].items():
                nova_distancia = distancias[bairro_atual] + distancia
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = bairro_atual

            nao_visitados.remove(bairro_atual)

        return distancias, predecessores

    def rota_mais_curta(self, origem, destino, predecessores):
        caminho = []
        bairro_atual = destino
        while bairro_atual in predecessores:
            caminho.append(bairro_atual)
            bairro_atual = predecessores[bairro_atual]
        caminho.append(origem)
        caminho.reverse()
        return caminho

mapa_bairros = GrafoLogistica()
bairros = ["Centro", "Bairro1", "Bairro2", "Bairro3", "Bairro4"]

for bairro in bairros:
    mapa_bairros.adicionar_bairro(bairro)

ruas = [
    ("Centro", "Bairro1", 5),
    ("Centro", "Bairro2", 10),
    ("Bairro1", "Bairro3", 8),
    ("Bairro2", "Bairro3", 2),
    ("Bairro3", "Bairro4", 6)
]

for bairro1, bairro2, distancia in ruas:
    mapa_bairros.adicionar_rua(bairro1, bairro2, distancia)

origem = "Centro"
distancias, predecessores = mapa_bairros.dijkstra(origem)
total_rotas = {}

for bairro in bairros:
    if bairro != origem:
        rota_mais_curta = mapa_bairros.rota_mais_curta(origem, bairro, predecessores)
        total_rotas[bairro] = rota_mais_curta


for bairro, rota in total_rotas.items():
    print("A menor rota para o bairro ",bairro,rota,"tem a distância de ",distancias[bairro])