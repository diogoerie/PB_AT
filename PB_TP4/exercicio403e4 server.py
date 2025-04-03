import socket

HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((HOST, PORT))

print(f"Servidor iniciado em {HOST}:{PORT}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Mensagem recebida de {client_address}: {data.decode()}")

    response = "ack"
    server_socket.sendto(response.encode(), client_address)
