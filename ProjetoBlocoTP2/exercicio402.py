def numero_fibonacci(posicao, memoria={}):
    if posicao in memoria:
        return memoria[posicao]

    if posicao == 0:
        return 0
    if posicao == 1:
        return 1

    resultado = numero_fibonacci(posicao - 1, memoria) + numero_fibonacci(posicao - 2, memoria)
    memoria[posicao] = resultado
    return resultado


teste = [10, 11, 12, 14]

for valor in teste:
    resultado = numero_fibonacci(valor)
    print(f"O valor: {valor}, da sequência de Fibonacci é {resultado}.")
