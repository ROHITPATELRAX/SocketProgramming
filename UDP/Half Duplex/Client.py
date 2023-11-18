import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('Enter quit to lose connection')

packets="datade"

while True:
    s.sendto(bytes(str(packets),'utf-8'),('',8888))
    data,addr=s.recvfrom(1024)
    print('Server says: '+data.decode())

s.close()