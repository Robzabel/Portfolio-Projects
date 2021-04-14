"""
The functions to save and load the database from a file
"""
import json

def save_database(content):
    with open("saved_database.txt", "w") as file:
        json.dump(content, file)


def read_database():
    with open("saved_database.txt", "r") as file:
        file_contents = json.load(file)
        return file_contents

