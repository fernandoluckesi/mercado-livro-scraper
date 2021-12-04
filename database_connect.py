from pymongo import MongoClient
import copy


DB_HOST = "localhost"
DB_PORT = "27017"


def insert_books(data):
  try:
    client = MongoClient(DB_HOST, 27017)
    print("Connected successfully!!!")
    db = client.mercadoLivro
    db.books.insert_many(data)
    client.close()
  except:
    print("Could not connect to MongoDB")


def insert_categories(data):
  try:
    client = MongoClient(DB_HOST, 27017)
    print("Connected successfully!!!")
    db = client.mercadoLivro
    db.categories.insert_many(data)
    client.close()
  except:
    print("Could not connect to MongoDB")


if __name__ == "__main__":
    main()
