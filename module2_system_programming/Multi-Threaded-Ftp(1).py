#!/usr/bin/env python

import threading
import Queue
import time
from ftplib import FTP

# Thanks to SPSE-445 for the list :) 
ftpHostList = [ 'ftp.x.org', 'ftp4.FreeBSD.org', 'ftp.ncsa.uiuc.edu', 'ftp.mozilla.org', 'ftp.crans.org' ]

class WorkerThread(threading.Thread) :

	def __init__(self, queue, tid) :
		threading.Thread.__init__(self)
		self.queue = queue
		self.tid = tid
		print "Worker %d Reporting for Service Sir!" %self.tid

	def run(self) :
		while True :
			host = None 

			try :
				host = self.queue.get(timeout=1)

			except 	Queue.Empty :
				print "Worker %d exiting..." % self.tid
				return
			
			# login to ftp host anonymously and list the dirs 
			try :
				conn = FTP(host)
				conn.login()
				print 'Host: ' +host
				print conn.retrlines('LIST')
			except :
				print "Error in listing " +host
				raise 

			self.queue.task_done()


queue = Queue.Queue()

threads = []
for i in range(1, 10) :
	print "Creating WorkerThread : %d"%i
	worker = WorkerThread(queue, i) 
	worker.setDaemon(True)
	worker.start()
	threads.append(worker)
	print "WorkerThread %d Created!"%i
	
for host in ftpHostList :
	queue.put(host)

queue.join()

# wait for all threads to exit 

for item in threads :
	item.join()

print "Scanning Complete!"

