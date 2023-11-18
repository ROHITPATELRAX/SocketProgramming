import socket

socket_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_client.sendto('HELLO'.encode(),('192.168.3.209',8888))