import requests
from bs4 import BeautifulSoup
from math import *


def find_categories_name(category_url):
    reponse = requests.get(category_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    # find the category
    final_category_list = []
    category_in_html = soup.find("ul", class_='nav nav-list')
    # print(category_in_html)
    category_balise = category_in_html.findChildren("a", recursive=True)
    # print(category_balise)

    for category in category_balise:
        category_url = category.get("href")
        #print(category_url)
        category_list = category_url.split("../books/")
        #print(category_list)
        if len(category_list) > 1:
            split_category_list = category_list[1].split("/index.html")
            final_category_list.append(split_category_list[0])
    print(final_category_list)
    return final_category_list





def next_page_url(category_url):
    reponse = requests.get(category_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    emplacement = soup.find_all("strong")
    total_number_books = emplacement[1].string
    url_next_page = []
    # print(total_number_books.string)

    # calculate the number of pages from the total number of books
    number_of_pages = ceil(int(total_number_books) / 20)
    print(number_of_pages)



        # replace the url by the url of the next page
    for page in range(2, number_of_pages + 1):
        complete_url = f"http://books.toscrape.com/catalogue/category/{category}/page-{page}.html"
        url_next_page.append(complete_url)
    print(url_next_page)
    return url_next_page


if __name__ == '__main__':
    home_url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    #trouve liste categorie
    category_name_list = find_categories_name(home_url)
    category = category_name_list[1]
    #pour chaque categorie remplace dans l'url le nom de categorie
    category_url = f"http://books.toscrape.com/catalogue/category/{category}/index.html"
    reponse = requests.get(category_url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    next_page_url(category_url)




