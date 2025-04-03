from cython.parallel import prange
import numpy as np
import time


def contar_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio


def soma_paralela(int[:] vetor):
    cdef long long soma = 0
    cdef int i

for i in prange(len(vetor), nogil=True):
    soma += vetor[i]

return soma
