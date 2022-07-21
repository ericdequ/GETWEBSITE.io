import requests
from bs4 import BeautifulSoup
import csv
url = "https://csrc.nist.gov/glossary?sortBy-lg=relevance&ipp-lg=all"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)
quotes=[]  # a list to store quotes
table = soup.find('div', attrs = {'id':'results-container'})
# print(table)
for x in table.findAll('div', attrs = {'class':'col-sm-12 term-list-title'}):
    print(x.find('a').contents[0])