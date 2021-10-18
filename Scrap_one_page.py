import requests
from bs4 import BeautifulSoup
import csv
from recuperation_URLs import recuperation_urls_books
from Changing_page import next_page_url
from Scrap_one_book import scrap_data_books

books_data = []
#1.get first page url
page_url = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
#2.get url of each books on the page
books_url = recuperation_urls_books(page_url)

#3.scrap data on page, save datas in variable
for url in books_url:
    data = scrap_data_books(url)
    books_data.append(data)



en_tete = ["URL", "Categorie", "Titre", "Description", "UPC", "Type", "Prix Hors Tax", "Prix Avec Tax", "Tax", "Disponnibilité", "Nombre d'avis", "URL Couverture"]
with open("data_livre_one_page.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for data in books_data:
        writer.writerow(data)


