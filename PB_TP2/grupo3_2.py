class DNode:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class DoublyLinkedList:
    def __init__(self):
        self.cabeca = None
        self.ultimo = None

    def inserir_no_inicio(self, valor):
        novo_no = DNode(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
            self.ultimo = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no

    def inserir_no_final(self, valor):
        novo_no = DNode(valor)
        if self.ultimo is None:
            self.cabeca = novo_no
            self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            novo_no.anterior = self.ultimo
            self.ultimo = novo_no

    def excluir_na_posicao(self, posicao):
        if self.cabeca is None:
            print("A lista está vazia.")
            return

        no_atual = self.cabeca
        contador = 0

        while no_atual is not None and contador < posicao:
            no_atual = no_atual.proximo
            contador += 1

        if no_atual is None:
            print("Posição da lista.")
            return

        if no_atual == self.cabeca:
            self.cabeca = no_atual.proximo
            if self.cabeca is not None:
                self.cabeca.anterior = None
            if no_atual == self.ultimo:
                self.ultimo = None

        elif no_atual == self.ultimo:
            self.ultimo = no_atual.anterior
            if self.ultimo is not None:
                self.ultimo.proximo = None

        else:
            no_atual.anterior.proximo = no_atual.proximo
            no_atual.proximo.anterior = no_atual.anterior

    def exibir_lista_direta(self):
        if self.cabeca is None:
            print("A lista está vazia.")
            return
        no_atual = self.cabeca
        while no_atual is not None:
            print(no_atual.valor, end=" ")
            no_atual = no_atual.proximo
        print()

    def exibir_lista_reversa(self):
        if self.ultimo is None:
            print("A lista está vazia.")
            return
        no_atual = self.ultimo
        while no_atual is not None:
            print(no_atual.valor, end=" ")
            no_atual = no_atual.anterior
        print()
