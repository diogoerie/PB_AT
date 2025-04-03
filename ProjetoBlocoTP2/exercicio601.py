import time
import random


def contar_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

def mochila_calculo(capacidade, pesos, valores, n):
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                tabela[i][w] = max(valores[i - 1] + tabela[i - 1][w - pesos[i - 1]], tabela[i - 1][w])
            else:
                tabela[i][w] = tabela[i - 1][w]

    return tabela[n][capacidade]

tamanhos = [10, 100, 1000]
capacidade_mochila = 50

for tamanho in tamanhos:
    pesos = [random.randint(1, 20) for _ in range(tamanho)]
    valores = [random.randint(10, 100) for _ in range(tamanho)]
    resultado, tempo = contar_tempo(mochila_calculo, capacidade_mochila, pesos, valores, tamanho)

    print("Número de itens:",tamanho)
    print("Valor máximo:",resultado)
    print("Tempo de execução:",tempo,"s")
    print()
