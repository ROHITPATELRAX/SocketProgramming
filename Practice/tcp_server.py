import socket

server_socket=socket.socket()
# server_socket.setsockopt()
server_socket.bind(('localhost',9098))
server_socket.listen(5)

fd,addr=server_socket.accept()
fd.send("Hello There!\n".encode())
print(server_socket.recv(2054).decode())
fd.close()
server_socket.close()