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

    def percurso_em_ordem(self):
        return self._percurso_em_ordem_recursivo(self.raiz)

    def _percurso_em_ordem_recursivo(self, no_atual):
        elementos = []
        if no_atual:
            elementos += self._percurso_em_ordem_recursivo(no_atual.esquerda)
            elementos.append(no_atual.valor)
            elementos += self._percurso_em_ordem_recursivo(no_atual.direita)
        return elementos

    def percurso_em_pre_ordem(self):
        return self._percurso_em_pre_ordem_recursivo(self.raiz)

    def _percurso_em_pre_ordem_recursivo(self, no_atual):
        elementos = []
        if no_atual:
            elementos.append(no_atual.valor)
            elementos += self._percurso_em_pre_ordem_recursivo(no_atual.esquerda)
            elementos += self._percurso_em_pre_ordem_recursivo(no_atual.direita)
        return elementos

    def percurso_em_pos_ordem(self):
        return self._percurso_em_pos_ordem_recursivo(self.raiz)

    def _percurso_em_pos_ordem_recursivo(self, no_atual):
        elementos = []
        if no_atual:
            elementos += self._percurso_em_pos_ordem_recursivo(no_atual.esquerda)
            elementos += self._percurso_em_pos_ordem_recursivo(no_atual.direita)
            elementos.append(no_atual.valor)
        return elementos

