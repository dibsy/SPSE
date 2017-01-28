#!/usr/bin/python
# This sample code is part of the SecurityTube Python Scripting Expert course and certification
# Website : http://securitytube-training.com
# Author: Vivek Ramachandran

import signal
import sys

def SigAlarmHandler(signal, frame) :
	print "Received alarm ....Shutting down..."
	sys.exit(0)

signal.signal(signal.SIGALRM, SigAlarmHandler)
signal.alarm(1000)

print "Starting work ... waiting for alarm to quit :) "
while True :
	# do something 
	pass



