from socket import *
server_name = ''
server_port = 8080
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

while True:
  sentence = input(">> ")
  client_socket.send(bytes(sentence,'utf-8'))
  if(sentence == 'q'):
    break
  message = client_socket.recv(2048).decode()
  if(message == 'q'):
      break
  print (">> ", message)

client_socket.close()
print('Connection closed')
