import urllib3
from bs4 import BeautifulSoup
import requests
http = urllib3.PoolManager()

alphebet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#new_quote_page = quote_page + "?index=" + alphebet[x]
all_in_one_page = "https://csrc.nist.gov/glossary?sortBy-lg=relevance&ipp-lg=all"
quote_page = "https://csrc.nist.gov/glossary"
tl = "term-list-item-"
mylist = []
# method to get all terms

print("indexing: "+ all_in_one_page)
page = requests.get(all_in_one_page)
soup = BeautifulSoup(page.content, 'html.parser')
for x in range(9419):
    term = tl + str(x)
    name_box = soup.find("div", id= {term})
    print(name_box)
#name = name_box.text.strip()  # strip() is used to remove starting and trailing





