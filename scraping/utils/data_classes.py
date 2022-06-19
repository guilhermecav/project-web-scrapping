from bs4 import BeautifulSoup
import requests

from scraping.utils.constants import PARSER, URL

class my_dictionary(dict):
  
    # __init__ function
    def __init__(self):
        self = dict()
          
    # Function to add key:value
    def add(self, key, value):
        self[key] = value


class BooksScraper():
    def __init__(self, url):
        self.url = url
    
    # Request data from a given URL
    def request(self):
        return requests.get(self.url)

    # Parse data into html format
    def html_parsing(self):
        return BeautifulSoup(self.request().content, PARSER)

    def get_list_of_books_info(self):
        books_list = self.html_parsing().find("div", class_="col-sm-8 col-md-9").find("ol", class_="row").find_all('li')
        
        i = 0
        books_info = my_dictionary()

        for book in books_list:
            books_info.add(i, my_dictionary())
            books_info[i].add('title', book.find("a", {"title": True}).get('title'))
            books_info[i].add('price', book.find("p", {"class": "price_color"}).text)
            books_info[i].add('stars', book.find("article", {"class": "product_pod"}).find('p').get('class')[1])
            i += 1

        return books_info