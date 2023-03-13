DEF_FILEPATH = "todos.txt"  # Default Filepath


def printlist(todo_list_to_print):
    """ Prints a list, each item on a new line """
    for index, item in enumerate(todo_list_to_print, 1):
        item = item.strip("\n")
        print(f"{index}. {item}")


# Function gets todo_list from file, with default file already set to todo_list.txt
def get_todo_txt(filepath=DEF_FILEPATH):
    """ Reads a text file and returns the lines in the text file as a list """
    with open(filepath, "r") as file:
        todo_list_get = file.readlines()
    return todo_list_get


# Function to overwrite the save-file
def savefile_txt(todo_list_to_save, filepath=DEF_FILEPATH):
    """ Save a list by overwriting the input file (default=files/todos.txt) """
    with open(filepath, "w") as file:
        file.writelines(todo_list_to_save)
