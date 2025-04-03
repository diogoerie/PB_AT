import time

def contar_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

def minimo_de_moedas(moedas, valor):
    dp = [float('inf')] * (valor + 1)
    dp[0] = 0

    for moeda in moedas:
        for i in range(moeda, valor + 1):
            dp[i] = min(dp[i], 1 + dp[i - moeda])

    return dp[valor] if dp[valor] != float('inf') else -1

testes = [
    ([1, 3, 4, 7, 11, 13], 5000),
    ([1, 2, 5, 10, 20, 50, 100], 10000),
    ([3, 7, 11, 17, 23], 20000),
]
for moedas, valor in testes:
    resultado, tempo = contar_tempo(minimo_de_moedas, moedas, valor)
    print(f"Moedas disponíveis: {moedas}")
    print(f"Valor desejado: {valor}")
    print(f"Mínimo de moedas necessárias: {resultado}")
    print(f"Tempo de execução: {tempo:.5f} s")
    print()
