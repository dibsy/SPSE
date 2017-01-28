#!/usr/bin/env python

import socket, select

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 8004

tcpSocket.bind(("0.0.0.0", port))

tcpSocket.listen(10)

print "Waiting for a connection on port:",port


holeinsock = []

while True:

	read, write, ex = select.select([tcpSocket] + holeinsock, [], [])
	for s in read :
		if s is tcpSocket :
			(client, (ip, port)) = tcpSocket.accept()
			print "Received a connection from IP %s on port %s"% (ip, port)
			print "Starting ECHO output..."
			holeinsock.append(client)

		else :
			data = s.recv(16)
			if data == "" :
				holeinsock.remove(s)
				print "Closing connection..."
			else:
				print "Received this from IP %s on port %s: %s"% (ip, port, data)
 				client.send("Client you sent the server this: " + data)

