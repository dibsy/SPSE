import socket
import struct
import binascii

def print_mac_address(msg,mac):
	blocks = [mac[x:x+2] for x in xrange(0, len(mac), 2)]
	macFormatted = ':'.join(blocks)
	print msg,macFormatted

def print_ip_address(msg,ip):
	octets = [ip[i:i+2] for i in range(0, len(ip), 2)]
	ip = [int(i, 16) for i in reversed(octets)]
	ip_formatted = '.'.join(str(i) for i in ip)
	print msg,ip_formatted

rawSocket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0806))
pkt = rawSocket.recvfrom(2048)
arp_frame = pkt[0][14:42]
arp_hdr =  struct.unpack("!2s2s1s1s2s6s4s6s4s",arp_frame)
src_mac = binascii.hexlify(arp_hdr[5])
src_ip = binascii.hexlify(arp_hdr[6])
dst_mac = binascii.hexlify(arp_hdr[7])
dst_ip = binascii.hexlify(arp_hdr[8])


#print src_mac
#print src_ip
#print dst_mac
#print dst_ip
print_mac_address("Source Mac:",src_mac)
print "Source IP:",socket.inet_ntoa(arp_hdr[6])
print_mac_address("Destination Mac:",dst_mac)
print "Destination IP:",socket.inet_ntoa(arp_hdr[8])
