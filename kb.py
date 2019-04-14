# kevin bacon 
# use regular expresions

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
page = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(page,'lxml')

#for link in bsObj.find_all('a'):
#	if 'href' in link.attrs:
#		print(link.attrs['href'])

# what we need is urls of article pages
#ignore other links
# common prop are 
''' 1) id =bodyContent->div
2) URLS dont contain colons(:)  - the category pages contan 'em
3) urls begin with /wiki/

'''
for link in bsObj.find('div',{'id': 'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
	if 'href' in link.attrs:
		print(link.attrs['href'])
