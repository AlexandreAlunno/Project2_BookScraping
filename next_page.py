import requests
from bs4 import BeautifulSoup
from math import *



page_url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"

def number_of_page(page):
    reponse = requests.get(page_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    emplacement = soup.find_all("strong")
    total_number_books = emplacement[1].string
    url_next_page = []

    number_of_pages = ceil(int(total_number_books) / 20)
    print(number_of_pages)



def next_buton(page_url):
    reponse = requests.get(page_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    next_emplacement = soup.find("li", class_="next")
    if next_emplacement == None:
        last_page = True
        next_page_url = page_url
    else:
        last_page = False
        next_balise = next_emplacement.findChild("a", recursive=True)

        next_url = next_balise.get("href")

        root_url = page_url

        incomplete_url = root_url.split("index.html")

        next_page_url = incomplete_url[0] + next_url
    )
    return next_page_url, last_page






if __name__ == '__main__':
    reponse = requests.get(page_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    number_of_page(page_url)
    next_buton(page_url)
