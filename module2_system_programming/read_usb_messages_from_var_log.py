import sys

f = open('/var/log/kern.log','r')

print "Displaying USB debug messages"

for i in f:
	if i.lower().find('usb')>=0:
		print i

f.close()
