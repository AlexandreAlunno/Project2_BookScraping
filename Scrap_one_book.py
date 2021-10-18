import requests
from bs4 import BeautifulSoup
import csv



def scrap_data_books(book_url):
    #book_url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
    reponse = requests.get(book_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    url_page = [book_url]
    genre = soup.find_all("a")
    categorie = []
    for type in genre:
        categorie = [genre[3].string]


    #récupération du titre
    titre = soup.find_all("h1")
    titre_officiel = []
    for title in titre:
        titre_officiel.append(title.string)



    #récupération de la description
    description = soup.find_all("p")
    product_description = []
    for descri in description:
        product_description = [description[3].string]



    #récupération des données du tableau de fin de page
    tableau = soup.find_all("td")
    data_tableau = []
    for data in tableau:
        data_tableau.append(data.string)


    #récupération image + reconstruction url complète
    image = soup.find_all("img")
    image_url = image[0].get("src")
    incomplete_url = image_url.split("../..")
    root_url = "http://books.toscrape.com"
    image_complete_url = [root_url + incomplete_url[1]]

    book_data = url_page + categorie + titre_officiel + product_description + data_tableau + image_complete_url
    return book_data




if __name__ == '__main__':
    book_url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
    scrap_data_books(book_url)