import requests
from bs4 import BeautifulSoup
import csv



def scrap_data_books(book_url):
    reponse = requests.get(book_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    url_page = [book_url]

    #récupération categorie
    genre = soup.find_all("a")
    categorie = []
    for type in genre:
        categorie = [genre[3].string]
    #print(categorie)


    #récupération du titre
    titre = soup.find_all("h1")
    titre_officiel = []
    for title in titre:
        titre_officiel.append(title.string)
    #print(titre_officiel)


    #récupération de la description
    description = soup.find_all("p")
    product_description = []
    for descri in description:
        product_description = [description[3].string]
    #print(product_description)


    #récupération des données du tableau de fin de page
    tableau = soup.find_all("td")
    data_tableau = []
    for data in tableau:
        data_tableau.append(data.string)
    #print(data_tableau)

    #récupération image + reconstruction url complète
    image = soup.find_all("img")
    image_url = image[0].get("src")
    incomplete_url = image_url.split("../..")
    root_url = "http://books.toscrape.com"
    image_complete_url = [root_url + incomplete_url[1]]
    #print(complete_url)

    book_data = url_page + categorie + titre_officiel + product_description + data_tableau + image_complete_url
    #print(book_data)
    return book_data




if __name__ == '__main__':
    book_url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
    scrap_data_books(book_url)