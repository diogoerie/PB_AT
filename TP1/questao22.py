import time
import tracemalloc
from collections import deque


def contar_tempo(func, *args):
    tempo_inicial = time.time()
    resultado = func(*args)
    tempo_final = time.time()
    tempo_decorrido = tempo_final - tempo_inicial
    return resultado, tempo_decorrido

def contar_memoria(func, *args):
    tracemalloc.start()
    resultado = func(*args)
    memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return resultado, memoria[1]

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as file:
        lines = file.readlines()

    return [line.split()[-1] for line in lines[1:]]

def criar_hashtable(lista):
    hashtable = set()
    for arquivo in lista:
        hashtable.add(arquivo)
    return hashtable

def criar_pilha(lista):
    pilha = []
    for arquivo in lista:
        pilha.append(arquivo)
    return pilha

def criar_fila(lista):
    fila = deque()
    for arquivo in lista:
        fila.append(arquivo)
    return fila

def achar_nomes(estrutura):
    indices = [0, 99, 999, 4999, len(estrutura) - 1]
    resultados = []

    if isinstance(estrutura, set):
        estrutura = list(estrutura)

    for idx in indices:
        if 0 <= idx < len(estrutura):
            resultados.append(estrutura[idx])
        else:
            resultados.append("Nao foi possivel encontrar.")

    return resultados


if __name__ == "__main__":
    nome_arquivo = "texto.txt"

    lista_arquivos, tempo_leitura = contar_tempo(ler_arquivo, nome_arquivo)
    print(f"Tempo para ler o arquivo: {tempo_leitura:.8f} segundos")

    hashtable, tempo_hashtable = contar_tempo(criar_fila, lista_arquivos)
    arquivos_hash, memoria_hashtable = contar_memoria(achar_nomes, hashtable)
    print(f"Hashtable - Tempo: {tempo_hashtable:.8f}s")
    print(f"Memória: {memoria_hashtable / 1024:.2f} KB")
    print("Nomes:", arquivos_hash)
    print()

    pilha, tempo_pilha = contar_tempo(criar_pilha, lista_arquivos)
    arquivos_pilha, memoria_pilha = contar_memoria(achar_nomes, pilha)
    print(f"Pilha - Tempo: {tempo_pilha:.8f}s")
    print(f"Memória: {memoria_pilha / 1024:.2f} KB")
    print("Nomes:", arquivos_pilha)
    print()

    fila, tempo_fila = contar_tempo(criar_fila, lista_arquivos)
    arquivos_fila, memoria_fila = contar_memoria(achar_nomes, fila)
    print(f"Fila - Tempo: {tempo_fila:.8f}s")
    print(f"Memória: {memoria_fila / 1024:.2f} KB")
    print("Nomes:", arquivos_fila)
