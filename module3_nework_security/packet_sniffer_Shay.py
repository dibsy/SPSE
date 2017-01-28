#!/usr/bin/env python2.7

## IP reference: http://www.networksorcery.com/enp/protocol/ip.htm
## TCP reference: http://www.networksorcery.com/enp/protocol/tcp.htm

import binascii
import ctypes
import fcntl
import math
import socket
import struct
import sys

## Interface from which to capture data
IF_NAME = "eth0"

## Format options structure; filled in when program options are parsed
formatter = {}

## Model the C interface request structure since Python doesn't expose it to us
## Found in /usr/include/net/if.h
class ifreq(ctypes.Structure):
	_fields_ = [
		## Interface name (i.e. eth0)
		("ifr_ifrn", ctypes.c_char * 16),
		## Flags to apply
		("ifr_flags", ctypes.c_short)
	]

## Model the C ethernet frame header
## Found in /usr/include/net/ethernet.h
class ether_header(ctypes.Structure):
	## How many headers have been created
	num = 0

	_fields_ = [
		## Destination eth addr
		("eth_dhost", ctypes.c_ubyte * 6),
		## Source eth addr
		("eth_shost", ctypes.c_ubyte * 6),
		## Packet type ID
		("eth_type", ctypes.c_ushort)
	]

	## Define some common ethertypes
	types = {
		2048: "IPv4",
		2054: "ARP",
		32821: "RARP",
		33100: "SNMP",
		34525: "IPv6",
	}

	def __init__(self, *args):
		self.eth_dhost = args[0:6]
		self.eth_shost = args[6:12]
		self.eth_type = args[12]
		ether_header.num += 1


	def dump(self):
		print_section_header('ETHERNET HEADER #{}'.format(self.num))

		print_output("Source MAC", "{}", (format_mac(self.eth_shost),))
		print_output("Destination MAC", "{}", (format_mac(self.eth_dhost),))
		print_output("Ether Type", "0x{:04x} ({})",
			(self.eth_type, self.types.get(self.eth_type, "Unknown"))
		)

		print_section_footer()


## IP header constants for bit masking
IP_OFFMASK = 0x1fff
IP_IHLMASK = 0x0f

## IP header bitmasking functions
IP_VER = lambda b: (b & ~IP_IHLMASK)>>4
IP_IHL = lambda b: b & IP_IHLMASK
IP_FLAGS = lambda b: (b & ~IP_OFFMASK)>>13
IP_OFF = lambda b: b & IP_OFFMASK
IP_DF = lambda b: (b & 0x2)>>1
IP_MF = lambda b: b & 0x1

