# SENDER
import socket
group = '239.255.255.250'
port = 1900
# 2-hop restriction in network
ttl = 2
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)
sock.sendto(b"HELLO DIGIVALET", (group, port))