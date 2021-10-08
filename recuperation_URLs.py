import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"

reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")

"""url_next_book = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
incomplete_url = str(url_next_book[0]).split('href="../../..')
book_url = incomplete_url[1].split('"')
print(book_url[0])"""

url_next_book = soup.find_all("div", class_="image_container")
#incomplete_url = url_next_book[0].findChildren("a", recursive=False)
#image_url = incomplete_url[0].get("href")
list_url_book = []

for image in url_next_book:
    incomplete_url = image.findChildren("a", recursive=False)
   #print(incomplete_url)
    image_url = incomplete_url[0].get("href")
    #print("image url: " + str(image_url))
    list_url_book.append(image_url)

print(list_url_book)

#print(url_next_book)
#for book in incomplete_url:
   # print(book)


"""next_book = soup.find_all("h3")
url_next_book = []
for adress in next_book:
    url_next_book.append(adress)
print(next_book)
print(url_next_book)"""