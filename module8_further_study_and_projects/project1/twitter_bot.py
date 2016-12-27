import os
print "Twitter Bot"

#tweet_raw_data = ''

#tweet_command = ''

#pastebin_data = ''

def pastebin_activities():
	print "PasteBin Activites"

def scan_tweet():
	global tweet_raw_data,tweet_command 
	tweet_raw_data = '#SPSEx64 ifconfig -a'
	tweet_command = 'uptime'

def execute_command():
	print "Executing Command:\n"
	print tweet_command
	pastebin_data=os.system(tweet_command)
	print pastebin_data


scan_tweet()
execute_command()
pastebin_activities()
