
# returns all the links prrsnet on a webpage

from bs4 import BeautifulSoup
import requests

url = input("Enter a website to extract urls from: \n")

r = requests.get("http://"+ url)

data = r.text

soup = BeautifulSoup(data,'lxml')

for link in soup.find_all('a'):
	print(link.get('href'))