itens = [
    ["item1", 2, 40],
    ["item2", 3, 50],
    ["item3", 5, 100],
    ["item4", 4, 90]
]

capacidade_mochila = 8

for item in itens:
    item.append(item[2] / item[1])

def obter_razao(item):
    return item[3]

itens.sort(key=obter_razao, reverse=True)

peso_total = 0
valor_total = 0
itens_selecionados = []

for item in itens:
    if peso_total + item[1] <= capacidade_mochila:
        itens_selecionados.append(item[0])
        peso_total += item[1]
        valor_total += item[2]

print("Itens selecionados:", itens_selecionados)
print("Peso total:", peso_total)
print("Valor total:", valor_total)
