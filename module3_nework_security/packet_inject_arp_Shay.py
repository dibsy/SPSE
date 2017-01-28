#!/usr/bin/env python2.7

from itertools import chain
import socket
import struct

sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
sock.bind(("eth0", 8))

ip_src_mac = "00:0c:29:c1:e4:50"
ip_dst_mac = "FF:FF:FF:FF:FF:FF"
ether_type = 0x0806
arp_htype = 0x0001
arp_ptype = 0x0800
arp_hlen = 0x06
arp_plen = 0x04
arp_op = 0x0001
arp_src_ip = "0.0.0.0"
arp_dst_mac = "00:00:00:00:00:00"
arp_dst_ip = "192.168.160.2"

## Accepts MAC in format XX:XX:XX:XX:XX:XX and returns a tuple of ints
def format_mac(mac):
	mac = mac.split(":")
	return tuple([int(mac[i], 16) for i in range(0, len(mac))])

## Accepts a dotted quad IP and returns a long
def format_ip(ip):
	return long("".join(["{:02X}".format(long(i)) for i in ip.split('.')]), 16)

ip_s_mac = format_mac(ip_src_mac)
ip_d_mac = format_mac(ip_dst_mac)
s_ip = format_ip(arp_src_ip)
arp_d_mac = format_mac(arp_dst_mac)
d_ip = format_ip(arp_dst_ip)

ether_header = struct.pack("!6B6BH", *tuple(chain(ip_d_mac, ip_s_mac, [ether_type])))
arp_data = struct.pack("!HHBBH6BI6BI",
	*tuple(chain(
		[arp_htype, arp_ptype, arp_hlen, arp_plen, arp_op], ip_s_mac,
		[s_ip], arp_d_mac, [d_ip]
	))
)

## Min length for ethernet frame sans 802.1Q tag is 46 bytes
while len(arp_data) < 46:
	arp_data += struct.pack("B", 0x00)

packet = ether_header + arp_data
sock.send(packet)
sock.close()

