import requests
from bs4 import BeautifulSoup
import csv
import json

TERM_VAL = []

print(type(TERM_VAL), TERM_VAL)
print()


url = "https://csrc.nist.gov/glossary/term/AIC"

r = requests.get(url)
# makes an item to scrape the html content with the html parser
soup = BeautifulSoup(r.content, 'html.parser')








data={}

#TODO EDIT FOR TERM PAGE


#table = soup.find('div', attrs = {'id':'results-container'})
# print(table)
#for x in table.findAll('div', attrs = {'class':'col-sm-12 term-list-title'}):
    #temp = str((x.find('a').contents[0]))
    #data[temp] = ""










# gathers the Abreviation data
Abrevation_Data = soup.find('a', attrs={'id':'term-abbr-link-0'}).contents[0]
print(Abrevation_Data)

# Gather Definition
Definition_Data = soup.find('i', attrs={'id':'term-def-none'}).contents[0]
print(Definition_Data)

# Gather source
Source_Data = soup.find('a', attrs={'id':'term-abbr-0-src-link-0'}).contents[0]
print(Source_Data)
print()



print(type(TERM_VAL), TERM_VAL)


