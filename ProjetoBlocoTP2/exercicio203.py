import random


def trocar(numeros, i, j):
    elemento_temporario = numeros[i]
    numeros[i] = numeros[j]
    numeros[j] = elemento_temporario

def particionar(numeros, indice_esquerda, indice_direita, indice_pivo):
    pivo = numeros[indice_pivo]
    trocar(numeros, indice_pivo, indice_direita)
    indice_pivo = indice_esquerda
    for i in range(indice_esquerda, indice_direita):
        if numeros[i] <= pivo:
            trocar(numeros, i, indice_pivo)
            indice_pivo += 1
    trocar(numeros, indice_pivo, indice_direita)
    return indice_pivo

def quickselect(numeros, indice_esquerda, indice_direita, k):
    if indice_esquerda == indice_direita:
        return numeros[indice_esquerda]
    indice_pivo = random.randint(indice_esquerda, indice_direita)
    indice_pivo = particionar(numeros, indice_esquerda, indice_direita, indice_pivo)

    if k == indice_pivo:
        return numeros[k]
    elif k < indice_pivo:
        return quickselect(numeros, indice_esquerda, indice_pivo - 1, k)
    else:
        return quickselect(numeros, indice_pivo + 1, indice_direita, k)
for i in range(10):
    lista_teste = [random.randint(1, 1000) for _ in range(10000)]
    valores_k = [1, 10, 100, 500, 1000]
    print(f"\nTeste {i + 1}:")

    for k in valores_k:
        lista_copia = lista_teste[:]
        k_esimo_menor = quickselect(lista_copia, 0, len(lista_copia) - 1, k - 1)
        print(f"O {k}-ésimo menor elemento é: {k_esimo_menor}")

