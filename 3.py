
    # FINDS THE NAMES & email ids OF ALL PROFESSORS OF  IITH CSE DEPT. 


from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen("http://cse.iith.ac.in/?q=People/Faculty")
soup = BeautifulSoup(page,'lxml')

title_tag = soup.title
print(title_tag.text)

for tag in soup.find_all('tr'):
 name = tag.strong.text
 print(name)

#prints all the mails which are hyperlinks
for span in soup.find_all('span',{'style':'color:rgb(0, 0, 0)'}):
 for mail in span.find_all('a'):
 	#print(mail.get('href') )   earlier it was just this line in loop
 	m = str(mail.get('href')).split(':')
 	m.remove('mailto')
 	#the star unpacks the list and return every element in the list.
 	print(*m)
    

