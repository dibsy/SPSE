import sys
import mechanize

url = sys.argv[1]

br = mechanize.Browser()

#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# [('User-agent', 'Firefox')]

response = br.open(url)
#print response.read()      # the text of the page

response1 = br.response()  # get the response again
#print response1.read()     # can apply lxml.html.fromstring()

for form in br.forms():
	print form
