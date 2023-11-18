import concurrent.futures
import socket
import time


def a(message):
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(('localhost',9696))
    client_socket.send(message.encode())
    return client_socket.recv(2048).decode()

with concurrent.futures.ThreadPoolExecutor() as executeIt:
    aa=time.time()
    future=[]
    for i in range(65,91):
        future.append(executeIt.submit(a,chr(i)))
    for f in concurrent.futures.as_completed(future):
        print(str(f.result()))

    bb=time.time()
    print(bb-aa)

aa=time.time()
for i in range(65,91):
    a(chr(i))
bb=time.time()
print(bb-aa)
# for f in concurreesult()))
