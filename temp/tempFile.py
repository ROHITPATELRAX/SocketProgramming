# import json
# import sys
# import m3u8
# import time
# import socket
# import requests
# from threading import Thread
#
# noOfPacketAfter1316Chunk=0
# filePointer=0
# counter=0
# dataStore=list()
# lastfileindex=False
# class DataProcessing():
#     def __init__(self, m3u8Link) -> None:
#         self.link = m3u8Link
#
#     def getData(self, url, singleTSINFO):
#         global filePointer
#         global noOfPacketAfter1316Chunk
#         chunkedData = list()
#
#         r = requests.get(url, stream=True)
#
#         for chunk in r.iter_content(chunk_size=1316):
#             if chunk:
#                 chunkedData.append(chunk)
#                 noOfPacketAfter1316Chunk += 1
#
#         singleTSINFO['filePointer'] = filePointer
#         singleTSINFO['data'] = chunkedData
#         filePointer += 1
#         print(filePointer)
#
#     def strip_end(self, text, suffix):
#         if not text.endswith(suffix):
#             return text
#         return text[:len(text) - len(suffix)]
#
#     def dataPicker(self):
#         global dataStore
#
#         m3u8_url = self.link  # m3u8 link
#         r = requests.get(m3u8_url)
#         m3u8_master = m3u8.loads(r.text)
#         m3u8_file = m3u8_url.split('/')[-1]
#         url = self.strip_end(m3u8_url, m3u8_file)
#         url_copy = url
#
#         for seg in m3u8_master.data['segments']:
#             singleTSINFO = dict()
#             singleTSINFO['uri'] = seg['uri']
#             singleTSINFO['duration'] = int(seg['duration'])
#             url += seg['uri']
#             self.getData(url, singleTSINFO)
#             url = url_copy
#             dataStore.append(singleTSINFO)
#         return "Processing is done!!!"
#
#
# def main():
#     global lastfileindex
#     m3u8Link = str(sys.argv[1])
#     dataProcessObj = DataProcessing(m3u8Link)
#     responsefromprocessing = dataProcessObj.dataPicker()
#     # if responsefromprocessing == "Processing is done!!!":
#     #     lastfileindex = True
#
#     json.dumps(dataStore)
#
#     # time.sleep(0.083333333)
#     # socketObj = TCPConnection(m3u8Link, "vcasServer", 8080, 8888)
#     # socketObj.start()
#     # socketObj.join()
#
#
# if __name__ == "__main__":
#     main()


import sys
import json
import requests
import m3u8
import shutil
import os


m3u8_url =str(sys.argv[1])
#str("http://192.168.0.51/content/verimatrix-hls/DRM_Client_Integration_Test_HLS/hls_content_ah_clear_rev1/list_1280x720_5000.m3u8")
r = requests.get(m3u8_url)
# print(r.content.decode())
IV=str()

for line in r.content.decode().splitlines():
    if "IV" in line and "URI" in line and "METHOD" in line:
        for i in str(line).split(","):
            # print(i)
            if "METHOD" in i:
                METHOD=i.split("METHOD=")[-1]
            if "URI" in i:
                URI=i.replace("URI=",'').replace('"','')
            if "IV" in i:
                IV=i.replace("IV=","")
    # lineResult = libLAPFF.parseLine(line)
print(IV)
print(URI)
print(METHOD)
# print(r.iter_lines)
m3u8_master = m3u8.loads(r.text)

# print(m3u8_master.server_control)

# print(m3u8_master.data)

# m3u8_file = m3u8_url.split('/')[-1]
# url = strip_end(m3u8_url, m3u8_file)
# url_copy = url