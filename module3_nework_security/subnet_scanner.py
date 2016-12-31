from scapy.all import *
for lsb in range(0,10):
	ip = "192.168.116."+str(lsb)
	print "Testing IP:",ip
	arpRequest=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip,hwdst="ff:ff:ff:ff:ff:ff")
	arpResponse=srp1(arpRequest,timeout=1,verbose=0)
	if arpResponse :
		print "IP: "+arpResponse.psrc+" MAC: "+arpResponse.hwsrc
