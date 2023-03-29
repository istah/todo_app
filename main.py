def get_todos():
    with open('todos.txt', 'r') as file:
            todos_local = file.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            listItem = f"{index + 1}. {item.capitalize()}"
            print(listItem)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            print('Here is todos existig: ', todos)

            new_todo = input('Enter replacement for to do: ')
            todos[number] = new_todo + '\n'
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print('Edited succesfully! Here is the new list: ', todos)
        except ValueError:
            print('Your command is not valid.')
            continue
        
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number-1)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except ValueError:
            print('Your command is not valid.')
            continue
        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("I do not recognize this input")

print('Bye!')