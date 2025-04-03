import threading
import time


class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoArvore(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvore(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = NoArvore(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def busca_paralela(self, valor):
        if self.raiz is None:
            return False

        encontrado = threading.Event()

        def buscar_subarvore(no_atual):
            if no_atual is None or encontrado.is_set():
                return
            if no_atual.valor == valor:
                encontrado.set()
                return

            esquerda_thread = threading.Thread(target=buscar_subarvore, args=(no_atual.esquerda,))
            direita_thread = threading.Thread(target=buscar_subarvore, args=(no_atual.direita,))

            esquerda_thread.start()
            direita_thread.start()

            esquerda_thread.join()
            direita_thread.join()

        buscar_subarvore(self.raiz)
        return encontrado.is_set()


def contar_tempo(funcao, *args):
    inicio = time.time()
    resultado = funcao(*args)
    fim = time.time()
    tempo_gasto = fim - inicio
    return resultado, tempo_gasto


arvore = ArvoreBinaria()
numeros = [50, 30, 70, 20, 40, 60, 80]
for num in numeros:
    arvore.inserir(num)

valor_procurado = 60
resultado, tempo_execucao = contar_tempo(arvore.busca_paralela, valor_procurado)
print(f"Valor {valor_procurado} encontrado: {resultado}")
print(f"Tempo de execução: {tempo_execucao} segundos")
