import requests
from bs4 import BeautifulSoup


def scrap_data_books(book_url):
    reponse = requests.get(book_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    url_page = [book_url]
    genre = soup.find_all("a")
    categorie = []
    for type in genre:
        categorie = [genre[3].string]

    titre = soup.find_all("h1")
    titre_officiel = []
    for title in titre:
        titre_officiel.append(title.string)

    descriptions = soup.find_all("p")
    product_description = []
    for description in descriptions:
        product_description = [descriptions[3].string]

    tableau = soup.find_all("td")
    data_tableau = []
    for data in tableau:
        data_tableau.append(data.string)

    image = soup.find_all("img")
    image_url = image[0].get("src")
    incomplete_url = image_url.split("../..")
    root_url = "http://books.toscrape.com"
    image_complete_url = [root_url + incomplete_url[1]]

    book_data = url_page + categorie + titre_officiel + product_description + data_tableau + image_complete_url
    return book_data


if __name__ == '__main__':
    book_url = 'http://books.toscrape.com/catalogue/orange-the-complete-collection-1-orange-the-complete-collection-1_914/index.html'
    book_data = scrap_data_books(book_url)
en_tete = ["URL", "Categorie", "Titre", "Description", "UPC", "Type", "Prix Hors Tax", "Prix Avec Tax", "Tax", "Disponnibilité", "Nombre d'avis", "URL Couverture"]

