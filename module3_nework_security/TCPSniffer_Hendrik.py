#!/usr/bin/env python

import socket, struct, binascii
global IP, TCP, UDP, HTTP 

IP, TCP, UDP, HTTP = False, False, False, False

def parseETH(header):
	global IP
	eth_hdr = struct.unpack("!6s6s2s", header)
	source = binascii.hexlify(eth_hdr[0])
	dest = binascii.hexlify(eth_hdr[1])
	print "\nEthernet"
	print "-Source:\t ", source
	print "-Dest:\t\t ", dest

	if binascii.hexlify(eth_hdr[2]) == '0800':
		IP = True

def parseIP(header):
	global TCP, UDP
	ip_hdr = struct.unpack("!9s1s2s4s4s", header)
	source = socket.inet_ntoa(ip_hdr[3])
	dest = socket.inet_ntoa(ip_hdr[4])

	print "\nIP"
	print "-Source:\t ", source
	print "-Dest:\t\t ", dest

	if binascii.hexlify(ip_hdr[1]) == '06':
		TCP = True

	elif binascii.hexlify(ip_hdr[1]) == '11':
		UDP = True

def parseTCP(header):
	global HTTP
	tcp_hdr = struct.unpack("!2s2s16s", header)
	src_port = binascii.hexlify(tcp_hdr[0])
	dst_port = binascii.hexlify(tcp_hdr[1])

	#converted ports in hex to decimal value
	print "\nTCP"
	print "-Source port:\t\t", int(src_port, 16)
	print "-Destination port:\t", int(dst_port, 16)

	if (int(src_port, 16) == 80 ) or (int(dst_port, 16) == 80):
		HTTP = True

def parseUDP(header):
	udp_hdr = struct.unpack("!2s2s16s", header)
	src_port = binascii.hexlify(udp_hdr[0])
	dst_port = binascii.hexlify(udp_hdr[1])


	#converted ports in hex to decimal value
	print "\nUDP"
	print "-Source port:\t\t", int(src_port, 16)
	print "-Destination port:\t", int(dst_port, 16)


def parseHTTP(data):
	print data


rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
while True:
	pkt = rawSocket.recvfrom(2048)
	print "Received packet:"

	parseETH(pkt[0][0:14])

	if IP:
		parseIP(pkt[0][14:34])

	if TCP:
		parseTCP(pkt[0][34:54])

	elif UDP:
		parseUDP(pkt[0][34:54])

	if HTTP:
		parseHTTP(pkt[0][54:])

	print "\nDone\n\n"


