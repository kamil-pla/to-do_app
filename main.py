import functions
import time

now = time.strftime("%d %b, %Y - %H:%M")
print('It is: ', now)

while True:
    user_action = input("Type add, show, edit, complete or exit(0): ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = input("Type the task name: ") + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos, 'todos.txt')

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)
        print('')    
    
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()
        
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}. {item.capitalize()}"
                print(row)
            print('')

            number = int(input("Number of task to edit: "))
            number = number - 1

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, 'todos.txt')
        
        except ValueError:
            print("\n<!> Error: Your command is not valid\n")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(input("Number of task to be completed: "))
        
            todos = functions.get_todos()          
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos, 'todos.txt')

            messsage = f"Todo -{todo_to_remove}- was removed from the list"
            print(messsage)
        
        except IndexError:
            print("\n<!> Error: Your task index is not valid\n")
            continue

    elif "exit" in user_action or '0' in user_action:
        break
    else:
        print('Command is not valid')

print("Bye!")