import socket

client_socket=socket.socket()

client_socket.connect(('localhost',9098))
print(client_socket.recv(2054).decode())

client_socket.send("I am not interested yaar".encode())
client_socket.close()