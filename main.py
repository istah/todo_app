
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            for index, item in enumerate(todos):
                listItem = f"{index + 1}. {item.capitalize()}"
                print(listItem)

        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            existing_todo = todos[number]
            print(existing_todo)
            edit = input('Enter replacement for to do: ')
            todos[number] = edit
            print('Edited succesfully! Here is the new list:')
            for item in todos:
                print(item.capitalize())

        case 'complete':
            number = int(input('Number of the todo to complete: '))
            todos.pop(number-1)
            print('Here is your updated list: ')
            for index, item in enumerate(todos):
                listItem = f"{index + 1}. {item.capitalize()}"
                print(listItem)

        case 'exit':
            break

        case _:
            print('I do not recognize this input.')

print('Bye!')