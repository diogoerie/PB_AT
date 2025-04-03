class Elemento:
    def iniciar(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def iniciar(self):
        self.inicio = None

    def inserir_no_comeco(self, valor):
        novo_elemento = Elemento()
        novo_elemento.iniciar(valor)

        if self.inicio is None:
            self.inicio = novo_elemento
        else:
            novo_elemento.proximo = self.inicio
            self.inicio = novo_elemento

    def inserir_no_fim(self, valor):
        novo_elemento = Elemento()
        novo_elemento.iniciar(valor)

        if self.inicio is None:
            self.inicio = novo_elemento
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_elemento

    def excluir_elemento(self, valor):
        if self.inicio is None:
            return

        if self.inicio.valor == valor:
            self.inicio = self.inicio.proximo
            return

        atual = self.inicio
        anterior = None

        while atual is not None and atual.valor != valor:
            anterior = atual
            atual = atual.proximo

        se_encontrado = atual is not None
        if se_encontrado:
            anterior.proximo = atual.proximo

    def exibir_lista(self):
        atual = self.inicio
        while atual is not None:
            print(atual.valor, end=" - ")
            atual = atual.proximo
        print("None")


lista = ListaEncadeada()
lista.iniciar()

lista.inserir_no_comeco(3)
lista.inserir_no_comeco(2)
lista.inserir_no_comeco(1)
lista.inserir_no_fim(4)
lista.inserir_no_fim(5)

lista.exibir_lista()

lista.excluir_elemento(3)

lista.exibir_lista()
