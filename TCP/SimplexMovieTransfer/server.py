import socket
import time

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',9696))
server_socket.listen(100)
while True:
    connection_socket, address = server_socket.accept()
    while True:
        sentence = connection_socket.recv(2048).decode().strip()
        print(sentence)

    # if "A" in sentence:
    #     connection_socket.send("A".encode())
    #
    # elif "B" in sentence:
    #     connection_socket.send("B".encode())
    #
    # elif "C" in sentence:
    #     connection_socket.send("C".encode())
    #
    # elif "D" in sentence:
    #     connection_socket.send("D".encode())
    #
    # elif "E" in sentence:
    #     connection_socket.send("E".encode())
    #
    # elif "F" in sentence:
    #     connection_socket.send("F".encode())
    #
    # elif "G" in sentence:
    #     connection_socket.send("G".encode())
    #
    # elif "H" in sentence:
    #     connection_socket.send("H".encode())
    #
    # elif "I" in sentence:
    #     connection_socket.send("I".encode())
    #
    # elif "J" in sentence:
    #     connection_socket.send("J".encode())
    #
    # elif "K" in sentence:
    #     connection_socket.send("K".encode())
    #
    # elif "L" in sentence:
    #     connection_socket.send("L".encode())
    #
    # elif "M" in sentence:
    #     connection_socket.send("M".encode())
    #
    # elif "N" in sentence:
    #     connection_socket.send("N".encode())
    #
    # elif "O" in sentence:
    #     connection_socket.send("O".encode())
    #
    # elif "P" in sentence:
    #     connection_socket.send("P".encode())
    #
    # elif "Q" in sentence:
    #     connection_socket.send("Q".encode())
    #
    # elif "R" in sentence:
    #     connection_socket.send("R".encode())
    #
    # elif "S" in sentence:
    #     connection_socket.send("S".encode())
    #
    # elif "T" in sentence:
    #     connection_socket.send("T".encode())
    #
    # elif "U" in sentence:
    #     connection_socket.send("U".encode())
    #
    # elif "V" in sentence:
    #     connection_socket.send("V".encode())
    #
    # elif "W" in sentence:
    #     connection_socket.send("W".encode())
    #
    # elif "X" in sentence:
    #     connection_socket.send("X".encode())
    #
    # elif "Y" in sentence:
    #     connection_socket.send("Y".encode())
    #
    # elif "Z" in sentence:
    #     connection_socket.send("Z".encode())

    # else:
    #     pass
    # time.sleep(0.1)
#
# for i in range(65,91):
#     if i==65:
#         print(f"""    if "{chr(i)}" in sentence:
#         connection_socket.send("{chr(i)}")
#         """)
#     else:
#         print(f"""    elif "{chr(i)}" in sentence:
#         connection_socket.send("{chr(i)}")
#                 """)