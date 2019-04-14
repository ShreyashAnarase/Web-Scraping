import requests
from bs4 import BeautifulSoup

print ('Enter the word you want to the meaning of ')
word =input()

print ()
url = 'https://en.oxforddictionaries.com/definition/'+word

source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')

'''   
Uncomment this and run to find meaning along with subsense

for m in soup.find_all('span',{'class':'ind'}):
	print(m.text)
'''

m = soup.find('div',{'class':'trg'})
main_mean = m.find('span',{'class':'ind'})
print(main_mean.text)

