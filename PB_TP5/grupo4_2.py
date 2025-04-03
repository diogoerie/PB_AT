from scapy.all import sniff, ARP

def monitorar_arp():
    arp_cache = {}

    def detectarSpoofing(pkt):
        if pkt.haslayer(ARP):
            ip_origem = pkt[ARP].psrc
            mac_origem = pkt[ARP].hwsrc

            if ip_origem in arp_cache:
                if arp_cache[ip_origem] != mac_origem:
                    print(f"Possível tentativa de ARP Spoofing no IP {ip_origem}")
                    print(f"MAC anterior: {arp_cache[ip_origem]}, MAC atual: {mac_origem}")

            arp_cache[ip_origem] = mac_origem

    print("Monitorando... Porém, nenhum spoofing foi detectado até o momento.")
    sniff(prn=detectarSpoofing, filter="arp", store=0)

if __name__ == "__main__":
    monitorar_arp()