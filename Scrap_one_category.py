import requests
from bs4 import BeautifulSoup
import csv
from recuperation_URLs import recuperation_urls_books
from Scrap_one_book import scrap_data_books
from next_page import next_buton

last_page = False
books_data = []
#1.get first page url
page_url = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"

#2.get url of each books on the page
while last_page == False:
    books_url = recuperation_urls_books(page_url)
    #print(books_url)
    #3.scrap data on page, save datas in variable
    for url in books_url:
        data = scrap_data_books(url)
        books_data.append(data)
    #find url of the next page
    next_page, last_page = next_buton(page_url)
    page_url = next_page
    #print(next_page)

print(books_data)

en_tete = ["URL", "Categorie", "Titre", "Description", "UPC", "Type", "Prix Hors Tax", "Prix Avec Tax", "Tax", "Disponnibilité", "Nombre d'avis", "URL Couverture"]
with open("data_livre_one_category.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for data in books_data:
        writer.writerow(data)