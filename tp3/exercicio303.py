import concurrent.futures
import time


class ArvoreNo:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = ArvoreNo(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = ArvoreNo(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = ArvoreNo(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def buscar_dfs_paralelo(self, valor):
        if self.raiz is None:
            return None
        return self._buscar_dfs_paralelo(self.raiz, valor, [])

    def _buscar_dfs_paralelo(self, no_atual, valor, caminho):
        if no_atual is None:
            return None

        caminho.append(no_atual.valor)

        if no_atual.valor == valor:
            return caminho

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            futuro_esquerda = executor.submit(self._buscar_dfs_paralelo, no_atual.esquerda, valor, caminho[:])
            futuro_direita = executor.submit(self._buscar_dfs_paralelo, no_atual.direita, valor, caminho[:])

            resultado_esquerda = futuro_esquerda.result()
            resultado_direita = futuro_direita.result()

        return resultado_esquerda if resultado_esquerda else resultado_direita

    def encontrar_maximo_paralelo(self):
        if self.raiz is None:
            return None
        return self._encontrar_maximo_paralelo(self.raiz)

    def _encontrar_maximo_paralelo(self, no_atual):
        if no_atual is None:
            return float('-inf')

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            futuro_esquerda = executor.submit(self._encontrar_maximo_paralelo, no_atual.esquerda)
            futuro_direita = executor.submit(self._encontrar_maximo_paralelo, no_atual.direita)

            max_esquerda = futuro_esquerda.result()
            max_direita = futuro_direita.result()

        return max(no_atual.valor, max_esquerda, max_direita)


def contar_tempo(funcao, *args):
    inicio = time.time()
    resultado = funcao(*args)
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio} segundos")
    return resultado


if __name__ == "__main__":
    arvore = ArvoreBinaria()
    valores = [15, 10, 20, 8, 12, 17, 25]
    for v in valores:
        arvore.inserir(v)

    print("Buscando caminho até o valor 5:")
    caminho = contar_tempo(arvore.buscar_dfs_paralelo, 5)
    print("Caminho encontrado:", caminho)

    print("Encontrando o maior valor na árvore:")
    maximo = contar_tempo(arvore.encontrar_maximo_paralelo)
    print("Maior valor encontrado:", maximo)
