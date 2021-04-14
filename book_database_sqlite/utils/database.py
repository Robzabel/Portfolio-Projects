"""
This database will store and retrieve books from information held in an SQLite DB
"""
import os #import for screen clearing
import sqlite3 #Import to connect to the database
from .database_connection import DatabaseConnection
from typing import List, Dict #import the list and dict identifiers for use with type hinting


def create_book_table() -> None:                                                                                     #This is a type hint and it signifies taht there is no return value from this function
    connection = sqlite3.connect("data.db")                                                                          #Create a connection to the specified database
    cursor = connection.cursor()                                                                                     #Create a cursor to issue instructions to the database

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')             #Issue the cursor instructions

    connection.commit()                                                                                              #Commit the instructions of the cursor from RAM to the database in NVRAM
    connection.close()                                                                                               #Close the connection to the database


def add_book() -> None:
    os.system("cls")
    name: str = input("Please enter the name of the book: ") #collect the variables for the table
    author = input("Please enter the name of the author: ")

    with DatabaseConnection("data.db") as connection:   #Use the new context manager to open the database connection, executute the code block then commit and close the connection on exit
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?, 0)',(name, author)) #use the ? marks to be replaced by values in the tuple to defend against SQL injection

    print(f'Your book {name} was entered into the database') 
    input("Press any key to go back to the main menu")


def list_books()->None:
    os.system('cls')
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books") # select all the information in the table books
    books = [{'name':row[0], 'author':row[1], 'read':row[2]} for row in cursor.fetchall()] #using the fetchall() method returns all the rows of the table as a list of tuples. Use comprehension to turn the tuples into a list of dictionaries which is stored in the variable books
    connection.close() #close the connection to the database, there is no need to commit as we have only read from not written to
    for book in books: #look through the elements of the dictionary list to print the contents to the user
        read = 'Yes' if book['read'] else 'No'#Yse the truthy and falsy values to chek if the book has been read. In the DB books are marked with 1 for read and 0 for not read. This statement says if the book is Truthy return yes if Falsy return no 0 is Falsy and >0 Truthy
        print(f"you have the book {book['name']}, written by {book['author']} in your collection, read: {read}")
    input("Press any key to go back to the main menu") #Ask for input so the programme halts and the user can read confirmation


def read_book()->None:
    os.system('cls')
    search_name = input("Please enter the name of the book that you have read: ") #get the book name from user
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?',(search_name,))#you must give the brackets a comma to make it a tuple or it is not going to be recognised
    connection.commit()
    connection.close()
    print(f"You have marked the book {search_name} as read.")
    input("Press any key to go back to the main menu") #Ask for input so the programme halts and the user can read confirmation
        

def del_book():
    os.system('cls')
    search_name = input("Please enter the name of the book that you would like to delete: ")
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name=?', (search_name,))#again the value that matches the ? must come from a tuple which must have (,) characters
    connection.commit()
    connection.close()
    input(f"Your book {search_name} has been deleted. Press any key to go back to the main menu")

if __name__ == '__main__':
 
    create_book_table()
    add_book()
    list_books()
    read_book()
    del_book()
    list_books()