import socket
import struct
import binascii

def print_mac_address(msg,mac):
	blocks = [mac[x:x+2] for x in xrange(0, len(mac), 2)]
	macFormatted = ':'.join(blocks)
	print msg,macFormatted

rawSocket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
pkt = rawSocket.recvfrom(2048)
ip_frame = pkt[0][14:34]
ip_hdr = struct.unpack("!12s4s4s",ip_frame)
#src_ip = binascii.hexlify(ip_hdr[0])
#dst_ip = binascii.hexlify(ip_hdr[1])

print "Source IP:",socket.inet_ntoa(ip_hdr[1])
print "Destination IP:",socket.inet_ntoa(ip_hdr[2])

tcp_frame = pkt[0][34:54]
tcp_hdr = struct.unpack("!HH16s",tcp_frame)
print tcp_hdr
