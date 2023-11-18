# import sys
# from socket import *
# server_name = ''
# server_port = 8080
# client_socket = socket(AF_INET, SOCK_STREAM)
# client_socket.connect((server_name,server_port))
#
# # data="data de"
# # details="details de"
# #
# # def decrypt(message):
# #     print("Me time lunga")
# #     time.sleep(2)
#
# # i=0
#
# # while True:
# #     if i==0:
# #         sentence=details
# #     else:
# #         sentence=data
# client_socket.send(bytes(sys.argv[1],'utf-8'))
# #     if i == 0:
# #         i += 1
# message = client_socket.recv(2048).decode()
# # print(">>",message)
# # decrypt(message)
#
# client_socket.close()
# print('Connection closed')


# a=range(1,1317)
#
# for i in a:
#     if 30080%i==0:
#         print(i)

import sys

# iv="0x863cb0101b293854f14f76967692f91b"
# print(len(iv))


# import time
#
# # a module which has functions related to time.
# # It can be installed using cmd command:
# # pip install time, in the same way as pyautogui.
# import pyautogui
#
# time.sleep(10)
#
# # makes program execution pause for 10 sec
# pyautogui.moveTo(100, 100, duration=1)
#
# # moves mouse to 1000, 1000.
# pyautogui.dragRel(100, 0, duration=1)
#
# # drags mouse 100, 0 relative to its previous position,
# # thus dragging it to 1100, 1000
# pyautogui.dragRel(0, 100, duration=1)
# pyautogui.dragRel(-100, 0, duration=1)
# pyautogui.dragRel(0, -100, duration=1)

a=bytes()

print(len(a))

# a="str".encode()
b="wert".encode()
print((a+b))


def domain_name(url):
    pattern = re.compile(r'(https?://|www\.)?(www\.)?([a-z0-9-]+)(\..+)?')


    subbed_url = pattern.sub(r'\3', url)

    return subbed_url
sed="https://client-test-1.verimatrix.com/CAB/keyfile?r=content_a&t=VOD&p=0"

# from urllib.parse import urlparse
# domain = urlparse(sed).netloc
# print(domain)
import re
print(domain_name(sed))