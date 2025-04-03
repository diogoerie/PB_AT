import time

def contar_tempo(func, *args):
    inicio = time.time()
    func(*args)
    fim = time.time()
    tempo_total = fim - inicio
    return tempo_total

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    with open("texto.txt", "r") as file:
        lines = file.readlines()
    file_lines = lines[1:]
    tempo_gasto = contar_tempo(selection_sort, file_lines)
    print("Linhas ordenadas:")
    for line in file_lines:
        print(line, end="")

    print(f"\nTempo de execução: {tempo_gasto:.8f} segundos")
