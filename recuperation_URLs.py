import requests
from bs4 import BeautifulSoup

def recuperation_urls_books(url):
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    url_next_book = soup.find_all("div", class_="image_container")
    list_url_book = []

    for image in url_next_book:
        incomplete_url = image.findChildren("a", recursive=False)
        image_url = incomplete_url[0].get("href")
        short_url = image_url.split("../../..")
        root_url = "http://books.toscrape.com/catalogue"
        complete_url = root_url + short_url[1]
        list_url_book.append(complete_url)
    return list_url_book



if __name__ == '__main__':
    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    url_next_book = soup.find_all("div", class_="image_container")
    list_url_book = []
    recuperation_urls_books(url)

