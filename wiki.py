#prints the contents of any topic on wikipedia you want

from bs4 import BeautifulSoup
from urllib.request import urlopen

#nprint('Enter the url of the page for which you want the contents ')

page = urlopen("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(page,'lxml')


for i in soup.find_all('span',{'class':'toctext'}):
	print(i.text)