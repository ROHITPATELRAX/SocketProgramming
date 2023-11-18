import time
from socket import *
server_name = ''
server_port = 8080
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

# data="data de"
# details="details de"
#
# def decrypt(message):
#     print("Me time lunga")
#     time.sleep(2)
#
# i=0
cl=0
senderMsg='datade'
while True:
    try:
        client_socket.send(senderMsg)
        message = client_socket.recv(2048).decode()
        print(f">> {cl} {message}")
        # decrypt(message)
    except:
        break

client_socket.close()
print('Connection closed')

