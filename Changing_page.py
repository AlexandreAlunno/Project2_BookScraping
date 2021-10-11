import requests
from bs4 import BeautifulSoup
from math import *


#calculate the number of books in a category
category_url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
reponse = requests.get(category_url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")
emplacement = soup.find_all("strong")
total_number_books = emplacement[1].string
print(total_number_books.string)

#calculate the number of pages from the total number of books
number_of_pages = ceil(int(total_number_books) / 20)
print(number_of_pages)






category = "mystery_3"
for page in range(2, number_of_pages + 1):
    url_next_page = f"http://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html"
    print(url_next_page)

