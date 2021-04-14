"""Project Brief:
    - Need to add new movies to the collection on
    - Be able to list all the movies int the collection 
    - Find a movie by searching for the title
    """
import os  #Import the os module to use the clear screen function
movies = [] # create the empty list which will act as the database for now

def add_movie(): #function to add movies to the list
    os.system('cls') # call the clear screen at the start so it is clear what is going on
    title = input("\nPlease enter the title of the movie: ")
    director = input("Please enter the name of the director: ") #Get the key values from the user
    year = input("Please enter the year the movie was made: ")
    movies.append({
        "Title" : title,
        "Year" : year,  #assign the values to the keys, creating a dictionary per movie
        "Director" : director
    })
    print("\nThank you, your movie has been stored in the database!") #Give the user confirmation 
    input("Press any key to go back to the main menu") #Ask for input so the programme halts and the user can read confirmation


def list_movie(): #function to pull all the movies from the list
    os.system('cls') # clear the screen in windows only
    print("The movies in your collection are:\n")
    for movie in movies:
        print(f"{movie['Title']} which was directed by {movie['Director']} in the year {movie['Year']}") #Use string formatting to pull the info from the dict keys. make sure to use the opposite 
    input("Press any key to go back to the main menu")                                                   #quote marks on the keys, to the ones you write the print statement with or pyhton thinks you have ended the print staement 
       

def find_movie(): # find movie function
    os.system('cls')
    search_title = input("Please enter the Title of the movie to search: ") # get the title of the film from the user
    for search in movies: # iterate over the dictionaries in the movies list
        if search["Title"] == search_title: #compare the Title key of each dict to the search criteria
            print(f"\nYou have the movie {search['Title']} which was directed by {search['Director']} in {search['Year']} saved to your database!\n") #Use string formatting to  pull the info from the dict keys 
        else:
            print("That movie is not in your collection!")#if not in the list give the user feedback
    input("Press any key to go back to the main menu")    #ask for input to pause program so the user understands 


def Main(): #the main function of the programme
    os.system('cls')
    print("Hello, Welcome to the Movie database!!!") #only print the welcome message once, so outside the for loop
    flag = "" # create a flag variable to check against and keep repeating the main menu
    while flag != "q": #only if the user enters q will the app stop
        flag = input("""\nPlease select one of the following options:
        Press a to add a new movie
        Press l to list all movies  
        Press f to search movies
        Press q to quit the app
        Enter selection: """) #this is the main menu and the central point of the programme 
        if flag.lower() == "a":
            add_movie()
        elif flag.lower() == "l": # the control flow logic that calls the functions based on user input
            list_movie()
        elif flag.lower() == "f": #using the.lower() function in case the user enters a capital letter
            find_movie()
        elif flag.lower() == "q":
            flag = "q"
        os.system('cls')

Main() # call the main function to get the programme started

#Improvements that can be made:
user_options = {
    "a": add_movie, #create a dictionary of first clas functions. AKA functions that dont run because they dont have ()
    "l": list_movie,
    "f": find_movie,
    "q": "q"
}
def main():
    os.system('cls')
    print("Hello, Welcome to the Movie database!!!") 
    flag = ""
    while flag != "q": 
        flag = input("""\nPlease select one of the following options:
        Press a to add a new movie
        Press l to list all movies  
        Press f to search movies
        Press q to quit the app
        Enter selection: """)
        if flag in user_options: #replace the whole if statement logic with a first class function dictinary slelection
            selected_function = user_options[flag] #create a variable then assign the first class function selected
            selected_function() #selected_function now takes on whichever function was selected so it can be run by using the variable name with the () to call it
        else:
            input("unknown command, press enter to go back to main menu")
        os.system('cls')


