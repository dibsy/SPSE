import signal

def ctrl_handler(signum,frm):
	print("Cannot be killed")


print "Signal Handler. Trying killling with Ctrl+C"
signal.signal(signal.SIGINT,ctrl_handler)

print "Done"

while True:
	pass
