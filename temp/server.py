import socket
from socket import *
import time
from threading import Thread

counter=0
killAllThreads=False
range_1 = range(1,100)

list_1 = list()
for x in range_1:
    list_1.append(x)


def incrementor(value):
    print("Me increment kiya: ")
    global counter
    if not ((counter+value)>=len(list_1)):
        counter+=value

def decrementor(value):
    global counter
    if (counter-value)>0:
        print("Me decrement kiya")
        counter-=value


def connectionMaker(dataPackets):
    server_name = '127.0.0.1'
    server_port = 9002
    server_socket = socket(AF_INET,SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((server_name,server_port))
    server_socket.listen(3)
    print("starting to listen")
    connection_socket, address = server_socket.accept()
    details=dict()
    details['url']="https://url.m3u8"
    details['vcasServer']="client.vas"

    global counter
    global killAllThreads

    while True and not killAllThreads:
        try:
            sentence = connection_socket.recv(2048).decode().strip()
            print(sentence,type(sentence),len(sentence))
            if sentence=="details de":
                connection_socket.send(str(details).encode())
            if "datade" in sentence:
                print("Me data diya")
                connection_socket.send(str(counter))
                    # while len(dataPackets)<=counter:
                    #     if killAllThreads:
                    #         connection_socket.close()
                    #         break
                    #     time.sleep(1)
                    # connection_socket.send(str(dataPackets[counter]).encode())
                counter+=1
        except:
            break
    server_socket.close()
    print('Connection closed')

def connectionForForwardAndBackward():
    server_name = '127.0.0.1'
    server_port = 8888
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    server_socket.bind((server_name, server_port))
    server_socket.listen(1)
    print("Starting to listen for forward and backward ")
    # connection_socket, address = server_socket.accept()
    # details = dict()
    # details['url'] = "https://url.m3u8"
    # details['vcasServer'] = "client.vas"
    global counter
    global killAllThreads

    while not killAllThreads:
        connection_socket, address = server_socket.accept()
        sentence = connection_socket.recv(2048).decode()
        print(sentence)
        if "FORWARD" in sentence:
            incrementor(int(sentence.split("*")[0]))
        elif "BACKWARD" in sentence:
            decrementor(int(sentence.split("*")[0]))
        elif "CLOSE" in sentence:
            killAllThreads=True

        connection_socket.close()
    server_socket.close()
    print('Connection closed')

a=Thread(target=connectionMaker,args=(list_1,))
# b=Thread(target=connectionForForwardAndBackward)

a.start()
# b.start()
