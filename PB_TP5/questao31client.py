import socket
import ssl

HOST = '127.0.0.1'
PORT = 65432

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("cert.pem")

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as tls_client:
        print("Cliente: conexão estabelecida")

        mensagem = "Olá, servidor TLS!"
        tls_client.sendall(mensagem.encode())

        data = tls_client.recv(1024)
        print("Cliente: recebido:", data.decode())
