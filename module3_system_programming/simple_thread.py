import thread
import time

def worker_thread(id):
	print "Thread ID %d now alive" % id
	
	count = 1
	while True:
		print "Thread with id %d has counter value %d" % ( id,count)
		time.sleep(2)

for i in range(5):
	thread.start_new_thread(worker_thread,(i,))

print "Main Thread"
while True:
	pass
