def quicksort(lista_estudantes):
    if len(lista_estudantes) <= 1:
        return lista_estudantes

    pivo = lista_estudantes[-1]
    restante = lista_estudantes[:-1]
    menores = []
    maiores = []

    for estudante in restante:
        if estudante["nota"] <= pivo["nota"]:
            menores.append(estudante)
        else:
            maiores.append(estudante)

    return quicksort(menores) + [pivo] + quicksort(maiores)

estudantes = [{"nome": "Ana", "nota": 8.5},{"nome": "Bruno", "nota": 7.2},{"nome": "Carla", "nota": 9.1},
    {"nome": "Daniel", "nota": 6.8},{"nome": "Eduarda", "nota": 7.9},{"nome": "Fernando", "nota": 5.4},
    {"nome": "Gabriela", "nota": 8.9}
]

estudantes_ordenados = quicksort(estudantes)

print("Lista de estudantes ordenada por nota:")
for estudante in estudantes_ordenados:
    print(f"{estudante['nome']}: {estudante['nota']}")
