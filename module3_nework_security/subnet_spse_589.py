#!/usr/bin/env python
import sys, socket, struct, fcntl

#  struct ifreq ifr;  (ifr contains "ethx")
#  ioctl(socket, SIOCGIFNETMASK, &ifr)


nic = sys.argv[1]

def getsubnet(nic):
        sock = socket.socket(socket.AF_INET)
        subnet = fcntl.ioctl(sock, 0x891b, struct.pack('256s', nic))[20:24]
        result = socket.inet_ntoa(subnet)
        print 'The subnet associated with %s is %s'% (nic,result)

getsubnet(nic)

