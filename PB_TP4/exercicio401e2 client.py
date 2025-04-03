import socket


HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

welcome_message = client_socket.recv(1024).decode()
print(f"Mensagem do servidor: {welcome_message}")

message = input("Digite a mensagem para o servidor: ")
client_socket.sendall(message.encode())

response = client_socket.recv(1024).decode()
print(f"Resposta do servidor: {response}")

client_socket.close()
