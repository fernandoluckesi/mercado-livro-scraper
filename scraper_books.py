import requests
from parsel import Selector
import database_connect
import scraper_categories_books
import json
import unicodedata


def get_book_details(category_url, category_value):
  base_url = category_url

  response = requests.get(base_url)
  selector = Selector(text=response.text)

  books = selector.css(".prateleiraProduto").getall()
  array_books = []
  for book in books:
    selector_book = Selector(book)
    url_book_details = selector_book.css(".prateleiraProduto__informacao__nome a::attr(href)").get()
    response_book_details = requests.get(url_book_details)
    selector_book_details = Selector(text=response_book_details.text)
    thumbnail_book = selector_book_details.css("meta[itemprop='image']::attr(content)").get()
    title_book = selector_book_details.css(".productName::text").get()
    description_book = selector_book_details.css("meta[itemprop='description']::attr(content)").get()
    author_book = selector_book_details.css("td[class='value-field Colaborador']::text").re(r"Autor:\w{1,},\s\w{1,}")
    if len(author_book) > 0:
      author_book = author_book[0][6:]
    else:
      author_book = []
    publishing_company_book = selector_book_details.css("td[class='value-field Editora']::text").get()
    year_edition_book = selector_book_details.css("td[class='value-field Ano']::text").get()
    edition_book = selector_book_details.css("td[class='value-field Edicao']::text").get()
    language_book = selector_book_details.css("td[class='value-field Idioma']::text").get()
    country_book = selector_book_details.css("td[class='value-field Pais']::text").get()
    pages_count_book = selector_book_details.css("td[class='value-field Paginas']::text").get()
    isbn_book = selector_book_details.css("td[class='value-field ISBN']::text").get()

    dict_book = {
      "title": title_book,
      "author": author_book,
      "publishing_company": publishing_company_book,
      "year_edition": year_edition_book,
      "edition": edition_book,
      "language": language_book,
      "country": country_book,
      "pages_count": pages_count_book,
      "isbn": isbn_book,
      "category": category_value,
      }

    array_books.append(dict_book)

  return array_books
  

def scraper_books():
  categories = scraper_categories_books.get_categories()

  for category in categories:

    category_url = category["category_url"]

    category_name = category["category_name"]

    category_value = category["category_value"]

    database_connect.insert_books(get_book_details(category_url, category_value))
    print(f"categoria: {category_name} inserida no banco")
