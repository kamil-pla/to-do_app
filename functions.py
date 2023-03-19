def get_todos(filepath='todos.txt'):
    """ Read the text file and return the list of tasks"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """ Save the new list of tasks in the specified text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
