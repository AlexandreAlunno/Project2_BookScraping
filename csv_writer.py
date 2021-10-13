import csv


en_tete = ["URL", "Categorie", "Titre", "Description", "UPC", "Type", "Prix Hors Tax", "Prix Avec Tax", "Tax", "Disponnibilité", "Nombre d'avis", "URL Couverture"]
with open("data_livre.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    writer.writerow(book_data)