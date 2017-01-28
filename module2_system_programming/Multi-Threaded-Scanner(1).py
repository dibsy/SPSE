#!/usr/bin/env python

import threading
import Queue
import time
from scapy.all import *

class WorkerThread(threading.Thread) :

	def __init__(self, queue, tid) :
		threading.Thread.__init__(self)
		self.queue = queue
		self.tid = tid
		print "Worker %d Reporting for Service Sir!" %self.tid

	def run(self) :
		total_ports = 0
		while True :
			port = 0
			try :
				port = self.queue.get(timeout=1)
			except 	Queue.Empty :
				print "Worker %d exiting. Scanned %d ports ..." % (self.tid, total_ports)
				return
			# port scanning to begin 
			# we rely on scapy to do this
			ip = sys.argv[1]
			response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), verbose=False, timeout=.2)
			# only checking for SYN-ACK == flags = 18 
			# filtererd ports etc. is another story altogether
			if response :
				if response[TCP].flags == 18 :
					
					print "ThreadId %d: Received port number %d Status: OPEN" %(self.tid, port)
			self.queue.task_done()
			total_ports += 1


queue = Queue.Queue()

threads = []
for i in range(1, 10) :
	print "Creating WorkerThread : %d"%i
	worker = WorkerThread(queue, i) 
	worker.setDaemon(True)
	worker.start()
	threads.append(worker)
	print "WorkerThread %d Created!"%i
	
for j in range (1,1000) :
	queue.put(j)

queue.join()

# wait for all threads to exit 

for item in threads :
	item.join()

print "Scanning Complete!"

