import requests
from myapp.models import Students
from bs4 import BeautifulSoup
import csv
import re
from validate_email import validate_email
from myapp.scraping.crawl import crawl
from itertools import zip_longest

max_urls=1
def showinfo(my_list):

 



  print("the list is as ")
  count=[0]
  for list in my_list:
    
    print (list)
    siteurl=[list]
    response = requests.get(list,timeout=20)
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
    if email:
       print(email)
    else:
       newurls=crawl(list, max_urls=max_urls)
       for new in newurls or []:
        if not email:
         email=shownested(new)
         print(email)
        else:
         break 
    for m in email:
     is_valid = validate_email(m,verify=True)
     validemail=[m];
     if is_valid==True:
      print(is_valid)
      break
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
     count[0]=count[0]+1
     writer.writerow(["索引","ウェブサイトのURL","題名", "", "説明", "メールアドレス"])
     for row in zip_longest(count,siteurl,titlestring, descriptionc,phone,validemail):
        writer.writerow(row)