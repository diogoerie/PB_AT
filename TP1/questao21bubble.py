import time

def contar_tempo(func, *args):
    inicio = time.time()
    func(*args)
    fim = time.time()
    tempo_total = fim - inicio
    return tempo_total

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break

if __name__ == "__main__":
    with open("texto.txt", "r") as file:
        lines = file.readlines()
    file_lines = lines[1:]
    tempo_gasto = contar_tempo(bubbleSort, file_lines)

    print("Linhas ordenadas:")
    for line in file_lines:
        print(line, end="")

    print(f"\nTempo de execução: {tempo_gasto:.8f}s")
