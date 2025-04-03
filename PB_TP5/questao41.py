from scapy.all import ARP, Ether, srp

def varredura_arp(ip_range):
    arp_request = ARP(pdst=ip_range)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = ether_frame/arp_request

    resposta, _ = srp(pacote, timeout=3, verbose=False)

    for _, res in resposta:
        print(f"IP: {res.psrc}, MAC: {res.hwsrc}")

if __name__ == "__main__":
    ip_range = "192.168.1.0/24"
    varredura_arp(ip_range)