## Model the C internet header
## Found in /usr/include/netinet/ip.h
class ip_header(ctypes.Structure):
	## How many headers have been created
	num = 0

	_fields_ = [
		## Version
		("_ip_ver", ctypes.c_ubyte, 4),
		## Internet header length
		("ip_ihl", ctypes.c_ubyte, 4),
		## Differentiated services (used to be TOS)
		("ip_ds", ctypes.c_ushort),
		## Total length
		("ip_tlen", ctypes.c_ushort),
		## Identification
		("ip_id", ctypes.c_ushort),
		## Flags
		("_ip_flags", ctypes.c_ushort, 3),
		## Fragment offset
		("ip_off", ctypes.c_ushort, 13),
		## TTL
		("ip_ttl", ctypes.c_ubyte),
		## Protocol
		("ip_proto", ctypes.c_ubyte),
		## Header checksum
		("ip_sum", ctypes.c_ushort),
		## Source IP
		("ip_src", ctypes.c_uint),
		## Destination IP
		("ip_dst", ctypes.c_uint),
	]

	## Define some IP versions
	versions = {
		4: "IPv4",
		6: "IPv6"
	}

	## Define some protocols
	protos = {
		1: "ICMP",
		6: "TCP",
		17: "UDP"
	}

	def __init__(self, *args):
		self.ip_ver = args[0]
		self.ip_ds = args[1]
		self.ip_tlen = args[2]
		self.ip_id = args[3]
		self.ip_flags = args[4]
		self.ip_ttl = args[5]
		self.ip_proto = args[6]
		self.ip_sum = args[7]
		self.ip_src = args[8]
		self.ip_dst = args[9]
		ip_header.num += 1

	@property
	def ip_ver(self): return self._ip_ver

	@ip_ver.setter
	def ip_ver(self, v):
		self._ip_ver = IP_VER(v)
		self.ip_ihl = IP_IHL(v)

	@property
	def ip_flags(self): return self._ip_flags

	@ip_flags.setter
	def ip_flags(self, v):
		self._ip_flags = IP_FLAGS(v)
		self.ip_off = IP_OFF(v)

	## Get the dotted quad format for the src IP
	def ip_src_dotted(self):
		return socket.inet_ntoa(struct.pack(">I", packet.ip_header.ip_src))

	## Get the dotted quad format for the dst IP
	def ip_dst_dotted(self):
		return socket.inet_ntoa(struct.pack(">I", packet.ip_header.ip_dst))

	def dump(self):
		print_section_header('IP HEADER #{}'.format(self.num))

		## Basic Differentiated Services field processing
		if not self.ip_ds & 0x1f:
			ds = "CS{0}".format((self.ip_ds & 0xe0)>>5)
		else:
			## Just display the raw value if we go past the CS codepoints
			ds = hex(self.ip_ds)

		print_output("Version", "{} ({})", (self.ip_ver, self.versions.get(self.ip_ver, "Unknown")))
		print_output("Inet Header Len", "{} bytes", (self.ip_ihl*4,))
		print_output("Diff Services", "{}", (ds,))
		print_output("Total Length", "{}", (self.ip_tlen,))
		print_output("Identification", "0x{:04x}", (self.ip_id,))
		print_output("Flags", "DF ({}), MF ({})", (IP_DF(self.ip_flags), IP_MF(self.ip_flags)))
		print_output("Fragment Offset", "{}", (self.ip_off,))
		print_output("TTL", "{}", (self.ip_ttl,))
		print_output("Protocol", "{}", (self.protos.get(self.ip_proto, "Unknown"),))
		print_output("Checksum", "0x{:04x}", (self.ip_sum,))
		print_output("Source IP", "{}", (self.ip_src_dotted(),))
		print_output("Destination IP", "{}", (self.ip_dst_dotted(),))

		print_section_footer()


## TCP constants for bitmasking
TCP_OFFMASK = 0xf000
TCP_ECNMASK = 0x01c0
TCP_FLAGSMASK = 0x003f

## TCP header bitmasking functions
TCP_OFF = lambda b: (b & TCP_OFFMASK)>>12
TCP_ECN = lambda b: (b & TCP_ECNMASK)>>6
TCP_FLAGS = lambda b: b & TCP_FLAGSMASK

