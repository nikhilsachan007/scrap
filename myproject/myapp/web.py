from urllib.request import urlopen
from bs4 import BeautifulSoup
a=urlopen("https://www.facebook.com")
soup=BeautifulSoup(a.read(),'lxml')
for link in soup.findAll("a"):
	if 'href' in link.attrs:
		print(link.attrs['href'])