from bs4 import BeautifulSoup
from parsers.book_parser import BookParser
from locators.all_books_page_locator import AllBooksPageLocators


class AllBooksPage:

    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')#takes in the page_Content paramater then creates the parsed html object of soup

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)] #creates a porpery that contains all the books on the page found by the BOOKS locator tag and stores them in a BookParser object