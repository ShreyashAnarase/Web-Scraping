'''
Ongoing 
to print the results of the recent matches played by RMA
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.realmadrid.com/en/football/schedule'

source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')
'''
result =soup.find('small',{'class':'m_match_teams_results'})
print(result)

gives NONE as output
'''
for td in soup.find_all('td',{'class':'m_match_teams'}):
 print(td.text) 
 break

for tr in soup.find_all('tr',{'class':'m_match_week'}):
 print(tr.text) 
 break 

for td in soup.find_all('td',{'class':'m_match_date'}):
 print(td.text) 
 break

 #remove break for all