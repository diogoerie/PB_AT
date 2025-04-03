import random
import time

def contar_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def quickSelect(arr, l, r, k):
    if 0 < k <= r - l + 1:
        index = partition(arr, l, r)
        if index - l == k - 1:
            return arr[index]
        if index - l > k - 1:
            return quickSelect(arr, l, index - 1, k)
        return quickSelect(arr, index + 1, r, k - (index - l + 1))
    return None

def acharMedia(arr):
    n = len(arr)
    if n % 2 == 1:
        return quickSelect(arr, 0, n - 1, n // 2 + 1)
    else:
        med1 = quickSelect(arr, 0, n - 1, n // 2)
        med2 = quickSelect(arr, 0, n - 1, n // 2 + 1)
        return (med1 + med2) / 2

def menoresNumeros(arr, k):
    resultado = []
    for i in range(k):
        resultado.append(quickSelect(arr, 0, len(arr) - 1, i + 1))
    return resultado


arr = [random.randint(1, 1000) for _ in range(1000)]
k = 3

media, tempo_mediana = contar_tempo(acharMedia, arr[:])
print(f"media: {media} (Tempo: {tempo_mediana:.6f}s)")
k_menores, tempo_menores = contar_tempo(menoresNumeros, arr[:], k)
print(f"Menores numeros: {k_menores} (Tempo: {tempo_menores:.8f}s)")
