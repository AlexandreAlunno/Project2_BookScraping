import requests
from bs4 import BeautifulSoup
import csv
from recuperation_URLs import recuperation_urls_books
from changing_page import next_page_url
from scrap_one_book import scrap_data_books

books_data = []
page_url = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
books_url = recuperation_urls_books(page_url)

for url in books_url:
    data = scrap_data_books(url)
    books_data.append(data)


en_tete = ["URL", "Categorie", "Titre", "Description", "UPC", "Type", "Prix Hors Tax", "Prix Avec Tax", "Tax", "Disponnibilité", "Nombre d'avis", "URL Couverture"]
with open("data_book_one_page.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for data in books_data:
        writer.writerow(data)


