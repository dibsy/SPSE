#!/usr/bin/python

# apt-get install python-netifaces

import netifaces
import socket 

print 'Interfaces available: ' 
print netifaces.interfaces()

eth0_addresses = netifaces.ifaddresses("eth0")

interface_info = eth0_addresses[socket.AF_INET][0]

print interface_info['addr']
print interface_info['netmask']

 
