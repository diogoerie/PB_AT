import time

def criar_heap(lista):
    tamanho = len(lista)
    for i in range(tamanho // 2 - 1, -1, -1):
        ajustar_heap(lista, tamanho, i)

def ajustar_heap(lista, tamanho, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < tamanho and lista[esquerda] > lista[maior]:
        maior = esquerda
    if direita < tamanho and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        ajustar_heap(lista, tamanho, maior)

def exibir_heap(lista):
    print(lista)


def contar_tempo(funcao, *args):
    inicio = time.time()
    resultado = funcao(*args)
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")
    return resultado

numeros = [5, 2, 3, 7, 1,0]
contar_tempo(criar_heap, numeros)
exibir_heap(numeros)
