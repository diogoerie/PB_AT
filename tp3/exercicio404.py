import time
import ipaddress

class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.prefixo = None

class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, prefixo):
        no_atual = self.raiz
        rede = ipaddress.IPv4Network(prefixo, strict=False)
        binario_prefixo = ''.join([bin(int(octeto))[2:].zfill(8) for octeto in str(rede.network_address).split('.')])
        for bit in binario_prefixo:
            if bit not in no_atual.filhos:
                no_atual.filhos[bit] = NoTrie()
            no_atual = no_atual.filhos[bit]
        no_atual.prefixo = prefixo

    def buscar(self, ip):
        no_atual = self.raiz
        binario_ip = ''.join([bin(int(octeto))[2:].zfill(8) for octeto in ip.split('.')])
        prefixo_correspondente = None
        for bit in binario_ip:
            if bit in no_atual.filhos:
                no_atual = no_atual.filhos[bit]
                if no_atual.prefixo:
                    prefixo_correspondente = no_atual.prefixo
            else:
                break
        return prefixo_correspondente

def busca_linear(ip, lista_prefixos):
    prefixo_correspondente = None
    for prefixo in lista_prefixos:
        if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(prefixo, strict=False):
            prefixo_correspondente = prefixo
    return prefixo_correspondente

prefixos = ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8", "172.16.0.0/12"]
ips_para_busca = ["192.168.1.55", "10.0.5.10", "172.16.15.5"]

for ip in ips_para_busca:
    inicio = time.time()
    resultado_linear = busca_linear(ip, prefixos)
    fim = time.time()
    tempo_busca_linear = fim - inicio
    print(f"Resultado da busca linear para {ip}: {resultado_linear}")
    print(f"Tempo da busca linear para {ip}: {tempo_busca_linear}")

trie = Trie()
for prefixo in prefixos:
    trie.inserir(prefixo)

for ip in ips_para_busca:
    inicio = time.time()
    resultado_trie = trie.buscar(ip)
    fim = time.time()
    tempo_trie = fim - inicio
    print(f"Resultado da busca na Trie para {ip}: {resultado_trie}")
    print(f"Tempo da busca na Trie para {ip}: {tempo_trie}")
