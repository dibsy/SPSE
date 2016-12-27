import sys
import urllib
try:
	url = 'http://'+sys.argv[1]
	urlopen = urllib.urlopen(url)
	data = urlopen.read()
	print data
except:
	print "Error:",sys.exc_info()	

