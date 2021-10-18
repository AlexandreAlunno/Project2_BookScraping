import requests
from bs4 import BeautifulSoup


def find_categories_url(home_url):

    reponse = requests.get(home_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    root_url = "http://books.toscrape.com/"
    category_list = []
    category_in_html = soup.find("ul", class_='nav nav-list')
    category_balise = category_in_html.findChildren("a", recursive=True)



    for category in category_balise:
        category_url = category.get("href")

        complete_url = root_url + category_url
        category_list.append(complete_url)
    category_list.pop(0)
    return category_list


if __name__ == '__main__':
    home_url = "http://books.toscrape.com/index.html"
    reponse = requests.get(home_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    root_url = "http://books.toscrape.com/"
    find_categories_url(home_url)


