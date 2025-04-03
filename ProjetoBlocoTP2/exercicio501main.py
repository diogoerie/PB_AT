import random
from exercicio501 import contar_tempo, soma_sequencial, soma_paralela

lista_numeros = [random.randint(1, 1000) for _ in range(100)]

soma_seq, tempo_seq = contar_tempo(soma_sequencial, lista_numeros)
print(f"Soma Sequencial: {soma_seq} (Tempo: {tempo_seq:.6f}s)")

soma_par, tempo_par = contar_tempo(soma_paralela, lista_numeros)
print(f"Soma Paralela: {soma_par} (Tempo: {tempo_par:.6f}s)")
