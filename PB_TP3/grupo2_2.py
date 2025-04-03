import multiprocessing
import time


def contar_tempo(funcao, *args):
    inicio = time.time()
    resultado = funcao(*args)
    fim = time.time()
    tempo_decorrido = fim - inicio
    return resultado, tempo_decorrido

def multiplicar_linha(argumentos):
    linha_a, matriz_b = argumentos
    tamanho = len(matriz_b[0])
    resultado_linha = []

    for j in range(tamanho):
        soma_elemento = 0
        for i in range(len(linha_a)):
            soma_elemento += linha_a[i] * matriz_b[i][j]
        resultado_linha.append(soma_elemento)

    return resultado_linha

def multiplicacao_paralela(matriz_a, matriz_b):
    linhas_matriz_a = len(matriz_a)
    argumentos = []
    for i in range(linhas_matriz_a):
        par_linha_matriz = (matriz_a[i], matriz_b)
        argumentos.append(par_linha_matriz)

    with multiprocessing.Pool(processes=linhas_matriz_a) as pool:
        matriz_resultado = pool.map(multiplicar_linha, argumentos)

    return matriz_resultado


if __name__ == "__main__":
    matriz_1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    matriz_2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
    resultado, tempo_gasto = contar_tempo(multiplicacao_paralela, matriz_1, matriz_2)

    print("Matriz resultante:")
    for linha in resultado:
        print(linha)

    print(f"Tempo de execução: {tempo_gasto:.4f} segundos")
