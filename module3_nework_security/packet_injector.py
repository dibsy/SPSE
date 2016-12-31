import socket
import struct

rawsocket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
rawsocket.bind(("ens33",socket.htons(0x0800)))
packet = struct.pack('!6s6s2s','\xaa\xaa\xaa\xaa\xaa\xaa','\xbb\xbb\xbb\xbb\xbb\xbb','\x08\x00')
rawsocket.send(packet+"This is an injected packet")

