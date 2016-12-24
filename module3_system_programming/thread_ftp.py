#Create a list of FTP sites
#Create a WorkerThread and Queue which can login to these sites and list the root directory and exit
#use 5 threads for this job and 10 FTP sites

import threading
import Queue
import time
from ftplib import FTP

class WorkerThread(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.queue = queue

	

	def run(self):
		print "In WorkerThread"
		while True:
			ftpURL = self.queue.get()
			print "FTPing %s!" % ftpURL
			ftp = FTP(ftpURL)
			ftp.login()
			print ftp.dir()
			print "Done FTPing for %s!" % ftpURL
			self.queue.task_done()
			

queue = Queue.Queue()

for i in range(5):
	print "Creating WorkerThread :%d" %i
	worker = WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "WorkerThread %d Created" %i

f = ['ftp.kernel.org','ftp.cc.umanitoba.ca','ftp.freenet.de',]
for ftpSite in f:
	queue.put(ftpSite)

queue.join()

print "All tasks over"
