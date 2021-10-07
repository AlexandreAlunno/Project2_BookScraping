import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"

def scrap_data_books(url):
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")

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
    complete_url = [root_url + incomplete_url[1]]
    #print(complete_url)

    book_data = categorie + titre_officiel + product_description + data_tableau + complete_url

    return book_data

book_data = scrap_data_books(url)

print(book_data)

en_tete = ["Categorie", "Titre", "Description", "UPC", "Type", "Prix Hors Tax", "Prix Avec Tax", "Tax", "Disponnibilité", "Nombre d'avis", "URL Couverture"]
with open("data_livre.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    writer.writerow(book_data)