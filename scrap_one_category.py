import requests
from bs4 import BeautifulSoup
import csv
from recuperation_URLs import recuperation_urls_books
from scrap_one_book import scrap_data_books
from next_page import next_buton

last_page = False
books_data = []
page_url = "http://books.toscrape.com/catalogue/category/books/classics_6/index.html"

while last_page == False:
    books_url = recuperation_urls_books(page_url)

    for url in books_url:
        data = scrap_data_books(url)
        books_data.append(data)
    next_page, last_page = next_buton(page_url)
    page_url = next_page


en_tete = ["URL", "Categorie", "Titre", "Description", "UPC", "Type", "Prix Hors Tax", "Prix Avec Tax", "Tax", "Disponnibilité", "Nombre d'avis", "URL Couverture"]
with open("data_book_one_category.csv", "w", encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for data in books_data:
        writer.writerow(data)