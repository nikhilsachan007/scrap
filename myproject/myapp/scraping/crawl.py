from myapp.scraping.get_all_website_links import get_all_website_links
internal_urls = set()
external_urls = set()
total_urls_visited = 0
def crawl(url, max_urls):

    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls) 