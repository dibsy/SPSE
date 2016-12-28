import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data=self.request.recv(1024)
		print "%s Client Says: %s" %(self.client_address[0],self.data)
		self.request.sendall(self.data)
if __name__ == "__main__":
	HOST = "0.0.0.0"
	PORT = 9003
	server = SocketServer.TCPServer((HOST,PORT),MyTCPHandler)
	server.serve_forever()