## Model the C TCP header
## Found in /usr/include/netinet/tcp.h
class tcp_header(ctypes.Structure):
	## How many headers have been created
	num = 0

	_fields_ = [
		## Source port
		("tcp_sport", ctypes.c_ushort),
		## Destination port
		("tcp_dport", ctypes.c_ushort),
		## Sequence number
		("tcp_seq", ctypes.c_uint),
		## ACK number
		("tcp_ack", ctypes.c_uint),
		## Data offset
		("_tcp_off", ctypes.c_ushort, 4),
		## 3 bits are reserved here that we ignore
		## ECN
		("tcp_ecn", ctypes.c_ushort, 3),
		## Control bits
		("tcp_flags", ctypes.c_ushort, 6),
		## Window
		("tcp_win", ctypes.c_ushort),
		## Checksum
		("tcp_sum", ctypes.c_ushort),
		## URG pointer
		("tcp_urgp", ctypes.c_ushort),
		## TCP options
		("tcp_opts", ctypes.c_ubyte * 40)
	]

	## Flag constants
	FIN = 0x01
	SYN = 0x02
	RST = 0x04
	PSH = 0x08
	ACK = 0x10
	URG = 0x20

	## ECN constants
	ECN_E = 0x01
	ECN_C = 0x02
	ECN_N = 0x04

	def __init__(self, *args):
		self.tcp_sport = args[0]
		self.tcp_dport = args[1]
		self.tcp_seq = args[2]
		self.tcp_ack = args[3]
		self.tcp_off = args[4]
		self.tcp_win = args[5]
		self.tcp_sum = args[6]
		self.tcp_urgp = args[7]
		tcp_header.num += 1


	@property
	def tcp_off(self): return self._tcp_off

	@tcp_off.setter
	def tcp_off(self, v):
		self._tcp_off = TCP_OFF(v)
		self.tcp_ecn = TCP_ECN(v)
		self.tcp_flags = TCP_FLAGS(v)

	## Format TCP options and print it
	def print_option(self, k, v):
		s = self.options.get(k, "Unknown")

		if v is not None:
			if k == 3:
				mul = int(math.pow(2, int(v)))
				print_output(s, "({{}} - multiply by {})".format(mul), (int(v, 16),))

			elif k == 8:
				print_output(s, "(TSval {}, TSecr {})", (int(v[0:8], 16), int(v[8:], 16)))
			else:
				print_output(s, "({})", (int(v, 16),))
		else:
			print_output(s, "({})", ("Set",))

	## Define some TCP options
	options = {
		0: "END",
		1: "NOP",
		2: "MSS",
		3: "WSOPT",
		4: "SACK",
		8: "TSOPT"
	}

	def dump(self):
		print_section_header("TCP HEADER #{}".format(self.num))

		## Format ECN
		ecn = self.tcp_ecn
		ecn_str = ''
		if ecn == 0: ecn_str += '0'
		if ecn & self.ECN_E: ecn_str += 'E'
		if ecn & self.ECN_C: ecn_str += ', C'
		if ecn & self.ECN_N: ecn_str += ', N'

		## Format flags
		ctrl = self.tcp_flags
		ctrl_str = ''
		if ctrl & self.FIN: ctrl_str += '/FIN'
		if ctrl & self.SYN: ctrl_str += '/SYN'
		if ctrl & self.RST: ctrl_str += '/RST'
		if ctrl & self.PSH: ctrl_str += '/PSH'
		if ctrl & self.ACK: ctrl_str += '/ACK'
		if ctrl & self.URG: ctrl_str += '/URG'

		print_output("Source Port", "{}", (self.tcp_sport,))
		print_output("Destination Port", "{}", (self.tcp_dport,))
		print_output("Sequence Number", "{}", (self.tcp_seq,))
		print_output("ACK Number", "{}", (self.tcp_ack,))
		print_output("Data Offset", "{} bytes", (self.tcp_off*4,))
		print_output("ECN", "{}", (ecn_str.strip(',').strip(),))
		print_output("Control Bits", "{}", (ctrl_str.strip('/'),))
		print_output("Window", "{}", (self.tcp_win,))
		print_output("Checksum", "0x{:04x}", (self.tcp_sum,))
		print_output("URG Pointer", "{}", (self.tcp_urgp,))

		if self.tcp_off > 5:
			## Parse options
			opts = self.tcp_opts

			## Loop through the option data, checking the kind and length and
			## Pulling out the option value based on those values.
			pos = 0
			for i in range(0, len(opts)):
				## Skip over option values we already pulled out
				if i < pos: continue

				## Get the kind, length, and value
				try:
					k, l, v = opts[i], opts[i+1], None

					## Hit the last option
					if k == 0 and l == 0: break

				except IndexError:
					break

				## k == 0 or k == 1 have no values
				if k <= 1: l = 1

				## Get a hex representation of the option value
				if l > 2: v = binascii.hexlify("".join([chr(s) for s in opts[pos+2:pos+l]]))

				## Adjust the position to consume the option key, length, and value
				pos += l

				## Output the option data
				self.print_option(k, v)

		print_section_footer()


class tcp_packet(ctypes.Structure):
	## How many packets have been created
	num = 0

	_fields_ = [
		("ether_header", ether_header),
		("ip_header", ip_header),
		("tcp_header", tcp_header),
		("data", ctypes.c_char_p)
	]

	def __init__(self, pkt):
		self.ether_header = ether_header(*struct.unpack("!6B6BH", pkt[0:14]))
		self.ip_header = ip_header(*struct.unpack("!BBHHHBBHII", pkt[14:34]))
		self.tcp_header = tcp_header(*struct.unpack("!HHLLHHHH", pkt[34:54]))
		self.check_options(pkt[54:])
		tcp_packet.num += 1

	## Determine if there are TCP options to parse
	def check_options(self, data):
		offset = self.tcp_header.tcp_off

		if offset > 5:
			## Parse options
			options_len = (offset*4) - 20
			s = struct.unpack("!{0}s".format(options_len), data[0:options_len])
			s0 = binascii.hexlify(s[0])
			b = [int("{}{}".format(s0[i], s0[i+1]), 16) for i in range(0,len(s0),2)]
			self.tcp_header.tcp_opts = tuple(b)

			## Anything left is data
			if len(data) > options_len:
				self.data = data[options_len:]

		else:
			self.data = data

	def dump(self):
		self.ether_header.dump()
		self.ip_header.dump()
		self.tcp_header.dump()

		print_section_header("TCP DATA #{}".format(self.num))
		print self.data
		print_section_footer()


