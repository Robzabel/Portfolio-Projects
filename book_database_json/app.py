from utils import database #import the database module to access the functions
import os # import the OS module to access the screen clearing function
from utils.file_operations import read_database, save_database

USER_CHOICE = """ 
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """ #create a nice user menu as a global variable
user_options = { #turn all the functions from the database module into first class functions to be used as menu selections
    'a' : database.add_book,
    'l' : database.list_books, #calling without the () makes the functions first class and wont execute them
    'r' : database.read_book,
    'd' : database.del_book
}
def menu(): #main function of app
    user_input = '' #create amatching criteria and leave empty to hold the menu choices
    os.system('cls')
    print("Welcome to the Book Database!")
    while user_input != 'q':
        user_input = input(USER_CHOICE) #display the menu and get the choice from the user
        if user_input in user_options:#check if the users choice is in the first class function dictionary
            action = user_options[user_input] #if the choice is in the dictionary save the variable to execute
            action() #execute the users choice function
        elif user_input == 'q': #break the while loop if the user presses q
            
            break
        else:
            input("unknown command, press enter to make another selection") #check the user input is from the menu options
        os.system('cls')

menu()   #call the menu function to start the app
