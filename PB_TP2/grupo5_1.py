import random
import time
from cython.parallel import prange
from libc.stdlib import malloc, free

def contar_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

def soma_sequencial(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

def soma_paralela(lista):
    cdef int i, n = len(lista)
    cdef long soma = 0
    cdef long[:] vetor = np.array(lista, dtype=np.int64)

    for i in prange(n, nogil=True):
        soma += vetor[i]

    return soma
