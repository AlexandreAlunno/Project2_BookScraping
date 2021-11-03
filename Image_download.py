import shutil
import requests
from bs4 import BeautifulSoup

book_url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
reponse = requests.get(book_url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")

image = soup.find_all("img")
image_url = image[0].get("src")
incomplete_url = image_url.split("../..")
root_url = "http://books.toscrape.com"
image_complete_url = [root_url + incomplete_url[1]]


r = requests.get(image_complete_url[0], stream=True)

if r.status_code == 200:
    with open("book1.jpg", "wb") as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)