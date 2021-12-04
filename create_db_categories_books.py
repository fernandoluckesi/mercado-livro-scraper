import database_connect
import scraper_categories_books
 
 
database_connect.insert_categories(scraper_categories_books.get_categories())
