import os
import datetime
fname = raw_input("Enter the file with path:")
if os.path.isfile(fname):
	print "File exists"
	print "Absolute Path : %s" % os.path.abspath(fname)
	print "File Size : %s" % os.path.getsize(fname)
	print "File Creation : %s" % datetime.datetime.fromtimestamp(os.path.getmtime(fname))
 
