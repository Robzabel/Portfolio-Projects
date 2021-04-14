import os
import tkinter as tk
from tkinter import ttk, filedialog




def create_file(content="", title="Untitled"):          #Create a function to make new files 
    text_area = tk.Text(notebook)       #this creates a text area in the notebook, text area takes up vertical and horizontal space
    text_area.insert("end", content) #starts the opened file content at the end which is actually the beginning because it is a blank file
    text_area.pack(fill="both", expand=True)     #Fills the entire notebook
    notebook.add(text_area, text=title)      #adds the text area to the notebook and gives it a title for the window
    notebook.select(text_area)          #similar to focus, this will select the text area when the application is run, also when we create multiple windows, the lates one will be selected




def save_file():            #Creating a function to save out notes
    file_path = filedialog.asksaveasfilename()  #this module function asks the user through the system dialogs, where they want to save their file. it doesnt actually do the writing to memory

    try:
        filename = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select()) #selects the filename of the current open notebook file
        content = text_widget.get("1.0","end-1c") #grabs the content of the current text file from line 1 character 0 "(1.0)" until the end but 1 character because there is aleays a blank character at the end of the file

        with open(file_path, "w") as file: #use a context editor to open the file in write mode
            file.write(content)         #write the content to the file which is then automatically closed 
    
    except (AttributeError, FileNotFoundError): #handle possible errors
        print("Save operation cancelled")
        return

    notebook.tab("current", text=filename) #uses the file name that we extracted at the start of the function to rename the notebook tab once it has been saved



def open_file():
    file_path = filedialog.askopenfilename() #uses the system dialog to ask the user which file they want to open
    try:
        filename = os.path.basename(file_path)

        with open(file_path, "r") as file: #opens the file in read mode
            content = file.read()   #extracts the content of the file 
    except (AttributeError, FileNotFoundError):
        print("Open operation cancelled")
        return
    create_file(content, filename) #passes the content of the file and the name to the create file function



root=tk.Tk()                #Create the root container
root.title("Python Text Editor") #give the main container window a title
root.option_add("*tearOff", False) #stopps the menu from being seperated "torn off" from the main window

main = ttk.Frame(root)      #Create the Frame called main and specify that it is in the root container
main.pack(fill="both", expand=True, padx=1, pady=(4,0))    #set the packing for the main frame, he frame takes up the whole container. no side is specified so it will be side="top" by default

menubar = tk.Menu()         #Create the menu bar, this will look different depending on OS
root.config(menu=menubar)   #Tells the root container that menubar is the main menu widget

file_menu = tk.Menu(menubar)    #creates a file menu within the menubar
menubar.add_cascade(menu=file_menu, label="File")    #makes the file menu a dropdown element from the menu bar with the title File

file_menu.add_command(label="New", command=create_file ) #create a button that opens a new file and has the acceloratior which binds shortcut keys
file_menu.add_command(label="Open", command=open_file )  #add the command to open a file, and short cut keys
file_menu.add_command(label="Save", command=save_file)  #add a button to use the save file function, and short cut keys

notebook = ttk.Notebook(main)               #create the notebook and place it in the main frame
notebook.pack(fill="both", expand=True)     #fill is set to both and expand is True so this  notebook takes up thewhole frame which takes up the whole root container
create_file()


root.mainloop()