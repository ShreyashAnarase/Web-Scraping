from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen("https://www.accuweather.com/en/in/pune/204848/weather-forecast/204848")
soup = BeautifulSoup(page,'lxml')


#a = soup.find('div', attrs={'class','panel'}).text
a = soup.find_all('ul', {'class' :' top-cities lt'}).text

print(a)


#file = open("hi.txt",'w')
#file.write(a)