
#https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

import csv
from datetime import datetime

from bs4 import BeautifulSoup
from urllib.request import urlopen


page = urlopen("https://www.bloomberg.com/quote/SPX:IND")

#parse the page into bs format
soup =BeautifulSoup(page,'html.parser')
# now the variable soup contains the html of the page

name_box = soup.select_one("h1.class.name")
#name_box = soup.find('h1',attrs ={'class': 'name'})
#name = name_box.text.strip()
print (name_box)

#to get the price
price_box = soup.find('div',attrs={'class':'price'})
price= price_box.text
print(price)

''' FOLLOWING PART IF YOU WANT TO WRITE
 THE DATA TO A CSV FILE

'''

# open a csv file with append
'''
myfile = open('index.csv','a') 
with myfile: 
 writer = csv.writer(myfile)
 writer.writerow([name, price, datetime.now()])
'''
 #awesome