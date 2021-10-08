import requests
from bs4 import BeautifulSoup
from math import *


category_url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
reponse = requests.get(category_url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")
emplacement = soup.find_all("strong")
total_number_books = emplacement[1].string
print(total_number_books)

number_of_pages = ceil(int(total_number_books) / 20)
print(number_of_pages)


