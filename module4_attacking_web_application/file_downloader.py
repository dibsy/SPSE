# Credits : http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python

import urllib
import sys

url = sys.argv[1]

urlopen = urllib.urlopen(url)

fname = url.split('/')[-1]
size = urlopen.headers.getheader('Content-Length')
print "Download Size : %s" % size

file = open(fname,'wb')
downloaded = 0
blocksize = 8192
while True:
	buffer = urlopen.read(blocksize)
	if not buffer:
		break
	downloaded +=len(buffer)
	file.write(buffer)
	status = "Downloaded %s of %s" % (downloaded,size)
    	print status,

file.close()


