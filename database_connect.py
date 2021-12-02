from pymongo import MongoClient
import copy


DB_HOST = "localhost"
DB_PORT = "27017"


try:
   client = MongoClient(DB_HOST, 27017)
   print("Connected successfully!!!")
except:
  print("Could not connect to MongoDB")


def insert_data(data):
    db = client.testeDb
    try:
      db.books.insert_many(data)
      print("Data entered successfully")
    except:
      print("Data not entered")
    client.close()


if __name__ == "__main__":
    main()
