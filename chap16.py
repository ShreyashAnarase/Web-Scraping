
'''
  Gonna scrape/crawl through all the chapters on
  automatetheboringstuff.com and convert to pdf


  #####    INCOMPLETE        ###
  ##CURENTLY JUST WRITES THE CHAPTER 16 AS A TEXT file
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen("https://automatetheboringstuff.com/chapter16/")
soup = BeautifulSoup(page,'lxml')

g = soup.get_text()

file = open("chap16.txt",'w')
file.write(g)