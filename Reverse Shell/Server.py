import socket
import sys
def create_connection():
    try:
        global host
        global port
        global s
        host=''
        port=9999
        s=socket.socket()
    except Exception as e:
        print("Error occured while creating connection: ",e)

def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host,port))
        s.listen(5)
    except Exception as e:
        print("Error occured while binding connection: "+e+"\nRetrying.....")
        bind_socket()

def accept_connection():
    try:
        global s
        global c
        c,addr=s.accept()
        print('Connected with ',addr)
        send_message()
        c.close()
    except Exception as e:
        print('Error occured while listening connection: ',e)

def send_message():
    while True:
        cmd=input('Enter cmd:-')
        if cmd=='quit':
            s.close()
            sys.exit()
        if len(str.encode(cmd)) >0:
            c.send(str.encode(cmd))
            response=c.recv(1024).decode('utf-8')
            print(response,end="\n")

def main():
    create_connection()
    bind_socket()
    accept_connection()


if __name__=='__main__':
    main()
