import os
import urllib
import subprocess
print "Twitter Bot"

pastebin_api_key = 'YOUR API KEY HERE'
pastebin_url = 'http://pastebin.com/api/api_post.php'
pastebin_username = 'YOUR USERNAME HERE'
pastebin_password = 'YOUR PASSWORD HERE'

#tweet_raw_data = ''

#tweet_command = ''

#pastebin_data = ''

def get_api_user_key():
	url = 'http://pastebin.com/api/api_login.php'
	data = {}

	params = urllib.urlencode({'api_dev_key': pastebin_api_key, 'api_user_name': pastebin_username, 'api_user_password':pastebin_password })
	urlopen = urllib.urlopen(url,params)
	api_user_key = urlopen.read()
	return api_user_key

def pastebin_activities():
	output = execute_command()
	api_user_key = get_api_user_key()
	params = urllib.urlencode({'api_dev_key':pastebin_api_key ,'api_option':'paste','api_paste_code':output,'api_paste_private':1})
	urlopen=urllib.urlopen(pastebin_url,params)
	res = urlopen.read()
	print res

def scan_tweet():
	#global tweet_raw_data,tweet_command 
	tweet_raw_data = '#SPSEx64 ifconfig -a'
	tweet_command = 'uptime'

def execute_command():
	#print "Executing Command:\n"
	proc = subprocess.Popen('uptime', stdout=subprocess.PIPE)
	output = proc.stdout.read()
	return output 


scan_tweet()
execute_command()
#get_api_user_key()
pastebin_activities()

