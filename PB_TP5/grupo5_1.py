import dns.resolver

domain = "google.com"


def collect_dns_records(domain):
    try:
        print(f"Registros A para {domain}:")
        a_records = dns.resolver.resolve(domain, 'A')
        for ip in a_records:
            print(ip.to_text())

        print(f"\nRegistros MX para {domain}:")
        mx_records = dns.resolver.resolve(domain, 'MX')
        for mx in mx_records:
            print(f"{mx.preference} {mx.exchange.to_text()}")

        print(f"\nRegistros NS para {domain}:")
        ns_records = dns.resolver.resolve(domain, 'NS')
        for ns in ns_records:
            print(ns.to_text())

    except(dns.resolver.NoAnswer, dns.resolver.NSDOMAIN):
        print(f"Erro ao consultar registros DNS para {domain}.")


collect_dns_records(domain)
