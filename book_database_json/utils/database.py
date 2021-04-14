"""
This database will store and retrieve books from a list.
"""
import os #import for screen clearing
from utils.file_operations import read_database, save_database


def add_book():
    os.system('cls')
    books = read_database()
    name = input("Please enter the name of the book: ")
    author = input("Please enter the name of the author: ") #Grab both the variables from the user
    books.append({
        'name': name, 
        'author': author, #add all the variables to create a dictionary item in the list
        'read': False
        })
    save_database(books)
    print("\nThank you, your book has been stored in the database!") #Give the user confirmation 
    input("Press any key to go back to the main menu") #Ask for input so the programme halts and the user can read confirmation

    


def list_books():
    os.system('cls')
    books = read_database()
    for book in books: #Loop through all the books printing the nice format string as you iterate
        print(f"You have {book['name']} in your list which was written by {book['author']}.")
    input("Press any key to go back to the main menu") #Ask for input so the programme halts and the user can read confirmation


def read_book():
    os.system('cls')
    books = read_database()
    search_name = input("Please enter the name of the book that you have read: ") #get the book name from user

    for search in books: #iterate through the list of dictionaries
        if search['name'] == search_name: #if the search name matches execute this block
            print(f"You have now marked the book {search_name}, as read")
            search['read'] = True#change the boolean value to true if the book is in the list  
            save_database(books)
            input("Press any key to go back to the main menu") #Ask for input so the programme halts and the user can read confirmation   
            break
    else: #putting the else codeo n the for loop instead of the if statement solves so many problems
        print(f"You dont habve the book {search_name} in your database!")       
        input("Press any key to go back to the main menu") #Ask for input so the programme halts and the user can read confirmation
        


def del_book():
    os.system('cls')
    books = read_database()
    search_name = input("Please enter the name of the book that you would like to delete: ")

    for search in books: #iterate through the list of dictionaries
        if search['name'] == search_name: #if the search name matches execute this block 
            books = [book for book in books if book['name'] != search_name] #create a new list without the dictionary that was deleted
        #this comprehension says create a variable called book to store the outcome of a loop through the books list but dont loop through the data that contains the name of the deleted book
        #After each loop, another ditionary entry is added to the list 
            save_database(books)
            input(f"Your book {search_name} has been deleted. Press any key to go back to the main menu") #Ask for input so the programme halts and the user can read confirmation
            break
    else: #putting the else codeo n the for loop instead of the if statement solves so many problems
        print(f"You dont habve the book {search_name} in your database!")       
        input("Press any key to go back to the main menu") #Ask for input so the programme halts and the user can read confirmation

if __name__ == '__main__':
 
    read_book()
    list_books()

    #need to change the search method of the read function as it is iterating over each book then printing the notin list if it is not the book. try an if in sta