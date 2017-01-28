#!/usr/bin/env python2.7

from SocketServer import ThreadingTCPServer, BaseRequestHandler
import threading

server_addr = '127.0.0.1'
server_port = 7000
gLock = threading.Lock()

class EchoHandler(BaseRequestHandler):
        def handle(self):
                self.data = None

                while True:
                        self.data = self.request.recv(1024)
                        if not self.data: break

                        gLock.acquire()
                        print "Server received {0} bytes on thread {1} from {2}:{3}".format(len(self.data),
                                threading.current_thread().name, *self.client_address)
                        print "   {0}".format(self.data)
                        gLock.release()

                        self.request.send(self.data)


try:   
        s = ThreadingTCPServer((server_addr, server_port), EchoHandler)
        s.allow_reuse_address = True

        print "Server started"
        s.serve_forever()

except (KeyboardInterrupt, SystemExit):
        pass

finally:
        s.shutdown()
        print "Server stopped"
 


