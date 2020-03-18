
def shownested(my_list):
  print("enters nested ")
  for list in my_list:
    nresponse = requests.get(list,timeout=5)
    soup = BeautifulSoup(nresponse.text,'lxml')
    nresponse.close()
    email=[]
    email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', nresponse.text)
    return email
  