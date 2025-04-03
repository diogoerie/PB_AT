import multiprocessing
import time


def contar_tempo(funcao, *args):
    inicio = time.time()
    resultado = funcao(*args)
    fim = time.time()
    tempo_decorrido = fim - inicio
    return resultado, tempo_decorrido


def somar_parte(lista):
    return sum(lista)


def soma_paralela(numeros, partes):
    tamanho_parte = len(numeros) // partes
    partes_lista = []

    for i in range(partes):
        inicio = i * tamanho_parte
        fim = (i + 1) * tamanho_parte
        parte = numeros[inicio:fim]
        partes_lista.append(parte)

    with multiprocessing.Pool(processes=partes) as pool:
        resultado = pool.map(somar_parte, partes_lista)

    return sum(resultado)


if __name__ == "__main__":
    limite = 10_000_000
    lista_numeros = list(range(1, limite + 1))
    total_nucleos = multiprocessing.cpu_count()

    resultado_final, tempo_gasto = contar_tempo(soma_paralela, lista_numeros, total_nucleos)

    print(f"Soma total de 1 até {limite}: {resultado_final}")
    print(f"Tempo de execução: {tempo_gasto}.")
