import requests
from pages1.all_books_page import AllBooksPage

page_content = requests.get('http://books.toscrape.com').content       #get the page content from the website
page = AllBooksPage(page_content)      #feed the page_content to the all books class to make an object of the page as a soup with a book parsing proprty 

books = page.books  #call the books function to parse the soup and pull all the books into a list to be stored in books 

for book in books:  #iterate over each of the books in the list 
    print(book) #this will call the __repr__ method of the book