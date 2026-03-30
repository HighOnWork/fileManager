import os

def showFiles():
    names = os.listdir('.')
    list_of_directories = f"The files in the current directory are: {names}"
    return list_of_directories
