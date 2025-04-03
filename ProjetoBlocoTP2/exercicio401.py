def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * calcular_fatorial(numero - 1)

valores_de_teste = [2, 7, 13, 12, 10]

for valor in valores_de_teste:
    resultado = calcular_fatorial(valor)
    print(f"O fatorial de {valor} é {resultado}")
