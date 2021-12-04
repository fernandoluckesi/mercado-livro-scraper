import requests
from parsel import Selector
import database_connect


def get_categories():
  base_url = "https://www3.livrariacultura.com.br/livros"
  response = requests.get(base_url)
  selector = Selector(text=response.text)

  categories = selector.css("h4[class='livros even']").getall()
  categories_array_dict = []

  for category in categories:

    category_selector = Selector(category)
    category_url = category_selector.css("h4[class='livros even'] a::attr(href)").get()

    category_name = category_selector.css("h4[class='livros even'] a::attr(title)").get()

    category_value = category_selector.css("h4[class='livros even'] a::attr(href)").re(r"livros/.{1,}\?")[0]
    category_value = category_value[7:len(category_value) - 1]

    dict_category = {
      "category_url": category_url,
      "category_name": category_name,
      "category_value": category_value,
    }

    categories_array_dict.append(dict_category)

  return categories_array_dict


if __name__ == "__main__":
    database_connect.insert_categories(get_categories())
    