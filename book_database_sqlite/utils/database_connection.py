import sqlite3
class DatabaseConnection:
    def __init__(self, host):
        self.connection = None                                              #Creates a property for the connection to be held. initialise with None to keep blank
        self.host = host                                                    #Creates a property to hold the db file location passed to the context manager from the main programme

    
    def __enter__(self):                                                    #This code is executed on entry to the context manager
        self.connection = sqlite3.connect(self.host)                        #Creates an SQLite3 connection to the specified DB file
        return self.connection                                              #returns the connection property to the main programme that will be usein in the "as connection" value

    def __exit__(self, exc_type, exc_val, exc_tb):                          #This code is executed on exit of the context manager
        if exc_type or exc_val or exc_tb:                                   #This code checks if the exception paramaters have any values, if there are that means errors occured and the connection should be closed without commiting
            self.connection.close()                                         
        else:                                                               #If no errors commit and close the connection
            self.connection.commit()                                        #Commits the changes. If there are no changes, this code will still run but wont have any effect
            self.connection.close()                                         #Closes the connection to the database
