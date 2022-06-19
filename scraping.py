from asyncio.windows_events import NULL
import requests
from bs4 import BeautifulSoup
from utils.constants import URL

from utils.data_classes import my_dictionary


# URL to extract data from
url = URL

# Make a request
r = requests.get(url=url)

# Parsing the html
soup = BeautifulSoup(r.content, 'html.parser')

page = soup.find("div", class_="col-sm-8 col-md-9")

books_list = page.find("ol", class_="row").find_all('li')

i = 0
books_info = my_dictionary()

for book in books_list:
    books_info.add(i, my_dictionary())
    books_info[i].add('title', book.find("a", {"title": True}).get('title'))
    books_info[i].add('price', book.find("p", {"class": "price_color"}).text)
    books_info[i].add('stars', book.find("article", {"class": "product_pod"}).find('p').get('class')[1])
    i += 1

print(books_info)