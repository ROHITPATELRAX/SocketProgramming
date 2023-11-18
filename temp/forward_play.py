import sys
from socket import *
server_name = ''
server_port = 8888
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

client_socket.send(bytes(sys.argv[1],'utf-8'))
message = client_socket.recv(2048).decode()
print(message)
client_socket.close()
print('Connection closed')
#
# import sys
# import json
# import requests
# import m3u8
# import shutil
# import os
#
#
# m3u8_url =str(sys.argv[1])
# #str("http://192.168.0.51/content/verimatrix-hls/DRM_Client_Integration_Test_HLS/hls_content_ah_clear_rev1/list_1280x720_5000.m3u8")
# r = requests.get(m3u8_url)
# m3u8_master = m3u8.loads(r.text)
# print(m3u8_master.data)

# m3u8_file = m3u8_url.split('/')[-1]
# url = strip_end(m3u8_url, m3u8_file)
# url_copy = url
#
# tsFileUrl=list()
#
# print(m3u8_master.simple_attributes)
# for seg in m3u8_master.data['segments']:
#     url += seg['uri']
#     print(url)
#     url = url_copy