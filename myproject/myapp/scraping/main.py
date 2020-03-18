
import colorama
from myapp.scraping.crawl import crawl
from myapp.scraping.showinfo import showinfo
from myapp.scraping.is_valid import is_valid
from myapp.scraping.shownested import shownested
from myapp.scraping.get_all_website_links import get_all_website_links
def scrap(keyw,sizeS,maxurl):
 print(keyw)
 print(sizeS)
 print(maxurl)

 colorama.init()
 GREEN = colorama.Fore.GREEN
 GRAY = colorama.Fore.LIGHTBLACK_EX
 RESET = colorama.Fore.RESET
 internal_urls = set()
 external_urls = set()
 total_urls_visited = 0
 if type=="keywords":
  print("keywords")
 else:
  print("url")
 
 
 my_list = []
 listofurl=[".com",".jp",".co.uk",".org",".net",".int",".edu",".gov",".in",".jp",".co"]

 for url in search(keyw, tld='com',pause=2):

    #print(url)
    for allurl in listofurl:
     if allurl in url:
      x=url.partition(allurl)
      p=x[0]+x[1]  
      break
     
    if (len(my_list)==sizeS):
     print(len(my_list))  
     break 
    res = [ele for ele in my_list if(ele in p)]
    if not res:
     my_list.append(p) 
     print(my_list)
 showinfo(my_list)     



  




