#!/usr/bin/env python
# SPSE 589

from scapy.all import *

while True:
        sr(IP(dst="192.168.1.1")/UDP()/fuzz(DNS()  ), inter = 1, timeout = 1  )


