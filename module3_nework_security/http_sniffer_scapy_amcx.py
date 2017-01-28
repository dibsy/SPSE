#!/usr/bin/python
from scapy.all import *
import re

def filterhttp(p):
    if p.haslayer(Raw):
        packet=str(p["Raw"])
        header = packet.split("\r\n")

        if re.match("^GET.+",header[0]):
            printHttpHeader(header)
        elif re.match("^POST.+",header[0]):
            printHttpHeader(header)
        elif re.match("^HTTP.+",header[0]):
            del header[len(header)-1]
            printHttpHeader(header)
    else:
        pass

def printHttpHeader(h):
    
    for i in h:
        print str(i)
    print "***********************************************************************"

if __name__=="__main__":
    sniff(iface="eth0",filter="tcp port 8000",prn=filterhttp)


