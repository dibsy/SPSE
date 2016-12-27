import urllib
from bs4 import BeautifulSoup

urlopen=urllib.urlopen('https://github.com')
data = urlopen.read()

bs = BeautifulSoup(data,'html.parser')

# Print Preety
#print bs.prettify()

#print bs.find_all('a')
for i in bs.find_all('a'):
	print i.get('href')

