import math

cidades = {"A": (0, 0),
    "B": (1, 5),
    "C": (5, 2),
    "D": (6, 6),
    "E": (8, 3),}

def calcular_distancia(cidade1, cidade2):
    coordenadas1 = cidades[cidade1]
    coordenadas2 = cidades[cidade2]

    x1 = coordenadas1[0]
    y1 = coordenadas1[1]
    x2 = coordenadas2[0]
    y2 = coordenadas2[1]
    diferenca_x = x2 - x1
    diferenca_y = y2 - y1
    quadrado_x = diferenca_x ** 2
    quadrado_y = diferenca_y ** 2
    soma_quadrados = quadrado_x + quadrado_y
    distancia = math.sqrt(soma_quadrados)

    return distancia

def cidade_proxima(cidade_atual, nao_visitadas):
    menor_distancia = float('inf')
    cidade_proxima = None

    for cidade in nao_visitadas:
        distancia = calcular_distancia(cidade_atual, cidade)
        if distancia < menor_distancia:
            menor_distancia = distancia
            cidade_proxima = cidade

    return cidade_proxima

def caixeiro_vizinho(inicio):
    nao_visitadas = set(cidades.keys())
    rota = [inicio]
    nao_visitadas.remove(inicio)
    cidade_atual = inicio

    while nao_visitadas:
        cidade_perto = cidade_proxima(cidade_atual, nao_visitadas)
        if cidade_perto is None:
            break
        rota.append(cidade_perto)
        nao_visitadas.remove(cidade_perto)
        cidade_atual = cidade_perto

    return rota

cidade_inicial = "A"
rota_final = caixeiro_vizinho(cidade_inicial)

print("Melhor caminho encontrado:")
for i in range(len(rota_final)):
    if i == len(rota_final) - 1:
        print(rota_final[i])
    else:
        print(rota_final[i])

