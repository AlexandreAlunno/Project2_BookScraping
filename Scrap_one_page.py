import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")

#récupération categorie
genre = soup.find_all("a")
categorie = []
for type in genre:
    categorie = [genre[3].string]

print(categorie)


#récupération du titre
titre = soup.find_all("h1")
titre_officiel = []
for title in titre:
    titre_officiel.append(title.string)
print(titre_officiel)

#récupération de la description
description = soup.find_all("p")
product_description = []
for descri in description:
    product_description = [description[3].string]
print(product_description)

#récupération des données du tableau de fin de page
tableau = soup.find_all("td")
data_tableau = []
for data in tableau:
    data_tableau.append(data.string)

print(data_tableau)

book_data = categorie + titre_officiel + product_description + data_tableau

en_tete = ["Categorie", "Titre", "Description", "UPC", "Type", "Prix Hors Tax", "Prix Avec Tax", "Tax", "Disponnibilité", "Nombre d'avis"]
with open("data_livre.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    writer.writerow(book_data)