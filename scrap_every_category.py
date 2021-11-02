# -- coding: utf-8 --:-
import os
import csv
import shutil
import requests
from recuperation_URLs import recuperation_urls_books
from scrap_one_book import scrap_data_books
from next_page import next_buton
from find_categories_url import find_categories_url

last_page = False
books_data = []
home_url = "http://books.toscrape.com/index.html"
number_category = 0
page_urls, category_names = find_categories_url(home_url)

for categories, names in zip(page_urls, category_names):
    page_url = categories
    last_page = False
    number_category += 1
    os.mkdir(f"categories_csv_files\\{number_category}_{names}")
    while last_page == False:
        books_url = recuperation_urls_books(page_url)
        for url in books_url:
            data = scrap_data_books(url)
            r = requests.get(data[11], stream=True)
            if r.status_code == 200:
                with open(f"categories_csv_files\\{number_category}_{names}\\{data[4]}.jpg", "wb") as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
            books_data.append(data)
        next_page, last_page = next_buton(page_url)
        page_url = next_page

    en_tete = ["URL", "Categorie", "Titre", "Description", "UPC", "Type", "Prix Hors Tax", "Prix Avec Tax", "Tax","Disponnibilité", "Nombre d'avis", "URL Couverture"]
    csv_file_name = f"categories_csv_files\\{number_category}_{names}\\{number_category}_{names}.csv"
    with open(csv_file_name, "w", errors="ignore") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(en_tete)
        for data in books_data:
            writer.writerow(data)
    books_data = []
    print(f"{names} is scrapped")
