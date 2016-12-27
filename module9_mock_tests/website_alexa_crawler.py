
#===========================MOCK SAMPLE 3================================#
# Write a simple web crawler which fetch the robots.txt file of a website#
# run your crawler on the top 1000 sites a ranked by Alexa		 #
# report on the top 40 directory names which are disallowed for robots   #
#========================================================================#
import threading
import Queue
import time
import sys
import urllib
import os


disallow = []
 

def crawler(website):
	print website
	urlopen = urllib.urlopen(website+'/robots.txt')

	print "Status : %s" % urlopen.code

	data=urlopen.readlines()

	sdata = ''.join(data)

	#print sdata

	fname = sys.argv[1] + '_robot.txt'

	f = open(fname,'w')

	f.write(sdata)

	f.close()

	f=open(fname,'r')

	for line in f:
		if line.find('Disallow')>=0:
			temp = line[line.find('/'):]
			temp = temp.strip()
			disallow.append(temp)
	f.close()
	os.remove(fname)




if len(sys.argv) < 2:
	print "usage: python website_alexa_crawler.py list.txt"
else:
	w = open(sys.argv[1],'r')
	for link in w:
		website = 'http://'+link
		try:
			crawler(website.strip())
		except:
			print sys.exc_info()[1]
			pass
print "Total listed path :",len(disallow)

disallow_set = set(disallow)

for i in disallow_set:
	print i
