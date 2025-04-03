import ipaddress


class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.eh_prefixo = False
        self.prefixo = None


class TriePrefixo:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir_prefixo(self, prefixo_str):
        rede = ipaddress.ip_network(prefixo_str, strict=False)
        binario = self._obter_binario(rede.network_address, rede.prefixlen)

        no_atual = self.raiz
        for bit in binario:
            if bit not in no_atual.filhos:
                no_atual.filhos[bit] = NoTrie()
            no_atual = no_atual.filhos[bit]

        no_atual.eh_prefixo = True
        no_atual.prefixo = prefixo_str

    def buscar_prefixo_mais_especifico(self, ip_str):
        ip = ipaddress.ip_address(ip_str)
        binario = self._obter_binario(ip, 32)

        no_atual = self.raiz
        prefixo_encontrado = None

        for bit in binario:
            if bit in no_atual.filhos:
                no_atual = no_atual.filhos[bit]
                if no_atual.eh_prefixo:
                    prefixo_encontrado = no_atual.prefixo
            else:
                break

        return prefixo_encontrado

    def _obter_binario(self, endereco, tamanho):
        endereco_inteiro = int(endereco)
        endereco_binario = bin(endereco_inteiro)
        endereco_binario_sem_prefixo = endereco_binario[2:]
        endereco_binario_formatado = endereco_binario_sem_prefixo.zfill(tamanho)
        return endereco_binario_formatado


trie = TriePrefixo()
prefixos = ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"]
for p in prefixos:
    trie.inserir_prefixo(p)

ip_teste = "192.168.1.100"
resultado = trie.buscar_prefixo_mais_especifico(ip_teste)
print(f"O prefixo mais específico encontrado para {ip_teste} é: {resultado}")
