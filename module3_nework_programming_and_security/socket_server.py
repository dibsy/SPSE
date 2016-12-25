import socket

tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcpSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

tcpSocket.bind(('0.0.0.0',8001))

tcpSocket.listen(2)

print "Waiting for a client"
(client,(ip,sock)) = tcpSocket.accept()

print "Received Connection from " , ip

data ='dummy'

while len(data):
	data = client.recv(2048)
	print "Client Sent ",data
	client.send(data)

print "Closing Connection"
client.close()
