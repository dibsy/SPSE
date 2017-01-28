#!/usr/bin/python

import socket
import sys
from multiprocessing import Process

def EchoClientHandler(clientSocket, addr) :
	while 1:
		client_data  = clientSocket.recv(2048)
		if client_data :
			clientSocket.send(client_data)
		else :
			clientSocket.close()
			return



echoServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

echoServer.bind(("0.0.0.0", int(sys.argv[1])))

echoServer.listen(10)

workerProcesses = []

while 1:
	cSock, addr = echoServer.accept()
	# start a new thread to service 
	print "Starting new thread to service client \n"
	worker = Process(target=EchoClientHandler, args= (cSock, addr))
	worker.start()
	workerProcesses.append(worker)
		


