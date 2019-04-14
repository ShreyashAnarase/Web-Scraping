from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re


page = "http://www.thehindu.com/news/"
src =requests.get(page)
txt = src.text
soup = BeautifulSoup(txt,'lxml')


sections = soup.find_all('a',href=re.compile('^(http://www.thehindu.com/news/national/)((?!:).)*$'))
#test = sections[0]
#print(test['href'])
common ='http://www.thehindu.com/news/national/'

for section in sections:
	n = str(section['href'])
	k =n.split('national/')[1]
	l = k.split('-')
	#if l.endswith('.ece'):
	#	l = l.split('.ece')
	'''
	for word in l:
		if word.endswith('.ece'):
			continue
		if '/' in word:
			word =word.split('/')
			print(*word,end ='')
		
			#print(word[0])
	'''
	
	print(*l)

	
	#string  = ''.join(l)

'''
file = open("news.txt",'w')
file.write(string)
'''
