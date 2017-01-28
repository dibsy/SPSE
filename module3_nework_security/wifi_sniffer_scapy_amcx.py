#!/usr/bin/python
from scapy.all import *

aps=[]

def wifiscan(p):
    if p.haslayer(Dot11Beacon):        
        bssid= p[Dot11].addr3        
        if bssid not in aps:
            aps.append(bssid)            
            print str(p[Dot11].addr3) + "-" + str(p[Dot11Elt].info)
        else :
            pass        
    else:
        pass

if __name__=="__main__":
    sniff(iface="mon0",prn=wifiscan)



