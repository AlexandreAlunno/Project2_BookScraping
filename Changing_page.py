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
#print(total_number_books.string)

#calculate the number of pages from the total number of books
number_of_pages = ceil(int(total_number_books) / 20)
#print(number_of_pages)

#find the category
category_name = []
category_in_html = soup.find("ul", class_='nav nav-list')

#print(category_in_html)

next_category_url = category_in_html.findChildren("li", recursive=True)
#find children "a"
category = next_category_url[4].get("href")
category_name.append(category)
print(next_category_url[4])



#replace the url by the url of the next page

"""for page in range(2, number_of_pages + 1):
    url_next_page = f"http://books.toscrape.com/catalogue/category/books/{category}/page-{page}.html"
    #print(url_next_page)"""



