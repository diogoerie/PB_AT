import socket
import ssl

HOST = '127.0.0.1'
PORT = 65432

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="chave.pem")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen(5)
    print("Servidor esperando conexões...")

    with context.wrap_socket(server_sock, server_side=True) as tls_server:
        conn, addr = tls_server.accept()
        print(f"Conexão estabelecida com {addr}")

        data = conn.recv(1024)
        if data:
            print("Recebido:", data.decode())
            conn.sendall(data)

