import time

def contar_tempo(func, *args):
    inicio = time.time()
    func(*args)
    fim = time.time()
    tempo_total = fim - inicio
    return tempo_total

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    with open("texto.txt", "r") as file:
        lines = file.readlines()
    file_lines = lines[1:]
    tempo_gasto = contar_tempo(insertionSort, file_lines)

    print("Linhas ordenadas:")
    for line in file_lines:
        print(line, end="")

    print(f"\nTempo de execução: {tempo_gasto:.8f} segundos")
