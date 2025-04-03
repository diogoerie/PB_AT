import subprocess
import sys

def scan_host(target):
    result = subprocess.run(['nmap', '--top-ports', '1000', target], capture_output=True, text=True)

    if result.returncode == 0:
        print("Resultado da varredura Nmap:")
        print(result.stdout)
    else:
        print("Erro ao executar o Nmap.")
        print(f"Código de retorno: {result.returncode}")
        print(result.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python group5_exercicio2.py <IP-alvo>")
    else:
        target_ip = sys.argv[1]
        scan_host(target_ip)
