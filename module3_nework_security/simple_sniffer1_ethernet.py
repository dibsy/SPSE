import socket
import struct
import binascii

def print_mac_address(msg,mac):
	blocks = [mac[x:x+2] for x in xrange(0, len(mac), 2)]
	macFormatted = ':'.join(blocks)
	print msg,macFormatted

rawSocket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
pkt = rawSocket.recvfrom(2048)
ethernet_packet = pkt[0][0:14]
eth_hdr = struct.unpack("!6s6s2s",ethernet_packet)
src_mac = binascii.hexlify(eth_hdr[0])
dst_mac = binascii.hexlify(eth_hdr[1])
ethr_type = binascii.hexlify(eth_hdr[2])

print_mac_address("Source Mac:",src_mac)
print_mac_address("Destination Mac:",dst_mac)
print "Ether Type:",ethr_type
