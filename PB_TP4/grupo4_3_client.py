import socket

HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Digite a mensagem para o servidor: ")

client_socket.sendto(message.encode(), (HOST, PORT))

response, server_address = client_socket.recvfrom(1024)
print(f"Resposta do servidor: {response.decode()}")

client_socket.close()
