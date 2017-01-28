#!/usr/bin/python
# This sample code is part of the SecurityTube Python Scripting Expert course and certification
# Website : http://securitytube-training.com
# Author: Vivek Ramachandran

import os
import pwd # password database module 
import sys

fileStat = os.stat(sys.argv[1])

if fileStat :
	# get file size in bytes 
	print 'Filename: %s' % sys.argv[1]
	print 'Size in bytes: %d' %fileStat.st_size 
	print 'Owner: uid is %d, username is %s' %( fileStat.st_uid, pwd.getpwuid(fileStat.st_uid).pw_name)

