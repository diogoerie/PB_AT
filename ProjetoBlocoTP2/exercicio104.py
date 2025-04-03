import time
import random

def medir_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

def quicksort(lista, escolha_pivo="ultimo"):
    if len(lista) <= 1:
        return lista

    if escolha_pivo == "primeiro":
        pivo = lista[0]
        restante = lista[1:]
    elif escolha_pivo == "mediano":
        meio = len(lista) // 2
        candidatos = [lista[0], lista[meio], lista[-1]]
        pivo = sorted(candidatos)[1]
        restante = [x for x in lista if x != pivo]
    else:
        pivo = lista[-1]
        restante = lista[:-1]

    menores = []
    maiores = []

    for x in restante:
        if x <= pivo:
            menores.append(x)
        else:
            maiores.append(x)

    return quicksort(menores, escolha_pivo) + [pivo] + quicksort(maiores, escolha_pivo)

lista_teste = [random.randint(1, 10000) for _ in range(1000)]

tipos_pivo = ["primeiro", "mediano", "ultimo"]
for tipo in tipos_pivo:
    lista_ordenada, tempo_gasto = medir_tempo(quicksort, lista_teste, tipo)
    print(f"{tipo} : Lista: {lista_ordenada[:10]}, Tempo: {tempo_gasto:.6f}")
