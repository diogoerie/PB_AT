import time


def mover_discos(quantidade, origem, destino, auxiliar):
    if quantidade == 1:
        print(f"Mover disco de {origem} para {destino}")
        return

    mover_discos(quantidade - 1, origem, auxiliar, destino)
    print(f"Mover disco de {origem} para {destino}")
    mover_discos(quantidade - 1, auxiliar, destino, origem)


def contar_tempo(quantidade):
    inicio = time.time()
    mover_discos(quantidade, "A", "C", "B")
    fim = time.time()
    tempo_total = fim - inicio
    print(f"Tempo para resolver com {quantidade} discos: {tempo_total:.5f} segundos")


valores_de_teste = [30]

for valor in valores_de_teste:
    print(f"\nResolvendo Torres de Hanói com {valor} discos:")
    contar_tempo(valor)
