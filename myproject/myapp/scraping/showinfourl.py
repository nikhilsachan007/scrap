import requests
from bs4 import BeautifulSoup
import csv
import re
from validate_email import validate_email
from myapp.scraping.crawl import crawl
from itertools import zip_longest
max_urls=1
def showinfourl(url):
    print("the list is as ")
    
    urll=[]
    urll.append(url)
    response = requests.get(url,timeout=20)
    soup = BeautifulSoup(response.text,'lxml')
    metas = soup.find_all('meta')
    response.close()
    print("The description of the website  is")
    try:
       descriptionc= ([meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description'])
       print (descriptionc)
    except:
       print("No description of the website")
    phone=[]
    phone1=[]
    email=[]
    validemail=[]
    phone = re.findall(r'([0-9][0-9]+-[0-9][0-9][0-9][0-9]+-[0-9][0-9][0-9][0-9])', response.text)
    phone1 = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response.text)
    phone=phone+phone1  
    print(phone)  
    email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response.text)
    print(email)
    print("Title")
    titlestring=[soup.title.string]  
    print(soup.title.string)
    try:
      myheading=soup.find('div', attrs={'id': 'header'})
      if myheading:
          print("Heading")  
          print(myheading.text)
    except:
      print("")
    with open('output.csv', 'w',encoding='utf-8') as outcsv:
     writer = csv.writer(outcsv)   
     writer.writerow(["url", "Title", "description","telephone","Email"])
     for row in zip_longest(urll, titlestring,descriptionc,phone,email):
        writer.writerow(row)

     p = Scraping(keywords='Petr', title='title',description='description',telephone='451485',email='ncjenjen')
     p.save() 