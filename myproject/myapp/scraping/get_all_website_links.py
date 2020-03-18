from urllib.request import urlparse, urljoin
import requests
from bs4 import BeautifulSoup
from myapp.scraping.is_valid import is_valid
internal_urls = set()
def get_all_website_links(url):
    urls = set()
    print("I enter here")

    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "lxml")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:           
            continue       
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):         
            continue
        if href in internal_urls:
            # already in the set
            continue
        urls.add(href)
        
    return urls