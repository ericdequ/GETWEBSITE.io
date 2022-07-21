# import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import json

# initializes base url, Dictionary for scrapping, and count for errors
base_url = "https://www.cms.gov/acronyms?searchterm=&items_per_page=30&viewmode=grid&page="
data = {}
Attribute_Error_count = 0
Other_Error_count = 0

# uses this code to iterate through all the pages
# to gather all acronyms since page can only display 30 results at a time
# Logic may vary per webpage

for x in range(147):
    url = base_url + str(x)

    # Make a variable that stores the HTML contents of the url
    r = requests.get(url)

    # makes an item to scrape the html content with the html parser
    soup = BeautifulSoup(r.content, 'html.parser')

    # print(soup)
    print("made a soup")

    # The Entire Table is copied
    table = soup.find('div', class_=['view-content', 'cols-2'])

    # iterate through all data to get specific info
    for y in table.findAll('tr'):
        try:
            # Try's to take selected data if cant it raises the error counter
            Term = str(y.find('td', attrs={'class': 'views-field views-field-title is-active'}).contents[0])
            Meaning = str(y.find('td', attrs={'class': 'views-field views-field-body'}).contents[0])
            data[Term] = Meaning
        except AttributeError:
            Attribute_Error_count = Attribute_Error_count + 1
        except:
            Other_Error_count = Other_Error_count + 1
            print("other error")

print("AttributeError total = ", Attribute_Error_count, " now starting to ship to Json")
print("Other Error total = ", Other_Error_count, " now starting to ship to Json")

# Dumps to Json file
with open('../JSONs/CMSdata.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# simple print statement to ensure the Json file completed dumping of contents
print(Other_Error_count)
