#!/usr/bin/python
# This sample code is part of the SecurityTube Python Scripting Expert course and certification
# Website : http://securitytube-training.com
# Author: Vivek Ramachandran

import sys

logFile = open(sys.argv[1])

print "Printing all lines with USB in it ... "

for line in logFile.readlines() :
	if line.lower().find("usb") != -1 :
		print line

print "Done!"