## Promisc flag
IFF_PROMISC = 0x100

## Found in /usr/include/bits/ioctls.h
SIOCGIFFLAGS = 0x8913 ## get flags
SIOCSIFFLAGS = 0x8914 ## set flags

## Header and footer formatting functions
def print_section_header(s): print "{:=^78}".format(" "+s+" ")
def print_section_footer():  print "{:=^78}\n".format("")

## s = Label as a string
## f = Format for 'v' as a string
## v = tuple of values matching 'f' format
def print_output(s, f, v): print ("{:<20} " + f).format(s, *v)

## Format a MAC address as XX:XX:XX:XX:XX:XX
## The input is an ether_header.eth_Xhost entry
def format_mac(eh):
	return ":".join(["{:02x}".format(eh[i]) for i in range(0, len(eh))])


## Parse program options
prog_args = sys.argv
prog_protos = ['tcp','udp']
prog_host = ['src','dst']

try:
	pos = 1
	for i in range(1, len(prog_args)):
		if i < pos: continue

		arg = prog_args[i]

		if arg in prog_host and prog_args[i+1] == "host":
			formatter[arg] = {"host": prog_args[i+2].split(',')}
			pos += 3

		elif arg == "host":
			formatter["host"] = prog_args[i+1].split(',')
			pos +=2 

		elif arg in prog_protos and prog_args[i+1] == "port":
			formatter[arg] = {"port": prog_args[i+2].split(',')}
			pos += 3

		elif arg == "port":
			formatter["port"] = prog_args[i+1].split(',')
			pos += 2

except IndexError:
	pass

## Create our raw socket
sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

## Set up the ifreq
ifr = ifreq()
ifr.ifr_ifrn = IF_NAME

## Get the current flags so we don't clobber them
fcntl.ioctl(sock.fileno(), SIOCGIFFLAGS, ifr)

## Put that bad boy in promisc mode
ifr.ifr_flags |= IFF_PROMISC
fcntl.ioctl(sock.fileno(), SIOCSIFFLAGS, ifr)

## Let's receive some data
try:
	while True:
		## Get a packet
		pkt = sock.recv(4096)
		packet = tcp_packet(pkt)

		## Only process IP packets
		if packet.ether_header.eth_type == 0x0800:
			## Get the src host filter
			f_ip_src = formatter.get("host", []) + formatter.get("src", {'host':[]}).get("host", [])
			## Get the dst host filter
			f_ip_dst = formatter.get("host", []) + formatter.get("dst", {'host':[]}).get("host", [])
			## Get the port filter
			f_port = formatter.get("port", [])

			## Check if we want to capture from the src or dst 
			ip_src = packet.ip_header.ip_src_dotted()
			ip_dst = packet.ip_header.ip_dst_dotted()

			if ip_src in f_ip_src or ip_dst in f_ip_dst:
				proto = packet.ip_header.ip_proto

				if proto == 6:
					## Get the TCP port filter
					f_port += formatter.get("tcp", {'port':[]}).get("port", [])

					## Check if we want to capture from the src or dst port
					tcp_src_port = str(packet.tcp_header.tcp_sport)
					tcp_dst_port = str(packet.tcp_header.tcp_dport)

					if tcp_src_port in f_port or tcp_dst_port in f_port:
						packet.dump()

					else:
						pass
						#print "IGNORING TCP {}:{} -> {}:{}".format(
						#	ip_src, tcp_src_port, ip_dst, tcp_dst_port)

				elif proto == 17:
					print "UDP"

				elif proto == 1:
					print "ICMP"

				else:
					print "UNKNOWN ({})".format(proto)

			else:
				pass
				#print "IGNORING {} -> {}".format(ip_src, ip_dst)


except (KeyboardInterrupt, SystemExit):
	pass

finally:
	## Remove promisc
	ifr.ifr_flags &= ~IFF_PROMISC
	fcntl.ioctl(sock.fileno(), SIOCSIFFLAGS, ifr)

	## Close the socket
	sock.close()

