import socket

HOST = '127.0.0.1'
PORT = 5000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen()
print(f"Servidor iniciado e aguardando conexões em {HOST}:{PORT}...")

client_socket, client_address = server_socket.accept()
print(f"Conexão recebida de {client_address}")

welcome_message = f"Bem-vindo {client_address}"
client_socket.sendall(welcome_message.encode())

while True:
    data = client_socket.recv(1024)
    if not data:
        break

    print(f"Mensagem recebida do cliente: {data.decode()}")
    response = "Mensagem recebida com sucesso!"
    client_socket.sendall(response.encode())

client_socket.close()
server_socket.close()
