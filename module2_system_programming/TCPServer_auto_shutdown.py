import SocketServer
import signal
import time
import sys
import os
import threading
def auto_shutdown(signum,frm): 
	print "Shutting down the server"
	os.kill(os.getpid(), signal.SIGUSR1)

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def fun(self,signum,frm):
		print "Soory you can't kill me"
	def handle(self):
		self.data=self.request.recv(1024)
		print "%s Client Says: %s" %(self.client_address[0],self.data)
		self.request.sendall(self.data)

def wait_till(activetime):
	#print "Active Time:%s seconds\n" % activetime
	start=time.time()
	while int(time.time() - start) < int(activetime):
		#print "Seconds Elasped : ",int(time.time()-start)
		pass
	print "I am done ... Shutting down the server after %s seconds" % activetime
	server.shutdown()


if __name__ == "__main__":

	activetime=sys.argv[1]
	#print "Active:",activetime
	HOST = "0.0.0.0"
	PORT = 9007
	#signal.signal(signal.SIGUSR1, auto_shutdown)
	global server
	server = SocketServer.TCPServer((HOST,PORT),MyTCPHandler)
	d = threading.Thread(name='t',target=wait_till,args=(activetime,))
	d.setDaemon(True)
	d.start()
	print "Starting server for %s seconds" %activetime
	server.serve_forever()

