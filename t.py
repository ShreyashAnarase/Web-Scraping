from bs4 import BeautifulSoup as soup
s ='<div class="fi-mu-list today" data-matchesdate="20180619">'
result = soup(s, 'html.parser').find('div')['data-matchesdate']
print(result)