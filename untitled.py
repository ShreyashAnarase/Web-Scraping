import requests
from bs4 import BeautifulSoup
from datetime import date
import re

date = str(date.today())

date = date.split('-')
month = date[1]
date = date[2]
#print(month)
print(date)

'''
print('Choose an option')
print('1) Today\'s matches')
print('2) All matches')
'''

url = 'https://www.fifa.com/worldcup/matches/'

source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')



single = soup.find('div',{'class':'fi-mu-list'})

for l in single.find_all('a'):
	print(l.get('href'))
#for link in single.find_all(href=re.compile("worldcup/matches/match")):
#	print(link)

#for mat in soup.find_all('span',{'class':'fi-mu-list__head__date'}):
#	print(mat.text)

for mat in  soup.find_all('span',{'class':'fi-mu-list__head__date'}):
    mat = str(mat.text)
    ref =(mat.strip())
    ref1 =ref.split('\n')
    ref2 = ref1[0]	       #day
    ref3 = ref1[1].strip()         #date
    ref4 = ref1[2]			#month
    #print(ref1)
    print(ref2)
    print(ref3)
    print()
    if ref3 == date:

    	break;
    


'''
def get_score(match_url):
	source_code = requests.get(match_url)
    plain_text = source_code.text
    soup1 = BeautifulSoup(plain_text,'lxml')
    teams =[]
    for team in soup1.find_all('span',{'class':'fi-t__nText '}):
    	teams = str(team.text) + teams

    score = soup1.find('span',{'class':'fi-s__scoreText'}).text

    print(*teams)
    print(score)



#matches for today
for day in soup.find_all('div',{'class':'fi-mu-list'}):
	
	for link in day.find_all('a'):
		href= link.get('href')
		match_url = 'www.fifa.com'+id
		get_score(match_url)
'''

