from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#finds all the tags which start with b
for tag in soup.find_all(re.compile("^b")):
 print(tag.name)

#finds all tags which contain letter 't'
for tag in soup.find_all(re.compile("t")):
 print(tag.name)


# .select() finds css selectors
#can find tags
soup.select("title")

#find tags beneath other ttgas
soup.select("p > a")

#finds all links containing 'elsie'
soup.find_all(href=re.compile("elsie"))

naya_page = urlopen("http://cse.iith.ac.in/?q=People/Faculty")

#prints the html code of the webpage
#print(naya_page.read())



#the varible c will contains the HTML code of the page
#c = BeautifulSoup(naya_page,'html.parser') # takes 1.963 sec
#we can use lxml instead which is faster 
c = BeautifulSoup(naya_page,'lxml')    #takes 1.568 sec

print("\nPrinting the 1st heading"+c.h1.text)
print("Printing the title : "+c.title.text)


# .contents has all the children in the tag
print(c.h1.contents)
print()
print(len(c.contents))
print(c.contents[0])
print(c.contents[1])


# .parent has the elements parent
title_tag = c.title

#print(c.prettify())

#printing all the links in the webpage
#for link in c.find_all('a'):
 #print(link.get('href'))


#prints the name of proff.
#name_box = soup.find('a',attrs = {'href':'http://cse.iith.ac.in/profile/faculty/kotaro/' })
name_box = soup.find('a',attrs = {'href':'http://www.iith.ac.in/~msingh/' })
name = name_box.text
print (name)



#this prints all the text on the webpage
g = c.get_text()

file = open("prof.txt",'w')
#file.write(g)
print("scraping ... \n\n\n\n\n\t\tDone")
