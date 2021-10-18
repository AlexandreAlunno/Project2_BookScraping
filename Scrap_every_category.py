import csv
from recuperation_URLs import recuperation_urls_books
from Scrap_one_book import scrap_data_books
from next_page import next_buton
from find_categories_url import find_categories_url
last_page = False
books_data = []
home_url = "http://books.toscrape.com/index.html"
count = 0
page_urls = find_categories_url(home_url)

for categories in page_urls:
    page_url = categories
    last_page = False
    while last_page == False:
        books_url = recuperation_urls_books(page_url)


        for url in books_url:

            data = scrap_data_books(url)
            books_data.append(data)

        next_page, last_page = next_buton(page_url)
        page_url = next_page


