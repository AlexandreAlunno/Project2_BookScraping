import requests
from bs4 import BeautifulSoup


home_url = "http://books.toscrape.com/index.html"
reponse = requests.get(home_url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")
root_url = "http://books.toscrape.com/"



#find the category
category_list = []
category_in_html = soup.find("ul", class_='nav nav-list')
#print(category_in_html)
category_balise = category_in_html.findChildren("a", recursive=True)
#print(category_balise)

for category in category_balise:
    category_url = category.get("href")
    #print(category_url)
    complete_url = root_url + category_url
    category_list.append(complete_url)
#print(complete_url)
print(category_list)



if __name__ == '__main__':
    url = "http://books.toscrape.com/index.html"
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    root_url = "http://books.toscrape.com/"