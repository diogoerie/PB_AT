class Arvore_no:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Arvore_no(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = Arvore_no(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = Arvore_no(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def verificar_bst(self):
        return self._verificar_bst_recursivo(self.raiz, float('-inf'), float('inf'))

    def _verificar_bst_recursivo(self, no_atual, minimo, maximo):
        if no_atual is None:
            return True
        if not (minimo < no_atual.valor < maximo):
            return False
        return (self._verificar_bst_recursivo(no_atual.esquerda, minimo, no_atual.valor) and
                self._verificar_bst_recursivo(no_atual.direita, no_atual.valor, maximo))

arvore = ArvoreBinariaDeBusca()
valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    arvore.inserir(valor)

print("Antes da modificação:")
if arvore.verificar_bst():
    print("A árvore é uma BST válida.")
else:
    print("A árvore NÃO é uma BST válida.")

arvore.raiz.esquerda.direita.valor = 100

print("\nDepois da modificação:")
if arvore.verificar_bst():
    print("A árvore é uma BST válida.")
else:
    print("A árvore NÃO é uma BST válida.")
