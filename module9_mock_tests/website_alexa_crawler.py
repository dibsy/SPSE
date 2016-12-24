
#===========================MOCK SAMPLE 3================================#
# Write a simple web crawler which fetch the robots.txt file of a website#
# run your crawler on the top 1000 sites a ranked by Alexa		 #
# report on the top 40 directory names which are disallowed for robots   #
#========================================================================#
import sys
import urllib

disallow = {}



def crawler(website):
	print website
	urlopen = urllib.urlopen(website+'/robots.txt')

	print "Status : %s" % urlopen.code

	data=urlopen.readlines()

	sdata = ''.join(data)

	print sdata	

	fname = sys.argv[1] + '_robot.txt'

	f = open(fname,'w')

	f.write(sdata)

	f.close()

	f=open(fname,'r')

	#for line in f:
	#	if line.find('Disallow')>=0:
	#		print line

website = 'http://'+sys.argv[1]
crawler(website)
