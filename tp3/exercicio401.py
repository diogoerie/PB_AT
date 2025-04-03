import ipaddress


def verificar_prefixo(ip_str, prefixo_str):
    ip = ipaddress.ip_address(ip_str)
    prefixo = ipaddress.ip_network(prefixo_str, strict=False)

    if ip in prefixo:
        mensagem = f"O IP {ip} está dentro do prefixo {prefixo}."
    else:
        mensagem = f"O IP {ip} NÃO está dentro do prefixo {prefixo}."

    return mensagem

resultado = verificar_prefixo("192.168.1.5", "192.168.1.0/24")
print(resultado)
