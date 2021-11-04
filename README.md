
# Project2_BookScraping
This project was made to scrap the data from the site http://books.toscrape.com/index.html \
Files overview: \
recuperation_URLs.py \
find_categories.py \
next_page.py \
image_download.py \
scrap_one_book.py \
scrap_one_page.py \
scrap_one_category.py \
scrap_every_category.py\
changing_page.py \
README.md \
requirements.txt \
categories_csv_files (empty folder to store csv and image, see last available script)
***
Installation:\
in the cmd go to the folder Project2_BookScraping \
Set up a virtual environement: \
In the cmd use the command: python -m venv <environment name> \
activate the virtual environment with the command : .\venv\Scripts\activate \

To run the different scripts you'll need to install the requirements as defined in the requirements.txt file \
Use the command : pip install -r requirements.txt \

Now you can run the scripts below
***
## Available scripts
### scrap_one_book.py
Will scrap the data from the page of a book
### scrap_one_page.py
Will scrap the data from one page
Will write the data in a csv file called data_book_one_page.csv
### scrap_one_category.py
Will scrap the data of one category, going through every page of the category
Will write the data in a csv file called data_book_one_category.csv
### scrap_every_category.py
Will the scrap the data of every book in every category
Will create within the folder categories_csv_files a folder named after the category containing the csv file of the data of all the books of the category + the .jpg image of the cover of each books
Each image is called after the UPC of the book


