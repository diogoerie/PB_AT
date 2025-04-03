def maiorSequencia(X, Y):
    m, n = len(X), len(Y)
    tabela = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1])

    i, j = m, n
    comums = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            comums.append(X[i - 1])
            i -= 1
            j -= 1
        elif tabela[i - 1][j] >= tabela[i][j - 1]:
            i -= 1
        else:
            j -= 1
    comums.reverse()
    return tabela[m][n], ''.join(comums)


X = "AGGTABXQWER"
Y = "GXTXAYBQWER"
comprimento, sequencia = maiorSequencia(X, Y)

print("Comprimento da sequência:", comprimento)
print("Maior sequência:", sequencia)
