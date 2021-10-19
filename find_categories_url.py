import requests
from bs4 import BeautifulSoup


def find_categories_url(home_url):

    reponse = requests.get(home_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    root_url = "http://books.toscrape.com/"
    category_list = []
    category_names = []
    category_in_html = soup.find("ul", class_='nav nav-list')
    category_balise = category_in_html.findChildren("a", recursive=True)

    for category in category_balise:
        category_url = category.get("href")
        complete_url = root_url + category_url
        category_list.append(complete_url)
    category_list.pop(0)

    for names in category_list:
        first_split = names.split("http://books.toscrape.com/catalogue/category/books/")
        second_split = first_split[1].split("/index.html")
        third_split = second_split[0].split("_")
        category_names.append(third_split[0])
    return category_list, category_names


if __name__ == '__main__':
    home_url = "http://books.toscrape.com/index.html"
    reponse = requests.get(home_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    root_url = "http://books.toscrape.com/"
    category_list, category_names = find_categories_url(home_url)




