from concurrent.futures import ThreadPoolExecutor
import socket
import time
def receiver(s):
    while True:
        data,addr=s.recvfrom(1024)
        print('Client says: '+data.decode())
        if data.decode().lower()=='quit':
            s.close()
            break

def send(s):
    while True:
        c, addr = s.accept()

        # display client address
        print("CONNECTION FROM:", str(addr))

        # dateTimeObj = str(datetime.now())
        # print(dateTimeObj)

        c.send(datapacket.encode())

        # disconnect the server
        c.close()

if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('',8000))

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(send,s)
        executor.submit(receiver,s)